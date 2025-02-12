if __name__ == "__main__":
  import sys
  import Read_input  as RI
  from check_in import Check_input

  all_data = {
  "prefix"  : str  ,
  "D"       : int  ,
  "ti"      : float, 
  "tf"      : float, 
  "N"       : int  , 
  "S"       : int  , 
  "psi0"    : float,   
  "psi1"    : float,   
  "psi2"    : float,   
  "psi3"    : float,   
  "wr00"    : float, 
  "wr01"    : float, 
  "wr02"    : float, 
  "wr03"    : float, 
  "wr10"    : float, 
  "wr11"    : float, 
  "wr12"    : float, 
  "wr13"    : float, 
  "wr20"    : float, 
  "wr21"    : float, 
  "wr22"    : float,  
  "wr23"    : float, 
  "wr30"    : float, 
  "wr31"    : float, 
  "wr32"    : float, 
  "wr33"    : float, 
  "wl0"     : float,
  "wl1"     : float,
  "wl2"     : float,
  "wl3"     : float,
  "w1"      : float,
  "w2"      : float,
  "qb_mode" : str  ,
  "env_mode": str  ,
  "F1"      : float, 
  "F2"      : float,
  "t0"      : float, 
  "t1"      : float, 
  "sigma1"  : float  , 
  "sigma2"  : float  ,
  "t00"     : float, 
  "t11"     : float
  }

  all_qbmode  = {"off":[[
  "prefix" , 
  "D"      ,
  "ti"     , 
  "tf"     , 
  "N"      , 
  "S"      , 
  "env_mode"
  ], "set_input_qb" , "rk4_qb" ] , 
  "on":[[
  "prefix" ,
  "ti"     , 
  "tf"     , 
  "N"      , 
  "S"      , 
  "env_mode",
  "wr00"   , 
  "wr01"   , 
  "wr02"   , 
  "wr03"   ,
  "wl0"    
  ], "set_input" , "rk4_qq"]} 

  all_dim = {"2":[
    "psi0"   ,   
    "psi1"   ,  
    "wr00"   , 
    "wr01"   , 
    "wr10"   , 
    "wr11"   , 
    "wl0"    ,
    "wl1"    
  ] 
  , "3":[
    "psi0"   ,   
    "psi1"   ,   
    "psi2"   ,  
    "wr00"   , 
    "wr01"   , 
    "wr02"   , 
    "wr10"   , 
    "wr11"   , 
    "wr12"   , 
    "wr20"   , 
    "wr21"   , 
    "wr22"   ,  
    "wl0"    ,
    "wl1"    ,
    "wl2"    ,
  ] 
  , "4":[
    "psi0"   ,   
    "psi1"   ,   
    "psi2"   ,   
    "psi3"   ,   
    "wr00"   , 
    "wr01"   , 
    "wr02"   , 
    "wr03"   , 
    "wr10"   , 
    "wr11"   , 
    "wr12"   , 
    "wr13"   , 
    "wr20"   , 
    "wr21"   , 
    "wr22"   ,  
    "wr23"   , 
    "wr30"   , 
    "wr31"   , 
    "wr32"   , 
    "wr33"   , 
    "wl0"    ,
    "wl1"    ,
    "wl2"    ,
    "wl3"    ,
  ]}


  all_pot     = { "off":{"off": "potential1_qq" , "const" : "potential1_qq" , "singimp" : "potential1_qq" , "gauss": "potential1_qq" , "2imp" : "potential2_qq" , "2gauss" : "potential2_qq"} 
                , "on" : {"off": "potential1_qb" , "const" : "potential1_qb" , "singimp" : "potential1_qb" , "gauss": "potential1_qb" , "2imp" : "potential2_qb" , "2gauss" : "potential2_qb"}}

  all_env     = {"off" : [[],["off"]] , 
                "const" : [["F1" , "w1"], "const"] , 
                "singimp":[["F1" , "W1" , "t0" , "t1"], "sing_imp"] , 
                "gauss":[["F1" , "w1" , "t0" , "sigma1"], "sing_gauss"] ,
                "2imp":[["F1" , "F2", "w1" , "w2" , "t0" , "t1" , "t00" , "t11"], "two_imp"] , 
                "2gauss":[["F1" , "F2" , "w1" , "w2" , "t0" , "t1" , "sigma1" , "sigma2"], "two_gauss"] }


  filein = str(sys.argv[1])
  
  
  data = RI.read_input(filein , all_data)


  
  ine = Check_input(data , all_qbmode , all_dim , all_env, all_pot)

  ine.check_qbmode()
  ine.check_env()
  ine.check_pot()
  ine.check_data()

  print("Input data imported correctly.")
  print(data)









