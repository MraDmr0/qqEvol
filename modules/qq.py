##Main executable file of qqPackage Ver. 2##
if __name__ == "main":
    #import python packages
    import numpy as np
    import time
    import datetime
    import sys
    #import local packages
    from Allowed_input import allowed_dimensions , allowed_envelope , allowed_potentials , allowed_rk , allowed_data , allowed_pairs , mandatory_input , optional_input , allowed_qbmode
    from Read_input    import read_input 
    from Write_output  import write_out , save_out
    from Set_input     import set_input_qb , set_input , set_potential
    from Check_input   import check_dimensions , check_mandin , check_envelope , check_qbmode
    from Evolution     import evolution
    from Plot          import plot
    #
    #Staring message
    print("Execution of qq.py started at : " + str(datetime.datetime.now()) + "\n")
    #
    #load the key names of all possible data
    all_data       = allowed_data()
    #define mandatory data
    mand_input     = mandatory_input()
    #load supported modes
    all_dimensions = allowed_dimensions()
    all_env        = allowed_envelope()
    all_qbmode     = allowed_qbmode()
    #
    #acquire input file
    filein = str(sys.argv[1])
    #
    #parse input file and appends the allowed valued to data
    print("Looking for " + str(filein) + "...\n")
    data = read_input(filein , all_data)
    #
    #write input data on output file
    write_out(data)
    #
    #check if dimensions and modes are supported
    print("Checking input data...\n")
    check_dimensions(data , all_dimensions)
    check_mandin(data     , mand_input)
    
    envelope , env_in          = check_envelope(data   , all_env )
    setinput , rk  , potential = check_qbmode(data , all_qbmode)

    #extract initial condition and frequencies trough set_input
    psi_in , wr , wl  = setinput(data)
    #
    #begin of main calculation
    print("Begin of the calculation...")
    time1 = time.time()
    #
    #compute envelope function
   # E_in = envelope(int(data["N"]) , float(data["ti"] ) , float(data["tf"] ) , env_in)
    #
    #call rk4
    psi_out , t_out , E_out = rk(psi_in , wr , wl , envelope , env_in , potential , float(data["ti"]) , float(data["tf"]) , int(data["N"]) , int(data["D"]))
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








