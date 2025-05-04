"""
Class for opponent movement tracking.
Contains variables representing table state
These can be updated by checking the opponent's position
using the lidar. If the opponent passes over plants or pots
we can consider them gone
"""

import asyncio


class FieldMonitor:
    plants_top_left = True
    plants_bottom_left = True
    plants_top_right = True
    plants_bottom_right = True
    plants_top_middle = True
    plants_bottom_middle = True

    pots_top_left = True
    pots_middle_left = True
    pots_bottom_left = True
    pots_top_right = True
    pots_middle_right = True
    pots_bottom_right = True

    solar_panels_middle = True

    _plants_top_left = 0
    _plants_bottom_left = 0
    _plants_top_right = 0
    _plants_bottom_right = 0
    _plants_top_middle = 0
    _plants_bottom_middle = 0

    _solar_panels_middle = 0

    _pots_top_left = 0
    _pots_middle_left = 0
    _pots_bottom_left = 0
    _pots_top_right = 0
    _pots_middle_right = 0
    _pots_bottom_right = 0

    _detection_threshold = 3

    

    pose_plants_top_left = (0.7, -0.5, 0)
    pose_plants_bottom_left = (1.3, -0.5, 0)
    pose_plants_top_middle = (0.5, 0, 0)
    pose_plants_bottom_middle = (1.5, 0, 0)
    pose_plants_top_right = (0.7, 0.5, 0)
    pose_plants_bottom_right = (1.3, 0.5, 0)



    _scan = True

    def __init__(self):
        self._scan = True

    async def run(self):
        while self._scan == True:
            self.scan()
            await asyncio.sleep(0.02)

    async def scan(self):
        self.check_plants_top_left()
        self.check_plants_bottom_left()
        self.check_plants_top_middle()
        self.check_plants_bottom_middle()
        self.check_plants_top_right()
        self.check_plants_bottom_right()
        self.check_solar_panels()

    async def check_solar_panels(self):
        if lidar.objectInRectangle([0.45, -1.5], [0.775, -1.2]):
            self._solar_panels_middle = self._solar_panels_middle + 1
            if self._solar_panels_middle >= self._detection_threshold:
                self.solar_panels_middle = False
        else:
            self._pots_bottom_right = 0

    async def check_plants_top_left(self):
        if lidar.objectInDisk(self.pose_plants_top_left, 0.2):
            self._plants_top_left = self._plants_top_left + 1
            if self._plants_top_left >= self._detection_threshold:
                self.plants_top_left = False
        else:
            self._plants_top_left = 0

    async def check_plants_bottom_left(self):
        if lidar.objectInDisk(self.pose_plants_bottom_left, 0.2):
            self._plants_bottom_left = self._plants_bottom_left + 1
            if self._plants_bottom_left >= self._detection_threshold:
                self.plants_bottom_left = False
        else:
            self._plants_bottom_left = 0

    async def check_plants_top_middle(self):
        if lidar.objectInDisk(self.pose_plants_top_middle, 0.2):
            self._plants_top_middle = self._plants_top_middle + 1
            if self._plants_top_middle >= self._detection_threshold:
                self.plants_top_middle = False
        else:
            self._plants_top_middle = 0

    async def check_plants_bottom_middle(self):
        if lidar.objectInDisk(self.pose_plants_bottom_middle, 0.2):
            self._plants_bottom_middle = self._plants_bottom_middle + 1
            if self._plants_bottom_middle >= self._detection_threshold:
                self.plants_bottom_middle = False
        else:
            self._plants_bottom_middle = 0

    async def check_plants_top_right(self):
        if lidar.objectInDisk(self.pose_plants_top_right, 0.2):
            self._plants_top_right = self._plants_top_right + 1
            if self._plants_top_right >= self._detection_threshold:
                self.plants_top_right = False
        else:
            self._plants_top_right = 0

    async def check_plants_bottom_right(self):
        if lidar.objectInDisk(self.pose_plants_bottom_right, 0.2):
            self._plants_bottom_right = self._plants_bottom_right + 1
            if self._plants_bottom_right >= self._detection_threshold:
                self.plants_bottom_right = False
        else:
            self._plants_bottom_right = 0

    async def check_pots_top_left(self):
        if lidar.objectInRectangle([0.45, -1.5], [0.775, -1.2]):
            self._pots_top_left = self.pots_top_left + 1
            if self._pots_top_left >= self._detection_threshold:
                self.pots_top_left = False
        else:
            self._pots_top_left = 0

    async def check_pots_middle_left(self):
        if lidar.objectInRectangle([0.45, -1.5], [0.775, -1.2]):
            self._pots_middle_left = self.pots_middle_left + 1
            if self._pots_middle_left >= self._detection_threshold:
                self.pots_middle_left = False
        else:
            self._pots_middle_left = 0
    async def check_pots_bottom_left(self):
        if lidar.objectInRectangle([0.45, -1.5], [0.775, -1.2]):
            self._pots_bottom_left = self.pots_bottom_left + 1
            if self._pots_bottom_left >= self._detection_threshold:
                self.pots_bottom_left = False
        else:
            self._pots_bottom_left = 0

    async def check_pots_top_left(self):
        if lidar.objectInRectangle([0.45, -1.5], [0.775, -1.2]):
            self._pots_top_left = self.pots_top_left + 1
            if self._pots_top_left >= self._detection_threshold:
                self.pots_top_left = False
        else:
            self._pots_top_left = 0

    async def check_pots_middle_right(self):
        if lidar.objectInRectangle([0.45, -1.5], [0.775, -1.2]):
            self._pots_middle_right = self.pots_middle_right + 1
            if self._pots_middle_right >= self._detection_threshold:
                self.pots_middle_right = False
        else:
            self._pots_middle_right = 0

    async def check_pots_bottom_right(self):
        if lidar.objectInRectangle([0.45, -1.5], [0.775, -1.2]):
            self._pots_bottom_right = self.pots_bottom_right + 1
            if self._pots_bottom_right >= self._detection_threshold:
                self.pots_bottom_right = False
        else:
            self._pots_bottom_right = 0