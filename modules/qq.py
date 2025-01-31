##Main executable file of qqPackage Ver. 2##
#
#import python packages
import numpy as np
import time
import datetime
import sys
#import local packages
from Allowed_input import allowed_dimensions , allowed_envelopes , allowed_potentials , allowed_rk , allowed_data , allowed_pairs
from Read_input    import read_input 
from Write_output  import write_out , save_out
from Set_input     import set_input_qb , set_input_qq , optional_pairs
from Check_input   import check_dimensions , check_envelope
from Evolution     import evolution
from Plot          import plot
#
#Staring message
print("Execution of qq.py started at : " + str(datetime.datetime.now()) + "\n")
#
#load the key names of needed data
allowed_data       = allowed_data()
#
#load supported modes
allowed_dimensions = allowed_dimensions()
allowed_envelopes  = allowed_envelopes()
allowed_potentials = allowed_potentials()
allowed_rk         = allowed_rk()
allowed_pairs      = allowed_pairs()
#
#acquire input file
filein = str(sys.argv[1])
#
#parse input file and appends the allowed valued to data
print("Reading input file " + str(filein) + "...\n")
data = read_input(filein , allowed_data)
#
#write input data on output file
write_out(data)
#
#check if dimensions and mode are supported
print("Checking input data...\n")
rk                   = check_dimensions(int(data["D"]) , allowed_dimensions , allowed_rk)
envelope , potential = check_envelope(int(data["D"]) , str(data["mode"]) , allowed_envelopes , allowed_potentials)
#
#handle optional input data
data = optional_pairs(data , allowed_data , allowed_pairs )
#extract initial condition and frequencies trough set_input
psi_in , wr , wl , data = rk[1](data)
#
#begin of main calculation
print("Begin of the calculation...")
time1 = time.time()
#
#compute envelope function
E_in = envelope(int(data["N"]) , float(data["ti"] ) , float(data["tf"] ) , float(data["F1"] ) , float(data["F2"] ) , float(data["t0"] ) , float(data["t1"] ) , float(data["sigma1"]), float(data["sigma2"]), float(data["t00"]) , float(data["t11"]))
#
#call rk4
psi_out , t_out , E_out = rk[0](psi_in , wr , wl , E_in , potential , float(data["ti"]) , float(data["tf"]) , int(data["N"]) , int(data["S"]) , float(data["w1"]), float(data["w2"]))
#psi_out , t_out , envelope_out  = evolution(rk , envelope , potential , data)
time2 = time.time()
#
#Write final result on text file
save_out(data["prefix"] , psi_out , t_out , E_out)
#
#plot results
plot(data["prefix"] , float(data["D"]))
#
#Exit message
print("Calculation completed successfully at : "+ str(datetime.datetime.now())+"\n")
print("Elapsed time for main process : " + str(time2-time1) + " s \n" )
print("Reults written on psi_"+data["prefix"]+".txt'")








