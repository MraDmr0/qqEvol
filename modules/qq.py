#qqEvol_Ver2.0: qq.py
#
##Main executable file that handels all the proesses of the qqEvol package##
#
if __name__ == "__main__":
    """main file of qqEvol_Ver2.0 package that handles all the process to executes the
       RK4 simulation.

       Input: "filein" (eg. "prefix.in") with input data. 
              See README.md for further informations on inputfile.
       
       Output: "prefix.out" report of the calculation, 
               "psi_prefix.txt" occupations as a function of time,
               "t_prefix.txt"  arrow of time,
               "env_prefix.txt" envelope as a function of time.
    """
    #print starting message
    
    #
    #import python packages
    import time
    import datetime
    import sys
    #import qqEvol modules
    import Allowed_input as AI
    import Read_input    as RI
    import Write_output  as WO
    from Check_in import Check_input
    import Plot        
    
    from RK4        import rk4_qb , rk4_qq
    from Set_input  import set_input_qb , set_input
    from Potentials import potential1_qb , potential1_qq , potential2_qb , potential2_qq
    from Envelopes  import off , const , sing_imp , sing_gauss , two_imp , two_gauss
  
    #
    print("Execution of qq.py started at: " + str(datetime.datetime.now()) + "\n")
    print("Loading data structure...\n")
    #
    #load the key names and types of possible input data
    all_data       = AI.allowed_data()
    #load supported modes
    all_dim        = AI.allowed_dimension()
    all_env        = AI.allowed_envmode()
    all_qbmode     = AI.allowed_qbmode()
    all_pot        = AI.allowed_pot()
    #
    #read the name of input file
    filein = str(sys.argv[1])
    #
    #parse input file and append values to data
    print("Looking for " + str(filein) + "...\n")
    data = RI.read_input(filein , all_data)
    #
    #write the extracted input data on output file
    WO.write_out(data)
    #
    #check if specified qb_mode , env_mode and dimension are supported
    #check if mandatory data are present in input file
    #return the lists of keys and values of input data and the
    #right  functions for rk4 , potential and envelope
    print("Checking input data...\n")
    #initialize check_input class
    chk = Check_input(data , all_qbmode , all_dim , all_env, all_pot)
    #exectute check of modes
    chk.check_qbmode()
    chk.check_env()
    chk.check_pot()    
    #execute check of input data
    chk.check_data()
    #extract rk4, potential, envelope and set_input functions
    rk        = chk.rk
    potential = chk.pot
    envelope  = chk.env
    setinput  = chk.setin
    env_in    = chk.env_in
    #extract input data needed according to the specified modes
    psi_in , wr , wl  = setinput(data)
    #
    #begin of main calculation
    print("Begin of the calculation...\n")
    print(potential)
    print(envelope)
    print(rk)
    print(setinput)
    #
    #read current time
    time1 = time.time()
    #
    #call rk4
    print(env_in)
    psi_out , t_out , E_out = rk(psi_in , wr , wl , envelope , env_in , potential , data["ti"] , data["tf"] , data["N"] , data["S"] , data["D"])
    #
    #read current time
    time2 = time.time()
    #
    #end of main calculation
    print("Calculation completed successfully")
    print("Elapsed time for RK4 cycle : " + str(time2-time1) + " s \n" )
    #
    #Write final result on text file
    WO.save_out(data["prefix"] , psi_out , t_out , E_out)
    print("Reults written on psi_" + data["prefix"]+".txt'")
    #
    #plot results
    Plot.plot(data["prefix"] , data["D"])
    #
    #exit message
    print(f"The execution of qq.py has been completed successfully at: "+ str(datetime.datetime.now())+"\n")
    








