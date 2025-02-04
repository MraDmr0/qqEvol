##Set of functions to define allowed data, dimensions, potentials and other features##
#
from RK4        import rk4_qb , rk4_qq
from Envelopes  import off , const , sing_imp , sing_gauss , two_imp , two_gauss
from Potentials import potential1_qb , potential1_qq , potential2_qb , potential2_qq
from Set_input  import set_input_qb , set_input
#
def allowed_data():
  """allowed input data"""
  allowed_data = [
  "prefix" ,
  "D"      ,
  "ti"     , 
  "tf"     , 
  "N"      , 
  "S"      , 
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
  "w1"     ,
  "w2"     ,
  "qb_mod" ,
  "env_mod",
  "F1"     , 
  "F2"     ,
  "t0"     , 
  "t1"     , 
  "sigma1" , 
  "sigma2" ,
  "t00"    , 
  "t11"    
  ]

  return allowed_data
#
def allowed_dimensions():
  """supported system dimensions"""
  return [2 , 3 , 4]

def mandatory_input():
  return {2 : ["prefix" ,
  "D"      ,
  "ti"     , 
  "tf"     , 
  "N"      , 
  "S"      , 
  "psi0"   ,   
  "psi1"   ,     
  "wr00"   , 
  "wr01"   , 
  "wr02"   , 
  "wr03"   , 
  "wl0"    ,
  "env_mode"] 
          
          , 4:[

  "prefix" ,
  "D"      ,
  "ti"     , 
  "tf"     , 
  "N"      , 
  "S"      , 
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
  "env_mode"
  ]}

def allowed_qbmode():
  return {"off":
          ["wl1" , set_input , rk4_qq , 
          {"off": potential1_qq  , "const": potential1_qq  , "singimp": potential1_qq  , "gauss": potential1_qq  , "2impm": potential2_qq , "2gauss": potential2_qq } ] , 
          "on"
          :[set_input_qb , rk4_qb , 
          {"off": potential1_qb , "const": potential1_qb , "singimp": potential1_qb , "gauss": potential1_qb  , "2impm": potential1_qb , "2gauss": potential1_qb }]}

def allowed_envelope():
  return {"off" : [[],[const]] , "const" : [["F1" , "w1"], const] , "singimp":[["F1" , "W1" , "t0" , "t1"], sing_imp] , "gauss":[["F1" , "w1" , "t0" , "sigma1"], sing_gauss] 
          , "2imp":[["F1" , "w1" , "w2" , "t0" , "t1" , "t00" , "t11"], two_imp] , "2gauss":[["F1" , "w1" , "w2" , "t0" , "t1" , "sigma1" , "igma2"], two_gauss] }

def allowed_dpotentials():
  return {"off": {"off": potential1_qq  , "const": potential1_qq  , "singimp": potential1_qq  , "gauss": potential1_qq  , "2impm": potential2_qq , "2gauss": potential2_qq } , "on" : {"off": potential1_qb , "const": potential1_qb , "singimp": potential1_qb , "gauss": potential1_qb  , "2impm": potential1_qb , "2gauss": potential1_qb }}