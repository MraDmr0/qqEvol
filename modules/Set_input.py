##Functions to set input data
import numpy as np  
#
def optional_pairs(data , allowed_data , allowed_pairs):
  """Check if both data in the pair are give in input file; otherwise they are set to be equal"""

  if allowed_pairs:
    for var1 , var2 in allowed_pairs:
      if var1 in data and var2 not in data:
        data[var2] = data[var1]
      if var2 in data and var1 not in data:
        data[var1] = data[var2]
      if var1 not in data and var2 not in data:
        data[var1] = 0
        data[var2] = 0

  for element in allowed_data:
    if element not in data:
      data[element] = 0
  return data
#
def set_input_qb(data):

  psi    = np.array([float(data["psi0"]) ,float(data["psi1"])] , dtype = complex)
  nomr   = np.sqrt(np.linalg.norm(psi))
  psi    = psi/nomr
  #
  wr     = np.array([float(data["wr00"]) , float(data["wr01"]) , float(data["wr02"]) , float(data["wr03"])] , dtype = complex)
  wl     = np.array([float(data["wl0"])])
  #
  # if data["w2"] == None:
  #   data["w2"] = data["w1"]
  # if data["F2"] == None:
  #   data["F2"] = data["F1"]
  # if data["sigma2"] == None:
  #   data["sigma2"] = data["sigma1"] 
  # #
  # for key , values in data.items():
  #   if data[key] == None:
  #     del data[key]
  # #
  return psi , wr , wl , data

def set_input_qq(data):
  psi    = np.array([float(data["psi0"]) ,float(data["psi1"]) ,float(data["psi2"]) ,float(data["psi3"])] , dtype = complex)
  nomr   = np.sqrt(np.linalg.norm(psi))
  psi    = psi/nomr

  wr   = np.array([[float(data["wr00"]) , float(data["wr01"]) , float(data["wr02"]) , float(data["wr03"])],
                   [float(data["wr10"]) , float(data["wr11"]) , float(data["wr12"]) , float(data["wr13"])],
                   [float(data["wr20"]) , float(data["wr21"]) , float(data["wr22"]) , float(data["wr23"])],
                   [float(data["wr30"]) , float(data["wr31"]) , float(data["wr32"]) , float(data["wr33"])]] , dtype = complex)
  
  wl   = np.array([float(data["wl0"] ), float(data["wl1"] ), float(data["wl2"] ), float(data["wl3"])])

  # if data["w2"] == None:
  #   data["w2"] = data["w1"]
  # if data["F2"] == None:
  #   data["F2"] = data["F1"]
  # if data["sigma2"] == None:
  #   data["sigma2"] = data["sigma1"] 

  # for key , values in data.items():
  #   if data[key] == None:
  #     data[key] = 0

  return psi , wr , wl , data