#! /usr/bin/env python3

import logging
import time
from pathlib import Path
from typing import Any, Optional, Dict, List

import yaml
from PIL import Image

from hvv_display.hvv_display_client.client import AuthenticatedClient
from hvv_display.hvv_display_client import models
from hvv_display.hvv_display_client.api.departure_list_controller import departure_list
from hvv_display.hvv_display_client.api.init_request_controller import init


logging.basicConfig(level=logging.DEBUG)  # TODO: INFO


class HvvDisplay:
    """This is the main class glueing the API client to the LED Matrix display."""

    def __init__(self):
        self.logger = logging.getLogger("HvvDisplay")
        self.logger.info("Initializing HvvDisplay...")

        self.icons: Dict[str, Image] = {}  # Caches icons of transit lines

        with open(Path(__file__.parent.parent / "config.yaml"), "r") as f:
            self.config: Dict[str, Any] = yaml.safe_load(f)

        self.client: AuthenticatedClient = self.connect()
        if self.client is None:  # Connection could not be established
            return  # Exit

        self.run(self.config["update_period"], self.config['max_failures'])

    def connect(self) -> AuthenticatedClient:
        """Returns a client connected and authenticated to the Geofox API.

        :raises RuntimeError: Could not create connection to Geofox API.
        :return: Connected Geofox API client
        :rtype: AuthenticatedClient
        """
        client = AuthenticatedClient(
            self.config["api"]["auth"]["base_url"],
            self.config["api"]["auth"]["token"],
        )

        init_request = models.InitRequest(
            version=self.config["api"]["version"],
            language=self.config["api"]["language"],
            filter_type=models.DLRequestFilterType.HVV_LISTED,
        )

        init_response : models.InitResponse = init.sync_detailed(
            client=self.client,
            json_body=init_request,
        )

        if init_response.return_code == models.InitResponseReturnCode.OK:
            return client
        else:
            self.logger.error(f"Could not create connection to Geofox API. Error '{init_response.return_code}':\n'{init_response.error_text}'\n'{init_response.error_dev_info}'")
            raise RuntimeError(init_response.error_dev_info)

    def shutdown(self):
        self.logger.info("Shutting down")

    def run(self, period: int, max_failures: int):
        """Runs the main loop:
        - Query departures,
        - Draw them on a canvas, and
        - Show the canvas on the LED Matrix display.

        :param sleep: Time in seconds to sleep between updates
        :type sleep: int
        :param max_failures: Number of successive failures when to stop main loop
        :type max_failures: int
        """
        self.logger.debug(f"Update period: {period}")

        failure_counter : int = 0  # If reaches max_failures, abort loop

        try:
            while failure_counter <= max_failures:  # Main loop
                time.sleep(period)  # Sleep between updates
                self.logger.debug("Updating...")
                try:
                    departures: List[models.Departure] = self.get_departures()
                    canvas: Image = self.draw(departures)
                    self.show(canvas)
                except (
                    RuntimeWarning,
                    RuntimeError,
                ):
                    failure_counter += 1
                else:  # Successful run -> reset failure counter
                    failure_counter = 0

        except KeyboardInterrupt:
            self.shutdown()

    def get_departures(self) -> List[models.Departure]:
        """Get next departures from API.

        :raises RuntimeWarning: Could not receive departures successfully
        :return: List of departures
        :rtype: List[models.Departure]
        """
        dl_request = models.DLRequest(
            version=self.config["api"]["version"],
            language=self.config["api"]["language"],
            filter_type=models.DLRequestFilterType.HVV_LISTED,
            time=models.GTITime("jetzt"),  # Now
            stations=[
                models.SDName(station["name"], station["city"])
                for station in self.config["request"]["stations"]
            ],
            max_list=self.config["api"]["max_list"],
            service_types=[
                models.DLResponseServiceTypesItem.UBAHN,
                models.DLResponseServiceTypesItem.XPRESSBUS,
            ],
            use_realtime=True,
        )

        dl_response: models.DLResponse = departure_list.sync_detailed(
            client=self.client,
            json_body=dl_request,
        )

        if dl_response.return_code == models.DLResponseReturnCode.OK:
            return dl_response.departures
        else:
            self.logger.warning(f"Could not receive departures successfully. Error: '{dl_response.return_code}'\n'{dl_response.error_text}'\n'{dl_response.error_dev_info}'")
            raise RuntimeWarning(dl_response.error_dev_info)

    def draw(self, departures: List[models.Departure]) -> Image:
        """Draws departures on a blank canvas.

        :param departures: List of departures to draw
        :type departures: List[models.Departure]
        :return: Canvas with drawn departures
        :rtype: Image
        """

    def show(self, canvas: Image) -> None:
        """Shows the canvas on the LED Matrix display.

        :param canvas: Canvas to show
        :type canvas: Image
        """


if __name__ == "__main__":
    HvvDisplay()
