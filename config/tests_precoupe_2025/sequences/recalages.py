import asyncio
from . import positions as pos
from . import robot_config as rc

@robot.sequence
async def recalage():
    if robot.start_zone == 1:
        await recalage_ZoneDA_J()
    elif robot.start_zone == 2:
        await recalage_ZoneDL_B()
    elif robot.start_zone == 3:
        await recalage_ZoneA_J()
    elif robot.start_zone == 4:
        await recalage_ZoneA_B()
    elif robot.start_zone == 5:
        await recalage_ZoneDL_J()
    elif robot.start_zone == 6:
        await recalage_ZoneDA_B()
    else:
        print("Recalage : Wrong start zone")

async def recalage_ZoneDA_J():
    poses = pos.YellowPoses
    homing_speed = 0.15
    turning_speed = 1.00

    print("****************************************************************")
    print("Recalage 'ZoneDA_J' (cote JAUNE) ")
    print("****************************************************************")

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # Robot is to be put approximately at its "pre-homing" position
    print("Le robot doit etre en position de 'pre-recalage' oriente selon l'axe Y")
    await propulsion.setPose([poses.ZoneDA_J_start_pose[0],
                              poses.ZoneDA_J_start_pose[1]], 90)

    print("Recalage axe Y")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([propulsion.pose.position.x , -1.5+rc.robot_back_length], 90)
    await asyncio.sleep(0.5)

    print("Orientation axe X")
    await propulsion.moveTo(poses.ZoneDA_J_start_pose, homing_speed)
    await propulsion.faceDirection(180, turning_speed)
    await asyncio.sleep(0.5)

    print("Recalage axe X")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([2.0 - rc.robot_back_length , propulsion.pose.position.y], 180)
    await asyncio.sleep(0.5)

    print("go depart")
    await propulsion.moveTo(poses.ZoneDA_J_start_pose, homing_speed)
    #await propulsion.faceDirection(180, turning_speed)
    await asyncio.sleep(0.5)


async def recalage_ZoneDL_B():
    poses = pos.BluePoses
    homing_speed = 0.15
    turning_speed = 1.00

    print("****************************************************************")
    print("Recalage 'ZoneDL_B' (cote BLEU) ")
    print("****************************************************************")

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # Robot is to be put approximately at its "pre-homing" position
    print("Le robot doit etre en position de 'pre-recalage' oriente selon l'axe X")
    await propulsion.setPose([poses.ZoneDL_B_start_pose[0],
                              poses.ZoneDL_B_start_pose[1]], 180)

    print("Recalage axe X")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([2.0 - rc.robot_back_length , propulsion.pose.position.y], 180)
    await asyncio.sleep(0.5)

    print("Orientation axe Y")
    await propulsion.moveTo(poses.ZoneDL_B_start_pose, homing_speed)
    await propulsion.faceDirection(90, turning_speed)
    await asyncio.sleep(0.5)

    print("Recalage axe Y")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([propulsion.pose.position.x , -1.5+rc.robot_back_length], 90)
    await asyncio.sleep(0.5)

    print("go depart")
    await propulsion.moveTo(poses.ZoneDL_B_start_pose, homing_speed)
    #await propulsion.faceDirection(90, turning_speed)
    await asyncio.sleep(0.5)


async def recalage_ZoneA_J():
    poses = pos.YellowPoses
    homing_speed = 0.15
    turning_speed = 1.00

    print("****************************************************************")
    print("Recalage 'ZoneA_J' (cote JAUNE) ")
    print("****************************************************************")

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # Robot is to be put approximately at its "pre-homing" position
    print("Le robot doit etre en position de 'pre-recalage' oriente selon l'axe Y")
    await propulsion.setPose([poses.ZoneA_J_start_pose[0],
                              poses.ZoneA_J_start_pose[1]], 90)

    print("Recalage axe Y")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([propulsion.pose.position.x , -1.5+rc.robot_back_length], 90)
    await asyncio.sleep(0.5)

    print("Orientation axe X")
    await propulsion.moveTo(poses.ZoneA_J_start_pose, homing_speed)
    await propulsion.faceDirection(0, turning_speed)
    await asyncio.sleep(0.5)

    print("Recalage axe X")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([rc.robot_back_length , propulsion.pose.position.y], 0)
    await asyncio.sleep(0.5)

    print("go depart")
    await propulsion.moveTo(poses.ZoneA_J_start_pose, homing_speed)
    #await propulsion.faceDirection(0, turning_speed)
    await asyncio.sleep(0.5)


async def recalage_ZoneA_B():
    poses = pos.BluePoses
    homing_speed = 0.15
    turning_speed = 1.00

    print("****************************************************************")
    print("Recalage 'ZoneA_B' (cote BLEU) ")
    print("****************************************************************")

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # Robot is to be put approximately at its "pre-homing" position
    print("Le robot doit etre en position de 'pre-recalage' oriente selon l'axe Y")
    await propulsion.setPose([poses.ZoneA_B_start_pose[0],
                              poses.ZoneA_B_start_pose[1]], -90)

    print("Recalage axe Y")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([propulsion.pose.position.x , 1.5-rc.robot_back_length], -90)
    await asyncio.sleep(0.5)

    print("Orientation axe X")
    await propulsion.moveTo(poses.ZoneA_B_start_pose, homing_speed)
    await propulsion.faceDirection(0, turning_speed)
    await asyncio.sleep(0.5)

    print("Recalage axe X")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([rc.robot_back_length , propulsion.pose.position.y], 0)
    await asyncio.sleep(0.5)

    print("go depart")
    await propulsion.moveTo(poses.ZoneA_B_start_pose, homing_speed)
    #await propulsion.faceDirection(0, turning_speed)
    await asyncio.sleep(0.5)


async def recalage_ZoneDL_J():
    poses = pos.YellowPoses
    homing_speed = 0.15
    turning_speed = 1.00

    print("****************************************************************")
    print("Recalage 'ZoneDL_J' (cote JAUNE) ")
    print("****************************************************************")

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # Robot is to be put approximately at its "pre-homing" position
    print("Le robot doit etre en position de 'pre-recalage' oriente selon l'axe X")
    await propulsion.setPose([poses.ZoneDL_J_start_pose[0],
                              poses.ZoneDL_J_start_pose[1]], 180)

    print("Recalage axe X")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([2.0 - rc.robot_back_length , propulsion.pose.position.y], 180)
    await asyncio.sleep(0.5)

    print("Orientation axe Y")
    await propulsion.moveTo(poses.ZoneDL_J_start_pose, homing_speed)
    await propulsion.faceDirection(-90, turning_speed)
    await asyncio.sleep(0.5)

    print("Recalage axe Y")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([propulsion.pose.position.x , 1.5-rc.robot_back_length], -90)
    await asyncio.sleep(0.5)

    print("go depart")
    await propulsion.moveTo(poses.ZoneDL_J_start_pose, homing_speed)
    #await propulsion.faceDirection(-90, turning_speed)
    await asyncio.sleep(0.5)


async def recalage_ZoneDA_B():
    poses = pos.BluePoses
    homing_speed = 0.15
    turning_speed = 1.00

    print("****************************************************************")
    print("Recalage 'ZoneDA_B' (cote BLEU) ")
    print("****************************************************************")

    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await propulsion.setAccelerationLimits(0.3,0.3,3,3)

    # Robot is to be put approximately at its "pre-homing" position
    print("Le robot doit etre en position de 'pre-recalage' oriente selon l'axe Y")
    await propulsion.setPose([poses.ZoneDA_B_start_pose[0],
                              poses.ZoneDA_B_start_pose[1]], -90)

    print("Recalage axe Y")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([propulsion.pose.position.x , 1.5-rc.robot_back_length], -90)
    await asyncio.sleep(0.5)

    print("Orientation axe X")
    await propulsion.moveTo(poses.ZoneDA_B_start_pose, homing_speed)
    await propulsion.faceDirection(180, turning_speed)
    await asyncio.sleep(0.5)

    print("Recalage axe X")
    await propulsion.reposition(-1.0, homing_speed)
    await propulsion.setPose([2.0 - rc.robot_back_length , propulsion.pose.position.y], 180)
    await asyncio.sleep(0.5)

    print("go depart")
    await propulsion.moveTo(poses.ZoneDA_B_start_pose, homing_speed)
    #await propulsion.faceDirection(180, turning_speed)
    await asyncio.sleep(0.5)


