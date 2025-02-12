##Set of functions to define allowed data, dimensions, potentials and other features##
#
from RK4        import rk4_qb , rk4_qq
from Envelopes  import off , const , sing_imp , sing_gauss , two_imp , two_gauss
from Potentials import potential1_qb , potential1_qq , potential2_qb , potential2_qq
from Set_input  import set_input_qb , set_input

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

allowed_dim = {2:[
  "psi0"   ,   
  "psi1"   ,  
  "wr00"   , 
  "wr01"   , 
  "wr10"   , 
  "wr11"   , 
  "wl0"    ,
  "wl1"    
] 
, 3:[
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
, 4:[
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