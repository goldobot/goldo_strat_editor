import asyncio
from . import positions as pos
from . import robot_config as rc

@robot.sequence
async def recalage():
    if robot.start_zone == 1:
        await recalage_ZoneDA_J()
    elif robot.start_zone == 2:
        await recalage_ZoneDL_J()
    elif robot.start_zone == 3:
        await recalage_ZoneA_J()
    elif robot.start_zone == 4:
        await recalage_ZoneDA_B()
    elif robot.start_zone == 5:
        await recalage_ZoneDL_B()
    elif robot.start_zone == 6:
        await recalage_ZoneA_B()
    else:
        print("Recalage : Wrong start zone")

async def recalage_ZoneDA_J():
    poses = pos.YellowPoses

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # Robot is to put approximately at its start pose
    await propulsion.setPose([poses.ZoneDA_J_start_pose[0],
                              poses.ZoneDA_J_start_pose[1]], 90)

    print("Recalage axe Y")
    await propulsion.reposition(-1.0, 0.2)
    await propulsion.setPose([rc.robot_back_length , propulsion.pose.position.y], 90)
    await asyncio.sleep(0.5)

    print("Orientation axe X")    
    await propulsion.moveTo(poses.ZoneDA_J_start_pose, 0.2)
    await propulsion.pointTo(0, [poses.ZoneDA_J_start_pose[1]], 1)
    await asyncio.sleep(0.5)

    print("Recalage axe X")
    await propulsion.reposition(-1.0, 0.2)
    await propulsion.setPose([propulsion.pose.position.x , 1.0 - rc.robot_back_length], 180)
    await asyncio.sleep(0.5)

    print("go depart")
    await propulsion.moveTo(poses.ZoneDA_J_start_pose, 0.2)
    #await propulsion.faceDirection(180, 1)
    await asyncio.sleep(0.5)


async def recalage_ZoneDL_J():
    poses = pos.YellowPoses

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # FIXME : TODO


async def recalage_ZoneA_J():
    poses = pos.YellowPoses

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # FIXME : TODO


async def recalage_ZoneDA_B():
    poses = pos.BluePoses

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # FIXME : TODO


async def recalage_ZoneDL_B():
    poses = pos.BluePoses

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # FIXME : TODO


async def recalage_ZoneA_B():
    poses = pos.BluePoses

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # FIXME : TODO


