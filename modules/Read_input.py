##Function that reads the input file and stores the needed data## 
#
import re
#
def read_input(filein , allowed_data):
  #empty dictionary
  data = {}
  #try to open filein
  try:
    with open(filein , "r") as textfile:
      pass
  #handle non-existing filein
  except FileNotFoundError:
    print(f"File '{filein}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")
 
  #if exists, parse lines
  else:
    print(f"File '{filein}' opened successfully.")
    lines = textfile.readlines()
  #append allowed_data in input to data
    for key in allowed_data:
      #pattern to search in input file
      pattern = rf"{re.escape(key)}\s*[:=]\s*(.+)"
      #check for pattern in each line
      for line in lines:
        match =  re.search(pattern , line)
        #append the value to output dictionary
        if match:
          value = match.group(1).strip()
          data[key] = value

  return data
