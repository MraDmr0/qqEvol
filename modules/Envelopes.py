import numpy as np

def off(*args , **kwargs):
  E    = np.array(3)
  E[:] = 0
  
  return E

def const(t , env_in):
  
  F1   = env_in[0]
  E    = np.array(3)

  E[:] = F1 
  return E

def sing_imp(t, env_in):
  F1 = env_in[0]
  t0 = env_in[2]
  t1 = env_in[3]

  E = np.zeros(3)

  for i in range(3):
    if t[i] < t0 or t[i] > t1:
      E[i] = 0
    else:
      E[i] = F1

  return E

def sing_gauss(t, env_in):
  F1     = env_in[0]
  t0     = env_in[2]
  sigma1 = env_in[3]

  E  = np.zeros((3))

  E[:]  = F1 / (np.sqrt(2.0 * np.pi) * sigma1) * np.exp(-np.power((t[:] - t0)*10**(6) / sigma1, 2.0) / 2)
  
  return E

def two_imp(t, env_in):
  F1 = env_in[0]
  F2 = env_in[1]

  t0  = env_in[4]
  t1  = env_in[5]
  t00 = env_in[6]
  t11 = env_in[7]

  E  = np.zeros((3 , 2))

  for i in range(3):
    if t0 < t[i] < t1:
      E[i,0] = F1
    elif t00 < t[i] < t11:
      E[i,1] = F2

  return E

def two_gauss(t , env_in):
  F1 = env_in[0]
  F2 = env_in[1]

  t0     = env_in[4] 
  t1     = env_in[5]
  sigma1 = env_in[6]
  sigma2 = env_in[7]

  E  = np.zeros((3,2))

  E[:,0]  = F1 / (np.sqrt(2.0 * np.pi) * sigma1) * np.exp(-np.power((t[:] - t0)*10**(6) / sigma1, 2.0) / 2)
  E[:,1]  = F2 / (np.sqrt(2.0 * np.pi) * sigma2) * np.exp(-np.power((t[:] - t1)*10**(6) / sigma2, 2.0) / 2)

  return E

