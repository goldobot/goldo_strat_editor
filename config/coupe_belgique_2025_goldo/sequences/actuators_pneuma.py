import asyncio
from enum import Enum

# VALVE 1 : ecarteurs
valve_1 = 0
# VALVE 2 : ventouses int
valve_2 = 0
# VALVE 3 : ventouses ext
valve_3 = 0
valve_purge = 0

@robot.sequence
async def start_compressor():
    pneumatic.set_valves(0, 0, 0, 0)
    pneumatic.start_compressor(30)

@robot.sequence
async def stop_compressor():
    pneumatic.stop_compressor()

@robot.sequence
async def purge():
    pneumatic.purge_compressor()
    pneumatic.set_valves(0, 0, 0, 1)

@robot.sequence
async def reset_valves():
    global valve_1
    global valve_2
    global valve_3
    global valve_purge
    valve_1 = 0
    valve_2 = 0
    valve_3 = 0
    valve_purge = 0
    pneumatic.set_valves(0, 0, 0, 0)

@robot.sequence
async def ventouses_int_lache():
    global valve_1
    global valve_2
    global valve_3
    global valve_purge
    valve_2 = 1
    pneumatic.set_valves(valve_1, valve_2, valve_3, valve_purge)

@robot.sequence
async def ventouses_int_attrape():
    global valve_1
    global valve_2
    global valve_3
    global valve_purge
    valve_2 = 0
    pneumatic.set_valves(valve_1, valve_2, valve_3, valve_purge)

@robot.sequence
async def ventouses_ext_lache():
    global valve_1
    global valve_2
    global valve_3
    global valve_purge
    valve_3 = 1
    pneumatic.set_valves(valve_1, valve_2, valve_3, valve_purge)

@robot.sequence
async def ventouses_ext_attrape():
    global valve_1
    global valve_2
    global valve_3
    global valve_purge
    valve_3 = 0
    pneumatic.set_valves(valve_1, valve_2, valve_3, valve_purge)

@robot.sequence
async def ecarteur_on():
    global valve_1
    global valve_2
    global valve_3
    global valve_purge
    valve_1 = 1
    pneumatic.set_valves(valve_1, valve_2, valve_3, valve_purge)

@robot.sequence
async def ecarteur_off():
    global valve_1
    global valve_2
    global valve_3
    global valve_purge
    valve_1 = 0
    pneumatic.set_valves(valve_1, valve_2, valve_3, valve_purge)
