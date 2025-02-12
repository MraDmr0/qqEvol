##Function that reads the input file and stores the needed data## 
#
import re
import sys
#
def read_input(filein , allowed_data):
  #empty dictionary
  data = {}
  #try to open filein
  try:
    with open(filein , "r") as textfile:
      print(f"File '{filein}' opened successfully.")
      lines = textfile.readlines()
      #append allowed_data in input to data
      for key , expected_type in allowed_data.items():
        #pattern to search in input file
        pattern = rf"{re.escape(key)}\s*[:=]\s*(.+)"
        #check for pattern in each line
        for line in lines:
          match =  re.search(pattern , line)
        #append the value to output dictionary
          if match:
            value = match.group(1).strip()

            if value.startswith(("'", '"')) and value.endswith(("'", '"')):
              value = value[1:-1]

            try:
              if expected_type == float:
                  value = float(value)
              elif expected_type == int:
                  value = int(value)
              elif expected_type == str:
                if re.fullmatch(r"^\d+(\.\d+)?$", value):
                  print(f"Error: The value '{value}' for '{key}' should be a string but instead it's a number.") 
                  sys.exit(1)
                else:
                  value = str(value)
              # Default case: string (no conversion needed)
            except ValueError:
              print(f"Error: The value '{value}' for '{key}' is not of the expected type: {expected_type.__name__}.")
              sys.exit(1)
              
            data[key] = value
      
  #handle non-existing filein
  except FileNotFoundError:
    print(f"File '{filein}' not found.") 
    sys.exit(1)
  except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
 
  return data
