# Sequences de la Coupe de France 2023 - gardees pour test & debug

# import base modules
import asyncio
import numpy as np

import time

# import modules from sequence directory
from . import positions as pos
from . import recalages
from . import actuators_pneuma
from . import actuators_dyna
from . import robot_config as rc

# objects included in the _sequences_globals of RobotMain class, defined in robot_main.py of goldo_main, are available as global variables
# those objects are used to interact with the robot (send commands, read data)

global_long_speed = 0.6
global_turn_speed = 3.0
global_turn_speed_slow = 1.5
global_debug_action_timeout = 0.5
global_debug_timeout = 2.0
global_T0 = 0.0
global_T = 0.0


@robot.sequence
async def prematch():

    global poses

    if robot.side == pos.Side.Yellow:
        poses = pos.YellowPoses
    elif robot.side == pos.Side.Blue:
        poses = pos.BluePoses
    else:
        raise RuntimeError('Side not set')
    
    await lidar.stop()

    # Pneuma
    await actuators_pneuma.reset_valves()
    await actuators_pneuma.start_compressor()

    # Propulsion
    await odrive.clearErrors()
    await propulsion.clearError()
    await propulsion.setAccelerationLimits(1,1,2,2)
    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    
    # Lidar
    robot._adversary_detection_enable = False
    #await lidar.start()

    # Actionneurs
    await asyncio.sleep(1)
    await actuators_dyna.bras_standby()
    await asyncio.sleep(2)
    await actuators_dyna.ascenseur_up()

    # Placement
    await recalages.recalage()

    await asyncio.sleep(1)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(1)
    await actuators_dyna.bras_up()
    await actuators_dyna.soulageur_down()

    # Dummy score
    await robot.setScore(0)
    await robot.gpioSet('keyboard_led', True)

    return True


@robot.sequence
async def action1():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_turn_speed_slow
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    # depose baniere
    await actuators_dyna.ascenseur_down()
    await propulsion.reposition(-0.07, 0.2)
    await robot.setScore(robot.score + 20)
    await asyncio.sleep(global_debug_action_timeout)

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action1_traj1 = [
        (p0_x, p0_y, 0),
        poses.Act1_traj1_start,
        poses.Act1_traj1_wp1,
        poses.Act1_traj1_finish
    ]

    # prise1
    try:
        await propulsion.trajectorySpline(action1_traj1, speed=global_long_speed)
    except:
        await propulsion.pointTo(poses.Act1_traj1_finish, global_turn_speed)
        await propulsion.moveToRetry(poses.Act1_traj1_finish, global_long_speed)
    await actuators_dyna.bras_standby()
    await asyncio.sleep(0.2)
    await propulsion.faceDirection(0, global_turn_speed)
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.12, 0.2)
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)

    # verrouillage planches
    await actuators_dyna.soulageur_up()
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(0.2)
    await actuators_dyna.pump_on()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.soulageur_transport()
    await asyncio.sleep(0.2)
    await propulsion.translation(0.12, 0.2)
    await asyncio.sleep(global_debug_action_timeout)

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action1_traj2 = [
        (p0_x, p0_y, 0),
        poses.Act1_traj2_start,
        poses.Act1_traj2_wp1,
        poses.Act1_traj2_finish
    ]

    # prep construction
    await propulsion.trajectorySpline(action1_traj2, speed=global_long_speed)
    await asyncio.sleep(0.2)
    await propulsion.faceDirection(180, global_turn_speed_slow)
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.10, 0.15)
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)
    
    # construction
    await construction_goldo()
    await robot.setScore(robot.score + 4)
    await robot.setScore(robot.score + 8)
    
    await propulsion.translation(0.10, 0.15)
    await asyncio.sleep(0.2)

    await asyncio.sleep(global_debug_action_timeout)

@robot.sequence
async def action2():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_turn_speed_slow
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action2_traj1 = [
        (p0_x, p0_y, 0),
        poses.Act2_traj1_start,
        poses.Act2_traj1_wp1,
        poses.Act2_traj1_finish
    ]

    # prise2
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(0.2)
    #await propulsion.trajectorySpline(action2_traj1, speed=global_long_speed)
    #await asyncio.sleep(0.2)
    #await propulsion.pointTo(poses.Act2_traj1_wp1, global_turn_speed)
    #await asyncio.sleep(0.2)
    #await propulsion.moveToRetry(poses.Act2_traj1_wp1, global_long_speed)
    #await asyncio.sleep(0.2)
    await propulsion.pointTo(poses.Act2_traj1_finish, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.moveToRetry(poses.Act2_traj1_finish, global_long_speed)
    await asyncio.sleep(0.2)

    # prep construction
    await propulsion.faceDirection(180, global_turn_speed)
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.1, 0.1)
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(0.2)
    await actuators_dyna.pump_on()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.soulageur_transport()
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.20, 0.15)
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(0.2)
    
    # construction
    await construction_goldo()
    await robot.setScore(robot.score + 4)
    await robot.setScore(robot.score + 8)
    
    await propulsion.translation(0.20, 0.15)
    await asyncio.sleep(0.2)
    
    await asyncio.sleep(global_debug_action_timeout)

@robot.sequence
async def action3():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_turn_speed_slow
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action3_traj1 = [
        (p0_x, p0_y, 0),
        poses.Act3_traj1_start,
        poses.Act3_traj1_wp1,
        poses.Act3_traj1_finish
    ]

    # prise3
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(0.2)
    #await propulsion.trajectorySpline(action3_traj1, speed=global_long_speed)
    #await asyncio.sleep(0.2)
    #await propulsion.pointTo(poses.Act3_traj1_wp1, global_turn_speed)
    #await asyncio.sleep(0.2)
    #await propulsion.moveToRetry(poses.Act3_traj1_wp1, global_long_speed)
    #await asyncio.sleep(0.2)
    await propulsion.pointTo(poses.Act3_traj1_finish, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.moveToRetry(poses.Act3_traj1_finish, global_long_speed)
    await asyncio.sleep(0.2)
    
    if robot.side == pos.Side.Yellow:
        await propulsion.faceDirection(90, global_turn_speed)
    elif robot.side == pos.Side.Blue:
        await propulsion.faceDirection(-90, global_turn_speed)

    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await asyncio.sleep(0.5)
    #await propulsion.translation(-0.1, 0.2)
    await propulsion.reposition(-0.115, 0.2)
    await asyncio.sleep(global_debug_action_timeout)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(0.2)
    await actuators_dyna.pump_on()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.soulageur_transport()
    await asyncio.sleep(0.2)
    await asyncio.sleep(0.5)

    # wooble..
    if robot.side == pos.Side.Yellow:
        await propulsion.faceDirection(95, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(85, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(90, global_turn_speed)
        await asyncio.sleep(0.2)
    elif robot.side == pos.Side.Blue:
        await propulsion.faceDirection(-95, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(-85, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(-90, global_turn_speed)
        await asyncio.sleep(0.2)

    # soulage..
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(0.2)

    # deplacement vers la zone de construction3
    await propulsion.moveToRetry(poses.Act3_predepose, global_long_speed)
    await asyncio.sleep(0.2)
    await propulsion.faceDirection(180, global_turn_speed)
    await asyncio.sleep(0.2)

    # construction
    await propulsion.translation(-0.10, 0.15)
    await asyncio.sleep(0.2)
    await construction_goldo()
    await robot.setScore(robot.score + 4)
    await robot.setScore(robot.score + 8)
    
    await propulsion.translation(0.20, 0.15)
    await asyncio.sleep(0.2)
    
    await asyncio.sleep(global_debug_action_timeout)

@robot.sequence
async def action4():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action4_traj1 = [
        (p0_x, p0_y, 0),
        poses.Act4_traj1_start,
        poses.Act4_traj1_wp3,
        poses.Act4_traj1_finish
    ]

    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.5)
    await actuators_dyna.ascenseur_disable()

    # deplacement vers la zone d'attente finale
    # FIXME : DEBUG : no spline yet..
    #try:
    #    await propulsion.trajectorySpline(action4_traj1, speed=global_long_speed)
    #    await asyncio.sleep(0.2)
    #except:
    #    await propulsion.pointTo(poses.Act4_traj1_finish, global_turn_speed)
    #    await propulsion.moveToRetry(poses.Act4_traj1_finish, global_long_speed)
    await propulsion.pointTo(poses.Act4_traj1_finish, global_turn_speed)
    await propulsion.moveToRetry(poses.Act4_traj1_finish, global_long_speed)

    await actuators_dyna.pump_off()
    await actuators_pneuma.reset_valves()
    await actuators_pneuma.purge()

    await propulsion.faceDirection(180, global_turn_speed)
    await asyncio.sleep(0.2)

    print ("******************************************************")
    print ("* Attente finale")
    print ("******************************************************")
    # attente finale
    global_T = time.time()
    while (global_T-global_T0)<92.0:
        await asyncio.sleep(1.0)
        global_T = time.time()

    # deplacement final
    await propulsion.moveToRetry(poses.Act4_final, global_long_speed)
    await robot.setScore(robot.score + 10)
    await asyncio.sleep(0.2)


@robot.sequence
async def action1_ZoneDL():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_turn_speed_slow
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    # depose baniere
    # FIXME : TODO

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action1_traj1 = [
        (p0_x, p0_y, 0),
        poses.Act1_ZoneDL_traj1_start,
        poses.Act1_ZoneDL_traj1_wp1,
        poses.Act1_ZoneDL_traj1_finish
    ]

    # prise1
    try:
        await propulsion.trajectorySpline(action1_traj1, speed=global_long_speed)
    except:
        await propulsion.pointTo(poses.Act1_ZoneDL_traj1_finish, global_turn_speed)
        await propulsion.moveToRetry(poses.Act1_ZoneDL_traj1_finish, global_long_speed)
    await actuators_dyna.bras_standby()
    await asyncio.sleep(0.2)
    await propulsion.faceDirection(0, global_turn_speed)
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.12, 0.2)
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)

    # verrouillage planches
    await actuators_dyna.soulageur_up()
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(0.2)
    await actuators_dyna.pump_on()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.soulageur_transport()
    await asyncio.sleep(0.2)
    await propulsion.translation(0.12, 0.2)
    await asyncio.sleep(global_debug_action_timeout)

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action1_traj2 = [
        (p0_x, p0_y, 0),
        poses.Act1_ZoneDL_traj2_start,
        poses.Act1_ZoneDL_traj2_wp1,
        poses.Act1_ZoneDL_traj2_finish
    ]

    # prep construction
    if robot.side == pos.Side.Yellow:
        await propulsion.faceDirection(90, global_turn_speed)
    elif robot.side == pos.Side.Blue:
        await propulsion.faceDirection(-90, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.trajectorySpline(action1_traj2, speed=global_long_speed)
    await asyncio.sleep(0.2)
    if robot.side == pos.Side.Yellow:
        await propulsion.faceDirection(-90, global_turn_speed)
    elif robot.side == pos.Side.Blue:
        await propulsion.faceDirection(90, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.10, 0.15)
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)
    
    # construction
    await construction_goldo()
    await robot.setScore(robot.score + 4)
    await robot.setScore(robot.score + 8)
    
    await propulsion.translation(0.10, 0.15)
    await asyncio.sleep(0.2)

    await asyncio.sleep(global_debug_action_timeout)


@robot.sequence
async def action2_ZoneDL():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_turn_speed_slow
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    # prise2
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(0.2)
    await propulsion.pointTo(poses.Act2_ZoneDL_preprise, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.moveToRetry(poses.Act2_ZoneDL_preprise, global_long_speed)
    await asyncio.sleep(0.2)
    await propulsion.faceDirection(180, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.12, 0.2)
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(0.2)
    await actuators_dyna.pump_on()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.soulageur_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(0.2)
    await propulsion.translation(0.12, 0.2)
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)

    # deplacement vers la zone de contruction
    await propulsion.pointTo(poses.Act2_ZoneDL_predepose, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.moveToRetry(poses.Act2_ZoneDL_predepose, global_long_speed)
    await asyncio.sleep(0.2)

    # prep construction
    if robot.side == pos.Side.Yellow:
        await propulsion.faceDirection(-90, global_turn_speed)
    elif robot.side == pos.Side.Blue:
        await propulsion.faceDirection(90, global_turn_speed)
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.12, 0.1)
    await asyncio.sleep(0.2)
    
    # construction
    await construction_goldo()
    await robot.setScore(robot.score + 4)
    await robot.setScore(robot.score + 8)
    
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await propulsion.translation(0.12, 0.15)
    await asyncio.sleep(0.2)
    
    await asyncio.sleep(global_debug_action_timeout)


@robot.sequence
async def action3_ZoneDL():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_turn_speed_slow
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    # prise3
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(0.2)
    await propulsion.pointTo(poses.Act3_ZoneDL_preprise, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.moveToRetry(poses.Act3_ZoneDL_preprise, global_long_speed)
    await asyncio.sleep(0.2)
    if robot.side == pos.Side.Yellow:
        await propulsion.faceDirection(-90, global_turn_speed)
    elif robot.side == pos.Side.Blue:
        await propulsion.faceDirection(90, global_turn_speed)
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.12, 0.2)
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(0.2)
    await actuators_dyna.pump_on()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.soulageur_transport()
    await asyncio.sleep(0.2)

    # wooble..
    if robot.side == pos.Side.Yellow:
        await propulsion.faceDirection(-95, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(-85, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(-90, global_turn_speed)
        await asyncio.sleep(0.2)
    elif robot.side == pos.Side.Blue:
        await propulsion.faceDirection(95, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(85, global_turn_speed)
        await asyncio.sleep(0.2)
        await propulsion.faceDirection(90, global_turn_speed)
        await asyncio.sleep(0.2)

    # soulage..
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(0.2)
    #await propulsion.translation(0.12, 0.2)
    await propulsion.translation(0.06, 0.2)
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)

    # deplacement vers la zone de contruction (pas necessaire en fait..)
    #await propulsion.pointTo(poses.Act3_ZoneDL_predepose, global_turn_speed)
    #await asyncio.sleep(0.2)
    #await propulsion.moveToRetry(poses.Act3_ZoneDL_predepose, global_long_speed)
    #await asyncio.sleep(0.2)

    # prep construction
    await propulsion.faceDirection(180, global_turn_speed)
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.18, 0.1)
    await asyncio.sleep(0.2)
    
    # construction
    await construction_goldo()
    await robot.setScore(robot.score + 4)
    await robot.setScore(robot.score + 8)
    
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.2)
    #await propulsion.translation(0.06, 0.15)
    #await asyncio.sleep(0.2)
    
    await asyncio.sleep(global_debug_action_timeout)


@robot.sequence
async def action4_ZoneDL():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    #action4_traj1 = [
    #    (p0_x, p0_y, 0),
    #    poses.Act4_ZoneDL_traj1_start,
    #    poses.Act4_ZoneDL_traj1_wp1,
    #    poses.Act4_ZoneDL_traj1_finish
    #]

    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(0.5)
    await actuators_dyna.ascenseur_disable()

    # deplacement vers la zone d'attente finale
    # FIXME : DEBUG : no spline yet..
    #try:
    #    await propulsion.trajectorySpline(action4_traj1, speed=global_long_speed)
    #    await asyncio.sleep(0.2)
    #except:
    #    await propulsion.pointTo(poses.Act4_ZoneDL_traj1_finish, global_turn_speed)
    #    await propulsion.moveToRetry(poses.Act4_ZoneDL_traj1_finish, global_long_speed)
    await propulsion.pointTo(poses.Act4_ZoneDL_traj1_wp1, global_turn_speed)
    await propulsion.moveToRetry(poses.Act4_ZoneDL_traj1_wp1, global_long_speed)
    await propulsion.pointTo(poses.Act4_ZoneDL_traj1_finish, global_turn_speed)
    await propulsion.moveToRetry(poses.Act4_ZoneDL_traj1_finish, global_long_speed)

    await actuators_dyna.pump_off()
    await actuators_pneuma.reset_valves()
    await actuators_pneuma.purge()

    await propulsion.faceDirection(180, global_turn_speed)
    await asyncio.sleep(0.2)

    print ("******************************************************")
    print ("* Attente finale")
    print ("******************************************************")
    # attente finale
    global_T = time.time()
    while (global_T-global_T0)<92.0:
        await asyncio.sleep(1.0)
        global_T = time.time()

    # deplacement final
    await propulsion.moveToRetry(poses.Act4_ZoneDL_final, global_long_speed)
    await robot.setScore(robot.score + 10)
    await asyncio.sleep(0.2)

@robot.sequence
async def action1_ZoneA():
    global poses
    global global_long_speed
    global global_turn_speed
    global global_turn_speed_slow
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action1_traj1 = [
        (p0_x, p0_y, 0),
        poses.Act1_ZoneA_traj1_start,
        poses.Act1_ZoneA_traj1_wp1,
        poses.Act1_ZoneA_traj1_finish
    ]

    # prise1
    try:
        await propulsion.trajectorySpline(action1_traj1, speed=global_long_speed)
    except:
        await propulsion.pointTo(poses.Act1_ZoneA_traj1_finish, global_turn_speed)
        await propulsion.moveToRetry(poses.Act1_ZoneA_traj1_finish, global_long_speed)
    await actuators_dyna.bras_standby()
    await asyncio.sleep(0.2)
    await propulsion.faceDirection(180, global_turn_speed)
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(0.2)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.12, 0.2)
    await asyncio.sleep(0.2)
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)

    # verrouillage planches
    await actuators_dyna.soulageur_up()
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(0.2)
    await actuators_dyna.pump_on()
    await asyncio.sleep(0.2)
    await actuators_dyna.bras_transport()
    await asyncio.sleep(0.2)
    await actuators_dyna.soulageur_transport()
    await asyncio.sleep(0.2)
    # Pas necessaire!..
    #await propulsion.translation(0.12, 0.2)
    #await asyncio.sleep(global_debug_action_timeout)

    p0_x = propulsion.pose.position.x
    p0_y = propulsion.pose.position.y

    action1_traj2 = [
        (p0_x, p0_y, 0),
        poses.Act1_traj2_start,
        poses.Act1_traj2_wp1,
        poses.Act1_traj2_finish
    ]

    # prep construction
    await propulsion.trajectorySpline(action1_traj2, speed=global_long_speed)
    await asyncio.sleep(0.2)
    await propulsion.faceDirection(180, global_turn_speed_slow)
    await asyncio.sleep(0.2)
    await propulsion.translation(-0.10, 0.15)
    await asyncio.sleep(0.2)
    await asyncio.sleep(global_debug_action_timeout)
    
    # construction
    await construction_goldo()
    await robot.setScore(robot.score + 4)
    await robot.setScore(robot.score + 8)
    
    await propulsion.translation(0.10, 0.15)
    await asyncio.sleep(0.2)

    await asyncio.sleep(global_debug_action_timeout)


@robot.sequence
async def match_start_ZoneDA():
    global poses
    global test_speed_g
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    stop_actions = False

    if not stop_actions:
        print ("======================================================")
        print ("= Action1")
        print ("======================================================")
        try:
            await action1()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action1 FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action1 disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if not stop_actions:
        print ("======================================================")
        print ("= Action2")
        print ("======================================================")
        try:
            await action2()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action2 FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action2 disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    #stop_actions = True

    if not stop_actions:
        print ("======================================================")
        print ("= Action3")
        print ("======================================================")
        try:
            await action3()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action3 FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action3 disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print ("======================================================")
    print ("= Action4")
    print ("======================================================")
    await action4()
    await asyncio.sleep(global_debug_timeout)


@robot.sequence
async def match_start_ZoneDL():
    global poses
    global test_speed_g
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    stop_actions = False

    if not stop_actions:
        print ("======================================================")
        print ("= Action1 ZoneDL")
        print ("======================================================")
        try:
            await action1_ZoneDL()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action1 ZoneDL FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action1 ZoneDL disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    global_T = time.time()
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print ("T Action1 ZoneDL DONE : match_time = {}".format(global_T-global_T0))
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

    #stop_actions = True

    if not stop_actions:
        print ("======================================================")
        print ("= Action2 ZoneDL")
        print ("======================================================")
        try:
            await action2_ZoneDL()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action2 ZoneDL FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action2 ZoneDL disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    global_T = time.time()
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print ("T Action2 ZoneDL DONE : match_time = {}".format(global_T-global_T0))
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

    #stop_actions = True

    if not stop_actions:
        print ("======================================================")
        print ("= Action3 ZoneDL")
        print ("======================================================")
        try:
            await action3_ZoneDL()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action3 ZoneDL FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action3 ZoneDL disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    global_T = time.time()
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print ("T Action3 ZoneDL DONE : match_time = {}".format(global_T-global_T0))
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

    #stop_actions = True

    print ("======================================================")
    print ("= Action4 ZoneDL")
    print ("======================================================")
    await action4_ZoneDL()
    await asyncio.sleep(global_debug_timeout)


@robot.sequence
async def match_start_ZoneA():
    global poses
    global test_speed_g
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    stop_actions = False

    if not stop_actions:
        print ("======================================================")
        print ("= Action1 ZoneA")
        print ("======================================================")
        try:
            await action1_ZoneA()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action1 ZoneA FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action1 ZoneA disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if not stop_actions:
        print ("======================================================")
        print ("= Action2")
        print ("======================================================")
        try:
            await action2()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action2 FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action2 disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    #stop_actions = True

    if not stop_actions:
        print ("======================================================")
        print ("= Action3")
        print ("======================================================")
        try:
            await action3()
        except:
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("! Action3 FAILED")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            await actuators_dyna.ascenseur_soulage()
            await actuators_pneuma.ventouses_ext_lache()
            await actuators_pneuma.ventouses_int_lache()
            stop_actions = True
        await asyncio.sleep(0.5)
    else:
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("! Action3 disabled")
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print ("======================================================")
    print ("= Action4")
    print ("======================================================")
    await action4()
    await asyncio.sleep(global_debug_timeout)


@robot.sequence
async def start_match():
    """
    Sequence called at the start of the match, before trying any action.
    This will typically be used to setup actuators and get out of the starting area.
    """
    global poses
    global test_speed_g
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    global_T0 = time.time()

    await propulsion.setAccelerationLimits(1,1,20,20)
    robot._adversary_detection_enable = True

    global_T = time.time()
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print ("T match_time = {}".format(global_T-global_T0))
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

    if (robot.start_zone == 1) or (robot.start_zone == 6):
        await match_start_ZoneDA()
    elif (robot.start_zone == 2) or (robot.start_zone == 5):
        await match_start_ZoneDL()
    elif (robot.start_zone == 3) or (robot.start_zone == 4):
        await match_start_ZoneA()

    global_T = time.time()
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print ("T match_time = {}".format(global_T-global_T0))
    print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    await lidar.stop()
    #await actuators_pneuma.reset_valves()


@robot.sequence
async def prep_construction_goldo():
    # Pneuma
    await actuators_pneuma.reset_valves()
    await actuators_pneuma.start_compressor()
    await asyncio.sleep(1)

    # Propulsion
    await odrive.clearErrors()
    await propulsion.clearError()
    await propulsion.setAccelerationLimits(1,1,2,2)
    await propulsion.setMotorsEnable(True)
    await propulsion.setEnable(True)
    await asyncio.sleep(1)
    
    # Actionneurs
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(1)
    await actuators_dyna.bras_up()
    await actuators_dyna.soulageur_down()


@robot.sequence
async def test_construction_goldo():
    await preprise_construction_goldo()
    await construction_goldo()

@robot.sequence
async def preprise_construction_goldo():
    global poses
    global test_speed_g
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    short_timeout = 0.2
    long_timeout = 0.5

    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.bras_up()
    await actuators_dyna.soulageur_down()

    print ("Pre-prise")
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(long_timeout)
    await actuators_pneuma.ventouses_ext_attrape()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.bras_standby()
    await asyncio.sleep(short_timeout)
    await propulsion.translation(-0.20, 0.15)
    await asyncio.sleep(short_timeout)
    await asyncio.sleep(long_timeout)

@robot.sequence
async def construction_goldo():
    global poses
    global test_speed_g
    global global_turn_speed
    global global_debug_action_timeout
    global global_debug_timeout
    global global_T0
    global global_T

    short_timeout = 0.1
    long_timeout = 0.3

    print ("Prise planches")
    await actuators_dyna.ascenseur_soulage()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.soulageur_up()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.pump_on()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.bras_prise_hard()
    await asyncio.sleep(long_timeout)
    #await actuators_dyna.bras_up()
    #await asyncio.sleep(short_timeout)
    await asyncio.sleep(long_timeout)
    
    print ("Construction niveau 1")
    await actuators_pneuma.ecarteur_on()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.bras_standby()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_int_lache()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_int_lache()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_int_attrape()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_int_lache()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_int_lache()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.ascenseur_down()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.soulageur_down()
    await asyncio.sleep(short_timeout)
    await asyncio.sleep(long_timeout)

    print ("Translation")
    await propulsion.translation(0.08, 0.15)
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ecarteur_off()
    await asyncio.sleep(short_timeout)
    await asyncio.sleep(long_timeout)

    print ("Construction niveau 2")
    await actuators_dyna.ascenseur_stage2_high()
    await asyncio.sleep(long_timeout)
    await propulsion.translation(-0.10, 0.15)
    await asyncio.sleep(short_timeout)
    await actuators_dyna.bras_prise()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.ascenseur_stage2_depose()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.pump_off()
    await asyncio.sleep(short_timeout)
    await actuators_pneuma.ventouses_ext_lache()
    await asyncio.sleep(short_timeout)
    await asyncio.sleep(long_timeout)

    print ("Fin")
    await propulsion.translation(0.22, 0.15)
    await asyncio.sleep(short_timeout)
    await actuators_dyna.bras_standby()
    await asyncio.sleep(short_timeout)
    await actuators_dyna.ascenseur_standby()
    await asyncio.sleep(short_timeout)

