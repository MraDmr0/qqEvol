##Function that reads the input file and stores the needed data## 
#
import re
#
def read_input(filein , allowed_data ):
  #empty dictionary
  data = {}
  #
  with open(filein , "r") as textfile:
    lines = textfile.readlines()
  #
  for key in allowed_data:
    #patter to search in input file
    pattern = rf"{re.escape(key)}\s*[:=]\s*(.+)"
    #check for pattern in each line
    for line in lines:
      match =  re.search(pattern , line)
      #append the value to output dictionary
      if match:
        value = match.group(1).strip()
        data[key] = value
  return data
#
#old version: to be eliminated
def read_input1(filein , allowed_data):
  """
  Reads the parameters of the run from input and stores needed data
  """
  with open(filein) as textfile:
    # read a line from the file
    for line in textfile:  
      #if not "#" in line and line.strip():
      #split arguments with =
      name = line.split('=')
      #append needed data to library
      if name[0].strip() in allowed_data:
        allowed_data[name[0].strip()] = name[1].strip()
  return allowed_data
  #