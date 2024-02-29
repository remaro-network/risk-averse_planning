import pydot
import os

class ConvertDotPNG:
   def __init__(self, root_folder, current_folder, filename, sub_folder=None):
      self.current_folder = current_folder
      self.root_folder = root_folder
      self.filename = filename
      self.sub_folder= sub_folder
      self.postfix = ".dot"
      self.postfix_png = ".png"
      
   def convert_dot_to_png(self):
     
      path = self.root_folder + self.current_folder  + \
                                             self.sub_folder + \
                                             self.filename + self.postfix
      
      (graph,) = pydot.graph_from_dot_file(path)
      
      graph.write_png(self.root_folder + self.current_folder + self.filename + self.postfix_png)
      
      print("PNG file saved successfully.")



if __name__ == "__main__":
   print("Nothing in main")
