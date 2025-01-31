import numpy as np

def off(N , ti , tf , F1 , F2 , t0 , t1 , sigma1 , sigma2 , t00 , t11):
  E = np.zeros((N+1,2))
  return E

def const(N , ti , tf , F1 , F2 , t0 , t1 , sigma1 , sigma2 , t00 , t11):
  E = np.zeros((N+1,2))
  E[:, 0] = F1 
  return E

def sing_imp(N , ti , tf , F1 , F2 , t0 , t1 , sigma1 , sigma2 , t00 , t11):
  E = np.zeros((N+1,2))
  t = np.linspace(ti , tf , N+1)
  dt = t[1]
  i = int((t0-ti)/(dt))
  f = int((t1-ti)/(dt))
  E[i:f,0] = F1
  return E

def sing_gauss(N , ti , tf , F1 , F2 , t0 , t1 , sigma1 , sigma2 , t00 , t11):
  E  = np.zeros((N+1,2))
  t  = np.linspace(ti , tf , N+1)
  dt = t[1]

  E[:,0]  = F1 / (np.sqrt(2.0 * np.pi) * sigma1) * np.exp(-np.power((t - t0)*10**(6) / sigma1, 2.0) / 2)
  
  return E

def two_imp(N , ti , tf , F1 , F2 , t0 , t1 , sigma1 , sigma2 , t00 , t11):
  E1 = np.zeros(N+1)
  E2 = np.zeros(N+1)
  E  = np.zeros((N+1,2))
  t = np.linspace(ti , tf , N+1)
  dt = t[1]

  i = int((t0-ti)/(dt))
  f = int((t1-ti)/(dt))
  ii = int((t00-ti)/dt)
  ff = int((t11-ti)/dt)
  E[i:f,0]   = F1
  E2[ii:ff,1] = F2

  return E

def two_gauss(N , ti , tf , F1 , F2 , t0 , t1 , sigma1 , sigma2 , t00 , t11):
  E  = np.zeros((N+1,2))
  t  = np.linspace(ti , tf , N+1)
  dt = t[1]

  E[:,0]  = F1 / (np.sqrt(2.0 * np.pi) * sigma1) * np.exp(-np.power((t - t0)*10**(6) / sigma1, 2.0) / 2)
  E[:,1]  = F2 / (np.sqrt(2.0 * np.pi) * sigma2) * np.exp(-np.power((t - t1)*10**(6) / sigma2, 2.0) / 2)

  return E

