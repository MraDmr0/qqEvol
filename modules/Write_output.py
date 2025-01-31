##Functions to write the output file and save the results##
#
from numpy import savetxt , array_str
import datetime
#
def write_out(data):
  "writes the input library data on output file"
  #check max length of names to print
  length  = max(len(x) for x in data)
  # decide on padding and width of *
  padding = 5
  width   = 40
  #total space between name and values
  space   = length + padding
  #
  print("*" * width)
  print("Input parameters : \n")
  #print all values in input library
  for key , value in data.items():
    #
    name = "{0:{space}}".format(key, space=space)
    num  = "{0:5}".format(value)
    print(name + " = " + num)
  #
  print("*" * width+"\n")
#
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

    
