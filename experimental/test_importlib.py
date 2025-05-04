import sys
import importlib.abc, importlib.util

positions = None

class SimRobot():
   def __init__(self):
      self._func_dico = {}
   def sequence(self,func):
      self._func_dico[func.__name__] = func

class MyLoader(importlib.abc.SourceLoader):
   def __init__(self, data):
      self.data = data
   def get_source(self, fullname):
      return self.data
   def get_data(self, path):
      return self.data.encode("utf-8")
   def get_filename(self, fullname):
      return fullname + ".py"

def import_positions(conf_path):
   global positions

   module_name = "positions"
   with open(conf_path + "/sequences/positions.py", "r") as mod_fd:
      loader = MyLoader(mod_fd.read())

   spec = importlib.util.spec_from_loader(module_name, loader, origin="built-in")
   positions = importlib.util.module_from_spec(spec)
   sys.modules[module_name] = positions

   sim_robot = SimRobot()

   mod_vars = vars(positions)

   mod_vars['robot'] = sim_robot

   spec.loader.exec_module(positions)


def get_poses(_pattern):
   global positions

   my_poses = []

   yellow_sim = dir (positions.YellowPoses)
   blue_sim = dir (positions.BluePoses)

   for item in yellow_sim:
      if _pattern in item:
         print ("{} = {}".format(item,eval("positions.YellowPoses."+item)))
         my_poses.append(eval("positions.YellowPoses."+item))

   for item in blue_sim:
      if _pattern in item:
         print ("{} = {}".format(item,eval("positions.BluePoses."+item)))
         my_poses.append(eval("positions.BluePoses."+item))

   return my_poses


def get_start_poses():
   return get_poses('_start_pose')


def get_preprise_poses():
   return get_poses('_preprise')


def get_predepose_poses():
   return get_poses('_predepose')


