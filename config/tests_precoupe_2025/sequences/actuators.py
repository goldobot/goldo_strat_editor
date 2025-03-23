import asyncio


class GoldoLift:
    Unknown = 0
    Left = 1
    Right = 2


async def goldo_lift_move(side,pos):
    lift_factor = 1.090
    if (side==GoldoLift.Left):
        await servos.liftsRaw(int(pos*lift_factor), 80, 0, 0)
    if (side==GoldoLift.Right):
        await servos.liftsRaw(0, 0, int(pos*lift_factor), 80)


async def goldo_lifts_move(pos, speed = 80):
    lift_factor = 1.090
    await servos.liftsRaw(int(pos*lift_factor), speed, int(pos*lift_factor), speed)


@robot.sequence
async def goldo_lifts_test_initialize():
    # initialisation ascenseurs    
    await servos.liftDoHoming(0)
    await servos.liftDoHoming(1)
    await asyncio.sleep(3)
    await servos.liftsRaw(65, 60, 65, 60)
    await asyncio.sleep(3)


@robot.sequence
async def goldo_lifts_test_pos_0():
    await goldo_lifts_move(0)

@robot.sequence
async def goldo_lifts_test_pos_65():
    await goldo_lifts_move(65)

@robot.sequence
async def goldo_lifts_test_pos_200():
    await goldo_lifts_move(200)

@robot.sequence
async def goldo_lifts_test_pos_400():
    await goldo_lifts_move(400)

@robot.sequence
async def goldo_lifts_test_pos_600():
    await goldo_lifts_move(600)

@robot.sequence
async def goldo_lifts_test_pos_800():
    await goldo_lifts_move(800)

@robot.sequence
async def goldo_lifts_test_pos_1000():
    await goldo_lifts_move(1000)


#@robot.sequence
#async def goldo_lift_l_test_pos_200():
#    await goldo_lift_move(GoldoLift.Left,200)
#
#@robot.sequence
#async def goldo_lift_l_test_pos_400():
#    await goldo_lift_move(GoldoLift.Left,400)
#
#@robot.sequence
#async def goldo_lift_l_test_pos_600():
#    await goldo_lift_move(GoldoLift.Left,600)
#
#@robot.sequence
#async def goldo_lift_l_test_pos_800():
#    await goldo_lift_move(GoldoLift.Left,800)
#
#@robot.sequence
#async def goldo_lift_l_test_pos_1000():
#    await goldo_lift_move(GoldoLift.Left,1000)
#
#
#@robot.sequence
#async def goldo_lift_r_test_pos_200():
#    await goldo_lift_move(GoldoLift.Right,200)
#
#@robot.sequence
#async def goldo_lift_r_test_pos_400():
#    await goldo_lift_move(GoldoLift.Right,400)
#
#@robot.sequence
#async def goldo_lift_r_test_pos_600():
#    await goldo_lift_move(GoldoLift.Right,600)
#
#@robot.sequence
#async def goldo_lift_r_test_pos_800():
#    await goldo_lift_move(GoldoLift.Right,800)
#
#@robot.sequence
#async def goldo_lift_r_test_pos_1000():
#    await goldo_lift_move(GoldoLift.Right,1000)
#

async def pump_on(left, right):
    if left:
        await robot.gpioSet('pompe_g', True)
        await robot.gpioSet('pompe_g', True)
    if right:
        await robot.gpioSet('pompe_d', True)
        await robot.gpioSet('pompe_d', True)


async def pump_off(left, right):
    if left:
        await robot.gpioSet('pompe_g', False)
        await robot.gpioSet('pompe_g', False)
    if right:
        await robot.gpioSet('pompe_d', False)
        await robot.gpioSet('pompe_d', False)

@robot.sequence
async def pumps_on():
    await pump_on(True, True)

@robot.sequence
async def pumps_off():
    await pump_off(True, True)

@robot.sequence
async def left_pump_on():
    await pump_on(True, False)

@robot.sequence
async def left_pump_off():
    await pump_off(True, False)

@robot.sequence
async def right_pump_on():
    await pump_on(False, True)

@robot.sequence
async def right_pump_off():
    await pump_off(False, True)


epaules_devant = {
    'epaule_g': 2052,
    'epaule_d': 2035
}

epaules_rentrees = {
    'epaule_g': 2952,
    'epaule_d': 1131
}

epaules_ouvertes = {
    'epaule_g': 1609,
    'epaule_d': 2277
}

epaules_prise = {
    'epaule_g': 2240,
    'epaule_d': 1845
}

coudes_leves = {
    'coude_g': 827,
    'coude_d': 204
}

coudes_baissees = {
    'coude_g': 490,
    'coude_d': 530
}

# Cote vert
#bras_gauche_prise_marron = {
#    'epaule_g': 1628,
#    'coude_g': 500
#}
bras_gauche_prise_marron = {
    'epaule_g': 1648,
    'coude_g': 500
}

bras_gauche_depose_marron = {
    'epaule_g': 2555,
    'coude_g': 500
}

#bras_droit_prise_jaune = {
#    'epaule_d': 3124,
#    'coude_d': 515
#}
bras_droit_prise_jaune = {
    'epaule_d': 3124,
    'coude_d': 530
}

#bras_droit_depose_jaune = {
#    'epaule_d': 1499,
#    'coude_d': 515
#}
bras_droit_depose_jaune = {
    'epaule_d': 1400,
    'coude_d': 515
}

#bras_droit_prise_rose = {
#    'epaule_d': 2411,
#    'coude_d': 515
#}
bras_droit_prise_rose = {
    'epaule_d': 2411,
    'coude_d': 530
}

bras_droit_depose_rose = {
    'epaule_d': 1450,
    'coude_d': 510
}


# Cote bleu
#bras_droit_prise_marron = {
#    'epaule_d': 2411,
#    'coude_d': 520
#}
bras_droit_prise_marron = {
    'epaule_d': 2390,
    'coude_d': 520
}

bras_droit_depose_marron = {
    'epaule_d': 1450,
    'coude_d': 510
}

bras_gauche_prise_jaune = {
    'epaule_g': 937,
    'coude_g': 490
}

#bras_gauche_depose_jaune = {
#    'epaule_g': 2630,
#    'coude_g': 500
#}
bras_gauche_depose_jaune = {
    'epaule_g': 2730,
    'coude_g': 500
}

#bras_gauche_prise_rose = {
#    'epaule_g': 1628,
#    'coude_g': 500
#}
bras_gauche_prise_rose = {
    'epaule_g': 1628,
    'coude_g': 500
}

#bras_gauche_depose_rose = {
#    'epaule_g': 2555,
#    'coude_g': 500
#}
bras_gauche_depose_rose = {
    'epaule_g': 2600,
    'coude_g': 500
}

bras_d_prep_minicake = {
    'epaule_d': 1500,
    'coude_d': 500
}

bras_d_take_minicake = {
    'epaule_d': 1500,
    'coude_d': 500
}

bras_d_rotate_minicake = {
    'epaule_d': 2200,
    'coude_d': 500
}

bras_d_end_minicake = {
    'epaule_d': 2200,
    'coude_d': 204
}

bras_g_prep_minicake = {
    'epaule_g': 2700,
    'coude_g': 500
}

bras_g_take_minicake = {
    'epaule_g': 2700,
    'coude_g': 500
}

bras_g_rotate_minicake = {
    'epaule_g': 1900,
    'coude_g': 500
}

bras_g_end_minicake = {
    'epaule_g': 1900,
    'coude_g': 827
}

bras_prep_minicake = {
    'epaule_d': 1400,
    'coude_d': 500,
    'epaule_g': 2700,
    'coude_g': 500
}


@robot.sequence
async def arms_initialize():

    # Activation dynamixels
    await servos.setMaxTorque(['epaule_g', 'epaule_d'], 0.30)
    await servos.setMaxTorque(['coude_g', 'coude_d'], 0.20)
    
    await servos.setEnable(['epaule_g', 'epaule_d'], True)
    await servos.setEnable(['coude_g', 'coude_d'], True)
    
    # Init bras
    await servos.moveMultiple(epaules_devant, speed=0.7)
    await asyncio.sleep(0.2)
    await servos.moveMultiple(coudes_leves, speed=0.7)
    await asyncio.sleep(0.2)
    
    # initialisation ascenseurs    
    await servos.liftDoHoming(0)
    await servos.liftDoHoming(1)
    await asyncio.sleep(3)
    
    await servos.liftsRaw(65, 60, 65, 60)
    await asyncio.sleep(1)
    await servos.moveMultiple(epaules_rentrees, speed=0.7)
    await servos.setMaxTorque(['epaule_g', 'epaule_d'], 1)
    await servos.setMaxTorque(['coude_g', 'coude_d'], 1)


async def minicake_prepare_left():
    await goldo_lift_move(GoldoLift.Left,600)
    await asyncio.sleep(0.4)
    await servos.moveMultiple(bras_g_prep_minicake, speed=1)
    await asyncio.sleep(0.4)

async def minicake_prepare_right():
    await goldo_lift_move(GoldoLift.Right,1000)
    await asyncio.sleep(0.4)
    await servos.moveMultiple(bras_d_prep_minicake, speed=1)
    await asyncio.sleep(0.4)

@robot.sequence
async def minicake_prepare():
    await servos.liftsRaw(600, 80, 1000, 60)
    await asyncio.sleep(0.5)
    await servos.moveMultiple(bras_prep_minicake, speed=1)
    await asyncio.sleep(0.2)

@robot.sequence
async def minicake_make_left():
    await left_pump_on()
    await asyncio.sleep(0.1)
    await goldo_lift_move(GoldoLift.Left,380)
    await asyncio.sleep(0.3)
    await servos.moveMultiple(bras_g_take_minicake, speed=1)
    await asyncio.sleep(0.1)
    await goldo_lift_move(GoldoLift.Left,420)
    await asyncio.sleep(0.2)
    await servos.moveMultiple(bras_g_rotate_minicake, speed=1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Left,140)
    await asyncio.sleep(0.2)
    await left_pump_off()
    await asyncio.sleep(0.1)
    await goldo_lift_move(GoldoLift.Left,600)
    await asyncio.sleep(0.3)
    await servos.moveMultiple(bras_g_end_minicake, speed=1)
    await asyncio.sleep(0.1)

@robot.sequence
async def minicake_make_right():
    await right_pump_on()
    await asyncio.sleep(0.1)
    await goldo_lift_move(GoldoLift.Right,140)
    await asyncio.sleep(0.4)
    await servos.moveMultiple(bras_d_take_minicake, speed=1)
    await asyncio.sleep(0.1)
    await goldo_lift_move(GoldoLift.Right,220)
    await asyncio.sleep(0.2)
    await servos.moveMultiple(bras_d_rotate_minicake, speed=1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Right,140)
    await asyncio.sleep(0.2)
    await right_pump_off()
    await asyncio.sleep(0.1)
    await goldo_lift_move(GoldoLift.Right,600)
    await asyncio.sleep(0.3)
    await servos.moveMultiple(bras_d_end_minicake, speed=1)
    await asyncio.sleep(0.1)


@robot.sequence
async def arms_open():
    await servos.moveMultiple(epaules_ouvertes, speed=1)
    await asyncio.sleep(0.1)
    await servos.moveMultiple(coudes_leves, speed=1)

@robot.sequence
async def arms_prep_take():
    await servos.moveMultiple(epaules_prise, speed=1)
    await asyncio.sleep(0.1)
    await servos.moveMultiple(coudes_leves, speed=1)

@robot.sequence
async def arms_take():
    await servos.moveMultiple(epaules_prise, speed=1)
    await asyncio.sleep(0.1)
    await servos.moveMultiple(coudes_baissees, speed=1)

@robot.sequence
async def arms_centering():
    await goldo_lifts_move(130,60)
    await servos.moveMultiple(epaules_prise, speed=1)
    await asyncio.sleep(0.1)
    await servos.moveMultiple(coudes_leves, speed=1)

@robot.sequence
async def arms_collect():
    await servos.moveMultiple(epaules_ouvertes, speed=1)
    await asyncio.sleep(0.1)
    await servos.moveMultiple(coudes_leves, speed=1)
    await asyncio.sleep(0.1)
    await goldo_lifts_move(130,60)

@robot.sequence
async def arms_close():
    await servos.moveMultiple(epaules_rentrees, speed=1)
    await asyncio.sleep(0.1)
    await servos.moveMultiple(coudes_leves, speed=1)

# Constructions vertes
@robot.sequence
async def construction_gateau_haut_vert():
    ####await goldo_lifts_move(500, 80)
    await goldo_lifts_move(520, 80)
    await pump_on(True, True)
    # bras au dessus du jaune et du marron
    taskarms = asyncio.create_task(servos.moveMultiple(bras_droit_prise_jaune, 1))
    await servos.moveMultiple(bras_gauche_prise_marron, 1)
    await taskarms
    await asyncio.sleep(0.2)
    # descente pour prise
    await goldo_lifts_move(400, 80)
    await asyncio.sleep(0.2)
    # depose marron
    ####tasklifts = asyncio.create_task(goldo_lifts_move(450, 80))
    tasklifts = asyncio.create_task(goldo_lifts_move(540, 80))
    await servos.moveMultiple(bras_gauche_depose_marron, 1)
    await asyncio.sleep(0.2)
    await tasklifts
    await goldo_lift_move(GoldoLift.Left, 140)
    await asyncio.sleep(0.2)
    await left_pump_off()
    await asyncio.sleep(0.2)

    # retrait bras gauche
    ####await goldo_lift_move(GoldoLift.Left, 500)
    await goldo_lift_move(GoldoLift.Left, 520)
    taskarms = asyncio.create_task(servos.moveMultiple(bras_gauche_prise_marron, 1))

    # depose jaune
    ####await goldo_lift_move(GoldoLift.Right, 800)
    await goldo_lift_move(GoldoLift.Right, 860)
    await asyncio.sleep(0.2)
    await servos.moveMultiple(bras_droit_depose_jaune, 1)
    await asyncio.sleep(0.5)
    await goldo_lift_move(GoldoLift.Right, 350)
    await asyncio.sleep(0.2)
    await right_pump_off()
    await asyncio.sleep(0.2)

    # prise rose
    ####
    await goldo_lift_move(GoldoLift.Right, 620)
    await asyncio.sleep(0.3)
    await servos.moveMultiple(bras_droit_prise_rose, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Right, 400)
    await right_pump_on()
    await asyncio.sleep(0.2)

    # depose rose
    await goldo_lift_move(GoldoLift.Right, 570)
    await asyncio.sleep(0.3)
    await servos.moveMultiple(bras_droit_depose_rose, 1)
    await asyncio.sleep(0.3)
    await right_pump_off()
    await taskarms
    await asyncio.sleep(0.2)

    # ecartement bras
    taskarms = asyncio.create_task(servos.moveMultiple(coudes_leves, 1))
    await servos.moveMultiple(epaules_ouvertes, 1)
    await taskarms

@robot.sequence
async def construction_gateau_milieu_vert():
    ####await goldo_lifts_move(300, 80)
    await goldo_lifts_move(320, 80)
    await pump_on(True, True)
    # bras au dessus du jaune et du marron
    taskarms = asyncio.create_task(servos.moveMultiple(bras_droit_prise_jaune, 1))
    await servos.moveMultiple(bras_gauche_prise_marron, 1)
    await taskarms
    await asyncio.sleep(0.2)
    # descente pour prise
    await goldo_lifts_move(200, 80)
    await asyncio.sleep(0.2)
    # depose marron
    ####tasklifts = asyncio.create_task(goldo_lifts_move(300, 80))
    tasklifts = asyncio.create_task(goldo_lifts_move(400, 80))
    await servos.moveMultiple(bras_gauche_depose_marron, 1)
    await asyncio.sleep(0.2)
    await tasklifts
    await goldo_lift_move(GoldoLift.Left, 150)
    await asyncio.sleep(0.3)
    await left_pump_off()
    await asyncio.sleep(0.2)

    # retrait bras gauche
    ####await goldo_lift_move(GoldoLift.Left, 300)
    await goldo_lift_move(GoldoLift.Left, 320)
    taskarms = asyncio.create_task(servos.moveMultiple(bras_gauche_prise_marron, 1))

    # depose jaune
    ####await goldo_lift_move(GoldoLift.Right, 600)
    await goldo_lift_move(GoldoLift.Right, 620)
    await servos.moveMultiple(bras_droit_depose_jaune, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Right, 400)
    await asyncio.sleep(0.3)
    await right_pump_off()
    await asyncio.sleep(0.2)

    # prise rose
    ####
    await goldo_lift_move(GoldoLift.Right, 420)
    await servos.moveMultiple(bras_droit_prise_rose, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Right, 200)
    await right_pump_on()
    await asyncio.sleep(0.2)

    # depose rose
    await goldo_lift_move(GoldoLift.Right, 600)
    await asyncio.sleep(0.2)
    await servos.moveMultiple(bras_droit_depose_rose, 1)
    await asyncio.sleep(0.3)
    await right_pump_off()
    await taskarms
    await asyncio.sleep(0.2)

    # ecartement bras
    taskarms = asyncio.create_task(servos.moveMultiple(coudes_leves, 1))
    await servos.moveMultiple(epaules_ouvertes, 1)
    await taskarms

@robot.sequence
async def construction_gateau_bas_vert():
    ####await goldo_lifts_move(100, 80)
    await goldo_lifts_move(120, 80)
    await pump_on(True, True)
    # bras au dessus du jaune et du marron
    taskarms = asyncio.create_task(servos.moveMultiple(bras_droit_prise_jaune, 1))
    await servos.moveMultiple(bras_gauche_prise_marron, 1)
    await taskarms
    await asyncio.sleep(0.2)
    # descente pour prise
    await goldo_lifts_move(40, 80)
    await asyncio.sleep(0.2)
    # depose marron
    ####tasklifts = asyncio.create_task(goldo_lifts_move(100, 80))
    tasklifts = asyncio.create_task(goldo_lifts_move(140, 80))
    await servos.moveMultiple(bras_gauche_depose_marron, 1)
    await asyncio.sleep(0.2)
    await tasklifts
    await goldo_lift_move(GoldoLift.Left, 100)
    await asyncio.sleep(0.2)
    await left_pump_off()
    await asyncio.sleep(0.2)

    # retrait bras gauche
    ####await goldo_lift_move(GoldoLift.Left, 100)
    await goldo_lift_move(GoldoLift.Left, 120)
    taskarms = asyncio.create_task(servos.moveMultiple(bras_gauche_prise_marron, 1))

    # depose jaune
    ####await goldo_lift_move(GoldoLift.Right, 400)
    await goldo_lift_move(GoldoLift.Right, 420)
    await servos.moveMultiple(bras_droit_depose_jaune, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Right, 400)
    await asyncio.sleep(0.2)
    await right_pump_off()
    await asyncio.sleep(0.1)

    # prise rose
    await servos.moveMultiple(bras_droit_prise_rose, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Right, 40)
    await right_pump_on()
    await asyncio.sleep(0.2)

    # depose rose
    ####await goldo_lift_move(GoldoLift.Right, 600)
    await goldo_lift_move(GoldoLift.Right, 620)
    await asyncio.sleep(0.1)
    await servos.moveMultiple(bras_droit_depose_rose, 1)
    await asyncio.sleep(0.3)
    await right_pump_off()
    await taskarms
    await asyncio.sleep(0.2)

    # ecartement bras
    taskarms = asyncio.create_task(servos.moveMultiple(coudes_leves, 1))
    await servos.moveMultiple(epaules_ouvertes, 1)
    await taskarms


@robot.sequence
async def test_prise_gauche():
    await goldo_lifts_move(100, 80)
    await asyncio.sleep(5)
    await right_pump_on()
    # bras au dessus du jaune
    taskarms = asyncio.create_task(servos.moveMultiple(bras_droit_prise_jaune, 1))
    await taskarms
    await asyncio.sleep(5)
    # descente pour prise
    await goldo_lifts_move(40, 80)
    await asyncio.sleep(5)
    # depose jaune
    await goldo_lift_move(GoldoLift.Right, 400)
    await servos.moveMultiple(bras_droit_depose_jaune, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Right, 400)
    await asyncio.sleep(0.2)
    await right_pump_off()
    await asyncio.sleep(0.1)



# Constructions bleues
async def construction_gateau_haut_bleu():
    ####await goldo_lifts_move(500, 80)
    await goldo_lifts_move(520, 80)
    await pump_on(True, True)
    # bras au dessus du jaune et du marron
    taskarms = asyncio.create_task(servos.moveMultiple(bras_gauche_prise_jaune, 1))
    await servos.moveMultiple(bras_droit_prise_marron, 1)
    await taskarms
    await asyncio.sleep(0.2)
    # descente pour prise
    await goldo_lifts_move(430, 80)
    await asyncio.sleep(0.2)
    # depose marron
    ####tasklifts = asyncio.create_task(goldo_lifts_move(430, 80))
    tasklifts = asyncio.create_task(goldo_lifts_move(520, 80))
    await servos.moveMultiple(bras_droit_depose_marron, 1)
    await asyncio.sleep(0.2)
    await tasklifts
    await goldo_lift_move(GoldoLift.Right, 150)
    await asyncio.sleep(0.3)
    await right_pump_off()
    await asyncio.sleep(0.2)

    # retrait bras droit
    #await goldo_lift_move(GoldoLift.Right, 500)
    await goldo_lift_move(GoldoLift.Right, 520)
    taskarms = asyncio.create_task(servos.moveMultiple(bras_droit_prise_marron, 1))

    # depose jaune
    #await goldo_lift_move(GoldoLift.Left, 800)
    await goldo_lift_move(GoldoLift.Left, 840)
    await asyncio.sleep(0.3)
    await servos.moveMultiple(bras_gauche_depose_jaune, 1)
    await asyncio.sleep(0.5)
    await goldo_lift_move(GoldoLift.Left, 380)
    await asyncio.sleep(0.3)
    await left_pump_off()
    await asyncio.sleep(0.2)

    # prise rose
    ####
    await goldo_lift_move(GoldoLift.Left, 620)
    await servos.moveMultiple(bras_gauche_prise_rose, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Left, 430)
    await left_pump_on()
    await asyncio.sleep(0.2)

    # depose rose
    await goldo_lift_move(GoldoLift.Left, 570)
    await servos.moveMultiple(bras_gauche_depose_rose, 1)
    await asyncio.sleep(0.3)
    await left_pump_off()
    await taskarms
    await asyncio.sleep(0.2)

    # ecartement bras
    taskarms = asyncio.create_task(servos.moveMultiple(coudes_leves, 1))
    await servos.moveMultiple(epaules_ouvertes, 1)
    await taskarms

async def construction_gateau_milieu_bleu():
    ####await goldo_lifts_move(300, 80)
    await goldo_lifts_move(320, 80)
    await pump_on(True, True)
    # bras au dessus du jaune et du marron
    taskarms = asyncio.create_task(servos.moveMultiple(bras_gauche_prise_jaune, 1))
    await servos.moveMultiple(bras_droit_prise_marron, 1)
    await taskarms
    await asyncio.sleep(0.2)
    # descente pour prise
    await goldo_lifts_move(210, 80)
    await asyncio.sleep(0.2)
    # depose marron
    ####tasklifts = asyncio.create_task(goldo_lifts_move(300, 80))
    tasklifts = asyncio.create_task(goldo_lifts_move(400, 80))
    await servos.moveMultiple(bras_droit_depose_marron, 1)
    await asyncio.sleep(0.2)
    await tasklifts
    await goldo_lift_move(GoldoLift.Right, 150)
    await asyncio.sleep(0.2)
    await right_pump_off()
    await asyncio.sleep(0.2)

    # retrait bras droit
    ####await goldo_lift_move(GoldoLift.Right, 300)
    await goldo_lift_move(GoldoLift.Right, 320)
    taskarms = asyncio.create_task(servos.moveMultiple(bras_droit_prise_marron, 1))

    # depose jaune
    ####await goldo_lift_move(GoldoLift.Left, 600)
    await goldo_lift_move(GoldoLift.Left, 620)
    await servos.moveMultiple(bras_gauche_depose_jaune, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Left, 400)
    await asyncio.sleep(0.3)
    await left_pump_off()
    await asyncio.sleep(0.2)

    # prise rose
    ####
    await goldo_lift_move(GoldoLift.Left, 420)
    await servos.moveMultiple(bras_gauche_prise_rose, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Left, 210)
    await left_pump_on()
    await asyncio.sleep(0.2)

    # depose rose
    await goldo_lift_move(GoldoLift.Left, 600)
    await asyncio.sleep(0.2)
    await servos.moveMultiple(bras_gauche_depose_rose, 1)
    await asyncio.sleep(0.3)
    await left_pump_off()
    await taskarms
    await asyncio.sleep(0.2)

    # ecartement bras
    taskarms = asyncio.create_task(servos.moveMultiple(coudes_leves, 1))
    await servos.moveMultiple(epaules_ouvertes, 1)
    await taskarms

async def construction_gateau_bas_bleu():
    ####await goldo_lifts_move(100, 80)
    await goldo_lifts_move(120, 80)
    await pump_on(True, True)
    # bras au dessus du jaune et du marron
    taskarms = asyncio.create_task(servos.moveMultiple(bras_gauche_prise_jaune, 1))
    await servos.moveMultiple(bras_droit_prise_marron, 1)
    await taskarms
    await asyncio.sleep(0.2)
    # descente pour prise
    await goldo_lifts_move(40, 80)
    await asyncio.sleep(0.2)
    # depose marron
    ####tasklifts = asyncio.create_task(goldo_lifts_move(100, 80))
    tasklifts = asyncio.create_task(goldo_lifts_move(140, 80))
    await servos.moveMultiple(bras_droit_depose_marron, 1)
    await asyncio.sleep(0.2)
    await tasklifts
    await goldo_lift_move(GoldoLift.Right, 100)
    await asyncio.sleep(0.2)
    await right_pump_off()
    await asyncio.sleep(0.2)

    # retrait bras droit
    ####await goldo_lift_move(GoldoLift.Right, 100)
    await goldo_lift_move(GoldoLift.Right, 120)
    taskarms = asyncio.create_task(servos.moveMultiple(bras_droit_prise_marron, 1))

    # depose jaune
    ####await goldo_lift_move(GoldoLift.Left, 400)
    await goldo_lift_move(GoldoLift.Left, 420)
    await servos.moveMultiple(bras_gauche_depose_jaune, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Left, 400)
    await asyncio.sleep(0.2)
    await left_pump_off()
    await asyncio.sleep(0.1)

    # prise rose
    await servos.moveMultiple(bras_gauche_prise_rose, 1)
    await asyncio.sleep(0.2)
    await goldo_lift_move(GoldoLift.Left, 40)
    await left_pump_on()
    await asyncio.sleep(0.2)

    # depose rose
    ####await goldo_lift_move(GoldoLift.Left, 600)
    await goldo_lift_move(GoldoLift.Left, 620)
    await asyncio.sleep(0.2)
    await servos.moveMultiple(bras_gauche_depose_rose, 1)
    await asyncio.sleep(0.2)
    await left_pump_off()
    await taskarms
    await asyncio.sleep(0.2)

    # ecartement bras
    taskarms = asyncio.create_task(servos.moveMultiple(coudes_leves, 1))
    await servos.moveMultiple(epaules_ouvertes, 1)
    await taskarms
