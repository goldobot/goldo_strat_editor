import numpy as np

def symetrie(pose):
    if isinstance(pose, np.ndarray):
        if pose.shape[0] == 2:
            return np.array([pose[0], -pose[1]])
    return (pose[0], -pose[1], -pose[2])

def symetrie_point(point):
    return (point[0], -point[1])


class Side:
    Unknown = 0
    Yellow = 1
    Blue = 2


ResourceCenter = {
    "ZoneM1G" : ( 0.275, -0.675),
    "ZoneM1D" : ( 0.275,  0.675),
    "ZoneM2G" : ( 1.050, -0.400),
    "ZoneM2D" : ( 1.050,  0.400),
    "ZoneM3G" : ( 1.750, -0.725),
    "ZoneM3D" : ( 1.750,  0.725),
    "ZoneM4G" : ( 1.600, -1.425),
    "ZoneM4D" : ( 1.600,  1.425),
    "ZoneM5G" : ( 0.675, -1.425),
    "ZoneM5D" : ( 0.675,  1.425),
    }

class YellowPoses:
    # Reperes
    ZoneA_center       = (  0.225, -1.125)
    ZoneDA_center      = (  1.775, -0.275)
    ZoneDL_center      = (  1.125,  1.275)
    ZoneCA_center      = (  1.925, -0.725)
    ZoneCC_center      = (  1.925,  1.275)

    # Poses de depart
    ZoneA_start_pose   = (  0.300, -1.150,   0)
    ZoneDA_start_pose  = (  1.800, -0.300, 180)
    ZoneDL_start_pose  = (  1.100,  1.200, -90)

    # Action1
    Act1_start         = ZoneDA_start_pose
    Act1_preprise      = (  1.300, -0.400,   0)
    Act1_predepose     = (  1.650, -0.200, 180)
    Act1_traj1_start   = Act1_start
    Act1_traj1_wp1     = (  1.500, -0.350, 180)
    Act1_traj1_finish  = Act1_preprise
    Act1_traj2_start   = Act1_preprise
    Act1_traj2_wp1     = (  1.500, -0.300,   0)
    Act1_traj2_finish  = Act1_predepose

    # Action2
    Act2_start         = Act1_predepose
    Act2_preprise      = (  1.500, -0.725, 180)
    Act2_predepose     = (  1.720, -0.725, 180)
    Act2_traj1_start   = Act2_start
    Act2_traj1_wp1     = (  1.500, -0.300, -90)
    Act2_traj1_finish  = Act2_preprise

    # Action3
    Act3_start         = Act2_predepose
    Act3_preprise      = (  1.600, -1.175,  90)
    Act3_depose        = (  1.600, -0.250, 180)
    Act3_predepose     = (  1.500, -0.250, 180)
    Act3_traj1_start   = Act3_start
    Act3_traj1_wp1     = (  1.600, -0.725, -90)
    Act3_traj1_finish  = Act3_preprise

    # Action4
    Act4_start         = Act3_predepose
    Act4_traj1_start   = Act4_start
    Act4_traj1_wp1     = (  1.600, -0.350, -135)
    Act4_traj1_wp2     = (  1.400, -0.400, -135)
    Act4_traj1_wp3     = (  0.800, -0.850, -90)
    Act4_traj1_finish  = (  0.800, -1.200, -90)
    Act4_final         = (  0.450, -1.200, 180)


    # Action1_ZoneDL
    Act1_ZoneDL_start         = ZoneDL_start_pose
    Act1_ZoneDL_preprise      = (  1.300,  0.400,   0)
    Act1_ZoneDL_predepose     = (  1.125,  1.150, -90)
    Act1_ZoneDL_traj1_start   = Act1_ZoneDL_start
    Act1_ZoneDL_traj1_wp1     = (  1.300,  0.800, -90)
    Act1_ZoneDL_traj1_finish  = Act1_ZoneDL_preprise
    Act1_ZoneDL_traj2_start   = Act1_ZoneDL_preprise
    Act1_ZoneDL_traj2_wp1     = (  1.300,  0.800,   0)
    Act1_ZoneDL_traj2_finish  = Act1_ZoneDL_predepose

    # Action2_ZoneDL
    Act2_ZoneDL_start         = Act1_ZoneDL_predepose
    Act2_ZoneDL_preprise      = (  1.500,  0.725, -90)
    Act2_ZoneDL_predepose     = (  1.125,  1.000, -90)

    # Action3_ZoneDL
    Act3_ZoneDL_start         = Act2_ZoneDL_predepose
    Act3_ZoneDL_preprise      = (  1.600,  1.175, -90)
    Act3_ZoneDL_predepose     = (  1.720,  1.250, 180)

    # Action4_ZoneDL
    Act4_ZoneDL_start         = Act3_ZoneDL_predepose
    Act4_ZoneDL_traj1_start   = Act4_ZoneDL_start
    Act4_ZoneDL_traj1_wp1     = (  0.800,  0.400, -135)
    Act4_ZoneDL_traj1_finish  = (  0.800, -1.200, -90)
    Act4_ZoneDL_final         = (  0.450, -1.200, 180)


    # Action1_ZoneA
    Act1_ZoneA_start         = ZoneA_start_pose
    Act1_ZoneA_preprise      = (  0.800, -0.400,   0)
    Act1_ZoneA_predepose     = (  1.650, -0.200, 180)
    Act1_ZoneA_traj1_start   = Act1_ZoneA_start
    Act1_ZoneA_traj1_wp1     = (  0.700, -1.100,   0)
    Act1_ZoneA_traj1_finish  = Act1_ZoneA_preprise
    Act1_ZoneA_traj2_start   = Act1_ZoneA_preprise
    Act1_ZoneA_traj2_wp1     = (  1.500, -0.300,   0)
    Act1_ZoneA_traj2_finish  = Act1_ZoneDL_predepose


class BluePoses:
    # Reperes
    ZoneA_center       = symetrie_point(YellowPoses.ZoneA_center)
    ZoneDA_center      = symetrie_point(YellowPoses.ZoneDA_center)
    ZoneDL_center      = symetrie_point(YellowPoses.ZoneDL_center)
    ZoneCA_center      = symetrie_point(YellowPoses.ZoneCA_center)
    ZoneCC_center      = symetrie_point(YellowPoses.ZoneCC_center)

    ZoneA_start_pose   = symetrie(YellowPoses.ZoneA_start_pose)
    ZoneDA_start_pose  = symetrie(YellowPoses.ZoneDA_start_pose)
    ZoneDL_start_pose  = symetrie(YellowPoses.ZoneDL_start_pose)

    # Action1
    Act1_start         = symetrie(YellowPoses.Act1_start)
    Act1_preprise      = symetrie(YellowPoses.Act1_preprise)
    Act1_predepose     = symetrie(YellowPoses.Act1_predepose)
    Act1_traj1_start   = symetrie(YellowPoses.Act1_traj1_start)
    Act1_traj1_wp1     = symetrie(YellowPoses.Act1_traj1_wp1)
    Act1_traj1_finish  = symetrie(YellowPoses.Act1_traj1_finish)
    Act1_traj2_start   = symetrie(YellowPoses.Act1_traj2_start)
    Act1_traj2_wp1     = symetrie(YellowPoses.Act1_traj2_wp1)
    Act1_traj2_finish  = symetrie(YellowPoses.Act1_traj2_finish)

    # Action2
    Act2_start         = symetrie(YellowPoses.Act2_start)
    Act2_preprise      = symetrie(YellowPoses.Act2_preprise)
    Act2_predepose     = symetrie(YellowPoses.Act2_predepose)
    Act2_traj1_start   = symetrie(YellowPoses.Act2_traj1_start)
    Act2_traj1_wp1     = symetrie(YellowPoses.Act2_traj1_wp1)
    Act2_traj1_finish  = symetrie(YellowPoses.Act2_traj1_finish)

    # Action3
    Act3_start         = symetrie(YellowPoses.Act3_start)
    Act3_preprise      = symetrie(YellowPoses.Act3_preprise)
    Act3_depose        = symetrie(YellowPoses.Act3_depose)
    Act3_predepose     = symetrie(YellowPoses.Act3_predepose)
    Act3_traj1_start   = symetrie(YellowPoses.Act3_traj1_start)
    Act3_traj1_wp1     = symetrie(YellowPoses.Act3_traj1_wp1)
    Act3_traj1_finish  = symetrie(YellowPoses.Act3_traj1_finish)

    # Action4
    Act4_start         = symetrie(YellowPoses.Act4_start)
    Act4_traj1_start   = symetrie(YellowPoses.Act4_traj1_start)
    Act4_traj1_wp1     = symetrie(YellowPoses.Act4_traj1_wp1)
    Act4_traj1_wp2     = symetrie(YellowPoses.Act4_traj1_wp2)
    Act4_traj1_wp3     = symetrie(YellowPoses.Act4_traj1_wp3)
    Act4_traj1_finish  = symetrie(YellowPoses.Act4_traj1_finish)
    Act4_final         = symetrie(YellowPoses.Act4_final)


    # Action1_ZoneDL
    Act1_ZoneDL_start         = symetrie(YellowPoses.Act1_ZoneDL_start)
    Act1_ZoneDL_preprise      = symetrie(YellowPoses.Act1_ZoneDL_preprise)
    Act1_ZoneDL_predepose     = symetrie(YellowPoses.Act1_ZoneDL_predepose)
    Act1_ZoneDL_traj1_start   = symetrie(YellowPoses.Act1_ZoneDL_traj1_start)
    Act1_ZoneDL_traj1_wp1     = symetrie(YellowPoses.Act1_ZoneDL_traj1_wp1)
    Act1_ZoneDL_traj1_finish  = symetrie(YellowPoses.Act1_ZoneDL_traj1_finish)
    Act1_ZoneDL_traj2_start   = symetrie(YellowPoses.Act1_ZoneDL_traj2_start)
    Act1_ZoneDL_traj2_wp1     = symetrie(YellowPoses.Act1_ZoneDL_traj2_wp1)
    Act1_ZoneDL_traj2_finish  = symetrie(YellowPoses.Act1_ZoneDL_traj2_finish)

    # Action2_ZoneDL
    Act2_ZoneDL_start         = symetrie(YellowPoses.Act2_ZoneDL_start)
    Act2_ZoneDL_preprise      = symetrie(YellowPoses.Act2_ZoneDL_preprise)
    Act2_ZoneDL_predepose     = symetrie(YellowPoses.Act2_ZoneDL_predepose)

    # Action3_ZoneDL
    Act3_ZoneDL_start         = symetrie(YellowPoses.Act3_ZoneDL_start)
    Act3_ZoneDL_preprise      = symetrie(YellowPoses.Act3_ZoneDL_preprise)
    Act3_ZoneDL_predepose     = symetrie(YellowPoses.Act3_ZoneDL_predepose)

    # Action4_ZoneDL
    Act4_ZoneDL_start         = symetrie(YellowPoses.Act4_ZoneDL_start)
    Act4_ZoneDL_traj1_start   = symetrie(YellowPoses.Act4_ZoneDL_traj1_start)
    Act4_ZoneDL_traj1_wp1     = symetrie(YellowPoses.Act4_ZoneDL_traj1_wp1)
    Act4_ZoneDL_traj1_finish  = symetrie(YellowPoses.Act4_ZoneDL_traj1_finish)
    Act4_ZoneDL_final         = symetrie(YellowPoses.Act4_ZoneDL_final)


    # Action1_ZoneA
    Act1_ZoneA_start         = symetrie(YellowPoses.Act1_ZoneA_start)
    Act1_ZoneA_preprise      = symetrie(YellowPoses.Act1_ZoneA_preprise)
    Act1_ZoneA_predepose     = symetrie(YellowPoses.Act1_ZoneA_predepose)
    Act1_ZoneA_traj1_start   = symetrie(YellowPoses.Act1_ZoneA_traj1_start)
    Act1_ZoneA_traj1_wp1     = symetrie(YellowPoses.Act1_ZoneA_traj1_wp1)
    Act1_ZoneA_traj1_finish  = symetrie(YellowPoses.Act1_ZoneA_traj1_finish)
    Act1_ZoneA_traj2_start   = symetrie(YellowPoses.Act1_ZoneA_traj2_start)
    Act1_ZoneA_traj2_wp1     = symetrie(YellowPoses.Act1_ZoneA_traj2_wp1)
    Act1_ZoneA_traj2_finish  = symetrie(YellowPoses.Act1_ZoneA_traj2_finish)


@robot.sequence
async def print_start_zone():
    print("Start zone : " + str(robot.start_zone))

@robot.sequence
async def led_off():
    await robot.gpioSet('keyboard_led', False)

@robot.sequence
async def led_on():
    await robot.gpioSet('keyboard_led', True)
