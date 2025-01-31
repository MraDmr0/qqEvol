##Set of functions to define allowed data, dimensions, potentials and other features##
#
from RK4        import rk4_qb , rk4_qq
from Envelopes  import off , const , sing_imp , sing_gauss , two_imp , two_gauss
from Potentials import potential1_qb , potential1_qq , potential2_qb , potential2_qq
from Set_input  import set_input_qb , set_input_qq
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

def std_data(): 
  return {"prefix": "qq" , "D": 4  , "ti":0  , "S":20 , "qb_mod":"off" , "env_mod":"off", "F1":1}

def mand_data(D):
  if D == 2:
    return ["psi0" , "psi1" ,  "N" , "wr00"   ,"wr01"   , "wr02"   , "wr03"   , "wl0"]

def allowed_qbmode():
  return {"off" : False , "on": True }

def allowed_pairs():
  """pair of data that if not both specified are set to be equal """
  return [("w1" , "w2") , ("F1" , "F2") , ("sigma1" , "sigma2")]

def allowed_dimensions():
  """supported system dimensions"""
  return { 2 : "qubit" , 4 : "ququart"}
#
def allowed_rk():
  """dictionary to choose which rk4 and set_input functions to use"""
  return { 2 : [rk4_qb , set_input_qb] , 4 : [rk4_qq , set_input_qq]}
#
def allowed_envelopes():
  """supported envelope functions"""
  return {"off" : off , "const" : const , "singimp" : sing_imp , "gauss" : sing_gauss , "2imp" : two_imp , "2gauss" : two_gauss}
#
def allowed_potentials():
  """dictionary to choose which potential function to use"""
  return {"off"  : {2 : potential1_qb  , 4 : potential1_qq} , "const" : {2 : potential1_qb  , 4 : potential1_qq} , "singimp" : {2 : potential1_qb  , 4 : potential1_qq} ,
          "gauss": {2 : potential1_qb  , 4 : potential1_qq} , "2imp"  : {2 : potential2_qb  , 4 : potential2_qq} , "2gauss"  : {2 : potential2_qb  , 4 : potential2_qq}}
#
