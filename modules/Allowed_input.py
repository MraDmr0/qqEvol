#qqEvol_Ver2.0: Allowed_input.py
#
##Set of functions to define allowed data, dimensions, potentials and other features of the qqEvol package##
#
from modules import RK4        as RK
from modules import Set_input  as SI
from modules import Potentials as PO
from modules import Envelopes  as EN

def allowed_data():
  """Returns the dictionary of allowed input data 
     and their expected type"""
  
  d = {"prefix"  : str , "D" : int , "ti" : float , "tf" : float , "N" : int , "S" : int , "psi0" : float , "psi1" : float , 
       "psi2" : float , "psi3" : float , "wr00" : float , "wr01" : float , "wr02" : float , "wr03" : float , "wr10" : float , 
       "wr11" : float , "wr12" : float , "wr13" : float , "wr20" : float , "wr21" : float , "wr22" : float , "wr23" : float , 
       "wr30" : float , "wr31" : float , "wr32" : float , "wr33" : float , "wl0" : float , "wl1" : float , "wl2" : float , "wl3" : float ,
       "w1" : float   , "w2" : float , "qb_mode" : str , "env_mode" : str , "F1" : float , "F2" : float , "t0" : float , "t1" : float , 
       "sigma1" : float , "sigma2" : float , "t00" : float , "t11" : float
  }
  return d

def allowed_qbmode():
  """Returns the dictionary of allowed qb_mode values and the corresponding
     mandatory input, rk4 function and set_input function to be used"""
  
  d = {
  "on" : [["prefix" , "D"  , "ti" , "tf" , "N"  , "S"  , "env_mode"], SI.set_input_qb , RK.rk4_qb ] , 
  "off" : [["prefix" , "ti" , "tf" , "N"  , "S"  , "env_mode" , "wr00" , "wr01" , "wr02" , "wr03" , "wl0"], SI.set_input , RK.rk4_qq]
  }
  return d

def allowed_dimension():
  """Returns the dictionary of supported dimensions and the corresponding
     mandatory input"""
  d = { 
  "2" : ["psi0" , "psi1" , "wr00" , "wr01" , "wr10" , "wr11" , "wl0"  , "wl1" ] , 
  "3" : ["psi0" , "psi1" , "psi2" , "wr00" , "wr01" , "wr02" , "wr10" , "wr11" , "wr12" , "wr20" , "wr21" , "wr22" , "wl0" , "wl1" , "wl2"] ,
  "4" : ["psi0" , "psi1" , "psi2" , "psi3" , "wr00" , "wr01" , "wr02" , "wr03" , "wr10" , "wr11" , "wr12" , "wr13" , "wr20" , "wr21" , 
         "wr22" , "wr23" , "wr30" , "wr31" , "wr32" , "wr33" , "wl0" , "wl1" , "wl2" ,"wl3"]
  }
  return d

def allowed_pot():
  """Returns the dictionary of supported qb_mode and qnv_mode
     and the corresponding potential function to be used"""
  
  d = { 
    "off": {"off": PO.potential1_qq , "const" : PO.potential1_qq , "singimp" : PO.potential1_qq , "gauss": PO.potential1_qq , "2imp" : PO.potential2_qq , "2gauss" : PO.potential2_qq} ,
    "on" : {"off": PO.potential1_qb , "const" : PO.potential1_qb , "singimp" : PO.potential1_qb , "gauss": PO.potential1_qb , "2imp" : PO.potential2_qb , "2gauss" : PO.potential2_qb}
  }
  return d

def allowed_envmode():
  """Returns the dictionary of supported env_mode and the corresponding
    mandatory input and envelope function to be used"""
  d = {
    "off"    :[["N"  , "w1"] , EN.off] , 
    "const"  :[["F1" , "w1"], EN.const] , 
    "singimp":[["F1" , "w1" , "t0" , "t1"], EN.sing_imp] , 
    "gauss"  :[["F1" , "w1" , "t0" , "sigma1"], EN.sing_gauss] ,
    "2imp"   :[["F1" , "F2", "w1" , "w2" , "t0" , "t1" , "t00" , "t11"], EN.two_imp] , 
    "2gauss" :[["F1" , "F2" , "w1" , "w2" , "t0" , "t1" , "sigma1" , "sigma2"], EN.two_gauss] 
    }
  return d
