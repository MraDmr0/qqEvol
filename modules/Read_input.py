#qqEvol_Ver2.0: Read_input.py
#
##Function to parse input file and extract data while making sure that they are  of the correct type## 
#
#import python packakges
import re
import sys
#
def read_input(filein , allowed_data):
  """Extract from input file the values of elements in allowed_data 
     and checks if the type corresponds to the expected one.

     Input: "filein"       txt input file
            "allowed_data" dictionary of expected data key names and type

    Output: "data" dictionary of keys and values of input data
  """
  #initialize empty dictionary
  data = {
  #try to open filein
  try:
    with open(filein , "r") as textfile:
      #
      print(f"File '{filein}' opened successfully.")
      #parse lines
      lines = textfile.readlines()
      #search keys of allowed_data in input file
      for key , expected_type in allowed_data.items():
        #pattern "key =" to search in input file
        pattern = rf"{re.escape(key)}\s*[:=]\s*(.+)"
        #check for pattern in each line
        for line in lines:
          match =  re.search(pattern , line)
          #when pattern found
          if match:
            #strip the value corresponding to key in input file
            value = match.group(1).strip()
            #eliminate commas if present
            if value.startswith(("'", '"')) and value.endswith(("'", '"')):
              value = value[1:-1]
            #check if the type of input file data is the expected one
            try:
              if expected_type == float:
                  value = float(value)
              elif expected_type == int:
                  value = int(value)
              elif expected_type == str:
                #make sure that strings are not just numbers inside ""
                if re.fullmatch(r"^\d+(\.\d+)?$", value):
                  print(f"Error: The value '{value}' for '{key}' should be a string but instead it's a number.") 
                  sys.exit(1)
                else:
                  value = str(value)
            #handle wrong type of input data exception
            except ValueError:
              print(f"Error: The value '{value}' for '{key}' is not of the expected type: {expected_type.__name__}.")
              sys.exit(1)
            #append input data to output dictionary  
            data[key] = value
  #handle non-existing filein exception
  except FileNotFoundError:
    print(f"File '{filein}' not found.") 
    sys.exit(1)
  #handle other exceptions
  except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
 
  return data