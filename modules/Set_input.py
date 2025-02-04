##Functions to set input data
import numpy as np  
#

def set_input_qb(data):

  psi    = np.array([float(data["psi0"]) ,float(data["psi1"])] , dtype = complex)
  nomr   = np.sqrt(np.linalg.norm(psi))
  psi    = psi/nomr
  #
  wr     = np.array([float(data["wr00"]) , float(data["wr01"]) , float(data["wr02"]) , float(data["wr03"])] , dtype = complex)
  wl     = np.array([float(data["wl0"])])
  #
  return psi , wr , wl

def set_input(data):
  psi = np.zeros(int(data["D"]) , dtype = complex)
  wl  = np.zeros(int(data["D"]))
  wr  = np.zeros((int(data["D"]) , int(data["D"])) , dtype = complex)
  
  for i in range(int(data["D"])):
    psi[i] = float(data[str("psi"+str(i))])
    wl[i]  = float(data[str("wl"+str(i))])
    for j in range(int(data["D"])):
      wr[i,j] = float(data[str("wr"+str(i)+str(j))])
  
  nomr   = np.sqrt(np.linalg.norm(psi))
  psi    = psi/nomr

  return psi , wr , wl 

