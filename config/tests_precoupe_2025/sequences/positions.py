import numpy as np
from . import robot_config as rc

def symetrie(pose):
    if isinstance(pose, np.ndarray):
        if pose.shape[0] == 2:
            return np.array([pose[0], -pose[1]])
    return (pose[0], -pose[1], -pose[2])


class Side:
    Unknown = 0
    Yellow = 1
    Blue = 2


class YellowPoses:
    ZoneA_J_start_pose   = (  0.30, -1.15,   0)
    ZoneDA_J_start_pose  = (  1.80, -0.30, 180)
    ZoneDL_J_start_pose  = (  1.10,  1.20, -90)


class BluePoses:
    ZoneA_B_start_pose   = (  0.30,  1.15,   0)
    ZoneDA_B_start_pose  = (  1.80,  0.30, 180)
    ZoneDL_B_start_pose  = (  1.10, -1.20,  90)


@robot.sequence
async def print_start_zone():
    print("Start zone : " + str(robot.start_zone))

@robot.sequence
async def led_off():
    await robot.gpioSet('keyboard_led', False)

@robot.sequence
async def led_on():
    await robot.gpioSet('keyboard_led', True)
