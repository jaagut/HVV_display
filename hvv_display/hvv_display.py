#! /usr/bin/env python3

import time
import logging
from pathlib import Path
from typing import Any, List, Dict

import yaml
from PIL import Image
from hvv_display.hvv_display_client.models.dl_response_service_types_item import DLResponseServiceTypesItem

from hvv_display_client.client import AuthenticatedClient
from hvv_display_client.models.departure import Departure
from hvv_display_client.models.dl_request import DLRequest
from hvv_display_client.models.dl_response import DLResponse
from hvv_display_client.models.gti_time import GTITime
from hvv_display.hvv_display_client.models.sd_name import SDName
from hvv_display.hvv_display_client.models.dl_request_filter_type import DLRequestFilterType

logging.basicConfig(level=logging.DEBUG)  # TODO: INFO


class HvvDisplay:
    """This is the main class glueing the API client to the LED Matrix display."""

    def __init__(self):
        self.logger = logging.getLogger('HvvDisplay')
        self.logger.info("Initializing HvvDisplay...")

        self.icons: Dict[str, Image] = {}  # Caches icons of transit lines

        with open(Path(__file__.parent.parent / "config.yaml"), 'r') as f:
            self.config: Dict[str, Any] = yaml.safe_load(f)

        self.client : AuthenticatedClient = self.connect()

        self.run(self.config['update_period'])

    def connect(self) -> AuthenticatedClient:
        """Returns a client connected and authenticated to the Geofox API.

        :return: Connected client
        :rtype: AuthenticatedClient
        """
        client = AuthenticatedClient(
            self.config['api']['auth']['base_url'], 
            self.config['api']['auth']['token'],
            )
        return client

    def shutdown(self):
        self.logger.info("Shutting down")

    def run(self, period: int):
        """Runs the main loop: 
        - Query departures,
        - Draw them on a canvas, and
        - Show the canvas on the LED Matrix display.

        :param sleep: Time in seconds to sleep between updates
        :type sleep: int
        """
        self.logger.debug(f"Update period: {period}")

        try:
            while True:  # Main loop
                self.logger.debug("Updating...")
                departures: List[Departure] = self.get_departures()
                canvas: Image = self.draw(departures)
                self.show(canvas)

                time.sleep(period)  # Sleep between updates
        except KeyboardInterrupt:
            self.shutdown()

    def get_departures(self) -> List[Departure]:
        """Get next departures from API.

        :return: List of departures.
        :rtype: List[Departure]
        """
        dl_request = DLRequest(
            version=self.config['api']['version'],
            language=self.config['api']['language'],
            filter_type=DLRequestFilterType.HVV_LISTED,
            time=GTITime("jetzt"),  # Now
            stations=[SDName(station['name'], station['city']) for station in self.config['request']['stations']],
            max_list=self.config['api']['max_list'],
            service_types=[
                DLResponseServiceTypesItem.UBAHN,
                DLResponseServiceTypesItem.XPRESSBUS,
            ],
            use_realtime=True,
        )

    def draw(self, departures: List[Departure]) -> Image:
        """Draws departures on a blank canvas.

        :param departures: List of departures to draw
        :type departures: List[Departure]
        :return: Canvas with drawn departures
        :rtype: Image
        """
        pass

    def show(self, canvas: Image) -> None:
        """Shows the canvas on the LED Matrix display.

        :param canvas: Canvas to show
        :type canvas: Image
        """
        pass


if __name__ == "__main__":
    HvvDisplay()
