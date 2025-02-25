#qqEvoll_Ver2.0: Write_output.py
#
##Functions to write the input data on output file and save the results##
#
from numpy import savetxt
#
def write_out(data):
  """prints the input data from dictionary in formatted way.
     
     Input: "data" dictionary of input data
  """
  #check max length of key to print
  length  = max(len(key) for key in data)
  # decide on padding and width of *
  padding = 5
  width   = 40
  #total space between name and values
  space   = length + padding
  #
  print("*" * width)
  print("Input parameters : \n")
  #print all values in input dictionary
  for key , value in data.items():
    #
    name = "{0:{space}}".format(key, space=space)
    num  = "{0:1}".format(value)
    print(name + " = " + num)
  #
  print("*" * width+"\n")


def save_out(prefix , psiff , tff , E_out): 
  "wirtes the results of the calculation on output files"
  #open the output files
  q_save = open("psi_"+ str(prefix) + ".txt" , "w") 
  t_save = open("t_"  + str(prefix) + ".txt" , "w") 
  E_save = open("envelope_" + str(prefix) + ".txt" , "w") 
  #write the results
  savetxt(q_save , psiff) 
  savetxt(t_save , tff) 
  savetxt(E_save , E_out)
  #close the output files
  q_save.close() 
  t_save.close()
  E_save.close()
#

    
