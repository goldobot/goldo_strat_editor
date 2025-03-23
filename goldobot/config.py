import yaml
import pathlib
from collections import OrderedDict
import struct

import runpy
import inspect

# FIXME : TODO
#from .hal_config import HALConfig
#from goldobot import messages

from google.protobuf.json_format import ParseDict

from goldobot import sequences_importer
import importlib


def align_buffer(buff):
    k = len(buff) % 8
    if k == 0:
        return buff
    else:
        return buff + b'\0' * (8-k)
        
class SequencesRobot(object):
    def __init__(self):
        self._sequences = {}
        self._sequence_names = []

    def sequence(self, func):
        self._sequences[func.__name__] = func
        self._sequence_names.append(func.__name__)
        return func

class DebugGui(object):
    
    def pose(self, pose):
        print(pose)

class RobotConfig:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.update_config()
        
    def update_config(self):
        #load nucleo config protobuf
# FIXME : TODO
        #self.robot_config = _sym_db.GetSymbol('goldo.robot.RobotConfig')()
        #nucleo_config = self.robot_config.nucleo
        self.yaml = yaml.load(open(self.path / 'nucleo.yaml'),Loader=yaml.FullLoader)
        
        ParseDict(yaml.load(open(self.path / 'hal.yaml'),Loader=yaml.FullLoader), self.robot_config, ignore_unknown_fields=True)
        ParseDict(yaml.load(open(self.path / 'nucleo.yaml'),Loader=yaml.FullLoader), self.robot_config, ignore_unknown_fields=True)
        ParseDict(yaml.load(open(self.path / 'robot.yaml'),Loader=yaml.FullLoader), self.robot_config, ignore_unknown_fields=True)
        ParseDict(yaml.load(open(self.path / 'strategy.yaml'),Loader=yaml.FullLoader), self.robot_config, ignore_unknown_fields=True)
# FIXME : TODO
        #self.hal_config = HALConfig(nucleo_config.hal)
        #self.config_proto = nucleo_config
        
        self.strategy = yaml.load(open(self.path / 'map.yaml'),Loader=yaml.FullLoader)

        robot = SequencesRobot()
        
        #import all sequences
        sequences_path = self.path / 'sequences'
        sequences_importer.meta_finder.sequences_path = sequences_path
        debug_gui = DebugGui()
        sequences_importer.meta_finder.inject_globals = {'robot': robot, 'config': self.robot_config, 'debug_gui': debug_gui}
        
        sequences = importlib.import_module('sequences.sequences')
        
        self.robot_config.sequences_names.extend(robot._sequence_names)
        
# FIXME : TODO
        #for k, v in sequences_importer.meta_finder.sequence_modules.items():   
        #    sequences_file = _sym_db.GetSymbol('goldo.robot.SequencesFile')()
        #    sequences_file.path = v.__name__[10:] + '.py'
        #    sequences_file.body = open(v.__file__).read()
        #    self.robot_config.sequences_files.extend([sequences_file])   

        sequences_importer.meta_finder.unload_all()
        
# FIXME : TODO
        #self.dc_motors_indices = {}
        #self.sensors_indices = {s.name:s.id for s in self.config_proto.sensors}
        #self.gpio_indices = {s.name:s.id for s in self.config_proto.hal.gpio}        
      
    def get_servo_index(self, name):
        return [s['name'] for s in self.yaml['servos']].index(name)
        
    def get_sensor_index(self, name):
        return self.sensors_indices[name]
        
    def get_gpio_index(self, name):
        return self.gpio_indices[name]
        
    def get_dc_motor_index(self, name):
        return self.dc_motors_indices[name]
        
    def get_arm_position_index(self, name):
        return list(self.dynamixels_positions.keys()).index(name) 

#Full config format:
# Offsets table
# hal config offset
# robot_config offset
# odometry_config offset
# propulsion_config offset
# arms_config offset
# arms position config offset
# servos config offset
# sequences_config offset
# arms torque offset

# FIXME : TODO
#def load_config(path):
#    global robot_config
#    robot_config = RobotConfig(path)
#    
#def compute_crc(buffer):
#    crc = 0
#    for b in buffer:
#        x = crc >> 8 ^ b;
#        x ^= x >> 4;
#        crc = ((crc << 8) ^ (x << 12) ^ (x << 5) ^ x) & 0xffff;
#    return crc

    
