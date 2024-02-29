import os
import subprocess
import convert_dot_to_png
import glob
import shutil
import random

print(os.getcwd())
 
"""run Safe-Planner program
"""
os.chdir("../safePlanner")

print(os.getcwd())

import sys

class MainProgram:

   def __init__(self, absolute_path, plan_folder, sub_plan_folder, \
               domain_filename, problem_filename, planner_name, verbose_flag, \
               outcome_flag, make_dot_graph, make_json_plan, space, program_name, stat, risk_factor):
      self.absolute_path = absolute_path
      self.plan_folder = plan_folder
      self.sub_plan_folder = sub_plan_folder
      self.domain_filename = domain_filename
      self.problem_filename = problem_filename
      self.planner_name = planner_name
      self.verbose_flag = verbose_flag
      self.outcome_flag = outcome_flag
      self.make_dot_graph = make_dot_graph
      self.make_json_plan = make_json_plan
      self.space = space
      self.program_name = program_name
      self.stat = stat
      self.risk_factor = risk_factor

   def run_program(self):
      # reserve for sending risk_factor to domain.py file
      result = subprocess.run(self.program_name + self.space +self.absolute_path + self.plan_folder + self.sub_plan_folder + self.domain_filename  \
                  + self.space + self.absolute_path +  self.plan_folder + self.sub_plan_folder + self.problem_filename \
                  + self.space + self.planner_name + self.space + self.make_json_plan + self.space + self.make_dot_graph  \
                  + self.space + self.outcome_flag + self.space + self.stat + self.space + self.verbose_flag, shell= True)
      return result
   
   def my_module(self, risk_factor):
      # sys.path.append('/src')
      print("Risk is " + str("%.2f" %risk_factor))
      # from src.domain import GroundedAction

      # Get the absolute path to the current script
      script_path = os.path.abspath(__file__)
      print(script_path)

      # Get the directory of the script
      script_directory = os.path.dirname(script_path)
      print(script_directory)

      # Get the absolute path to the module directory
      module_directory = os.path.join(script_directory, 'domain')
      print(module_directory)

      # Add the module directory to the sys.path
      sys.path.append(module_directory)

      # Now you can import and use your module
      # hello()
      # gAction = GroundedAction()
      # gAction.get_utility()

if __name__ == "__main__":
   ############################# Default #####################################
   absolute_path = os.getcwd()
   plan_folder = "/plans/prob_plans/"
   sub_plan_folder = "60states/"
   result_folder = "/results/"
   domain_filename = "SonarAUVDomain.pddl"
   problem_filename = "SonarAUVProblem.pddl"
   planner_name = "-c ff m fd"
   verbose_flag = "-v 2"
   outcome_flag = "--all-outcome"
   make_dot_graph = "-d -p"
   make_json_plan = "-j"
   space = " "
   stat_flag = "-s"
   program_name = "./sp"
   png_graph_folder = ""
   # risk_factor = 0.5 # should be changed

   ############################## RUN MainProgram ####################################
   for sample_num in range(1):
      # print(sample_num)
      risk_rand_factor = random.uniform(0.4, 1)
   

      mainObj = MainProgram(absolute_path= absolute_path, plan_folder= plan_folder, \
                        sub_plan_folder=sub_plan_folder, domain_filename=domain_filename, \
                        problem_filename= problem_filename, make_json_plan = make_json_plan, \
                        planner_name = planner_name, verbose_flag= verbose_flag, \
                        outcome_flag = outcome_flag, make_dot_graph = make_dot_graph, \
                        space = space, program_name = program_name, stat=stat_flag, risk_factor =risk_rand_factor)
      mainObj.run_program()
      mainObj.my_module(risk_rand_factor)

   ################################ Move results to Result Folder ###########################
   current_full_path = os.getcwd()
   full_path_plan_folder = absolute_path + plan_folder + sub_plan_folder 

   full_path_result_folder = absolute_path + result_folder 
   if not os.path.exists(full_path_result_folder + sub_plan_folder):
      os.mkdir(full_path_result_folder + sub_plan_folder)
   else:
      print(full_path_result_folder + sub_plan_folder)

   # change the directory which we'd like to move files
   os.chdir(full_path_plan_folder)
   

   files = [f for f in glob.glob('*.pddl') if 'Domain' or 'Problem' in f]

   for file in glob.glob("*"):
      if file in files:
         pass
      else:
         # print(full_path_plan_folder + "/" + file, full_path_result_folder \
         #             + sub_plan_folder  + file)
         shutil.move(full_path_plan_folder + "/" + file, full_path_result_folder \
                     + "/" + sub_plan_folder + "/" + file)

   # change the directory back
   os.chdir(current_full_path)

   ################################ Convert Dot Graph to PNG ################################
   filename = problem_filename.split(".")[0]
   dotfile_folder = result_folder
   try:
      convert_dot = convert_dot_to_png.ConvertDotPNG(root_folder=absolute_path, \
                                    current_folder=dotfile_folder, \
                                    sub_folder= sub_plan_folder, \
                                    filename= filename)
      convert_dot.convert_dot_to_png()
   except Exception as error:
      print(dotfile_folder)


