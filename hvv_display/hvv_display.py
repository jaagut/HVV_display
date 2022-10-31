#! /usr/bin/env python3

import os
import time
import logging
from typing import List, Dict
from PIL import Image
from hvv_display_client.client import AuthenticatedClient


class HvvDisplay:
    """This is the main class glueing the API client to the LED Matrix display."""

    def __init__(self):
        self.logger = logging.getLogger('HvvDisplay')

        self.icons: Dict[str, Image] = {}  # Caches icons of transit lines

        self.client : AuthenticatedClient = self.connect()

        self.run()

    def connect(self) -> AuthenticatedClient:
        """Returns a client connected and authenticated to the Geofox API.

        :return: Connected client
        :rtype: AuthenticatedClient
        """
        base_url: str = os.environ.get("HVV_API_URL").strip()
        token: str = os.environ.get("HVV_API_token").strip()

        client = AuthenticatedClient(base_url, token)
        return client

    def shutdown(self):
        self.logger.info("Shutting down")

    def run(self, period: int = 30):
        """Runs the main loop: 
        - Query departures,
        - Draw them on a canvas, and
        - Show the canvas on the LED Matrix display.

        :param sleep: Time in seconds to sleep between updates , defaults to 15
        :type sleep: int, optional
        """
        self.logger.debug(f"Update period: {period}")

        try:
            while True:  # Main loop
                self.logger.debug("Updating...")
                departures: List = self.get_departures()
                canvas: Image = self.draw(departures)
                self.show(canvas)

                time.sleep(period)  # Sleep between updates
        except KeyboardInterrupt:
            self.shutdown()

    def get_departures(self) -> List:
        """Get next departures from API.

        :return: List of departures.
        :rtype: List
        """
        pass

    def draw(self, departures: List) -> Image:
        """Draws departures on a blank canvas.

        :param departures: List of departures to draw
        :type departures: List
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
