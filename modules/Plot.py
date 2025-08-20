import numpy as np
import matplotlib.pyplot as plt

def plot(prefix , D):
  """Function that plots the computed square moduli of the two components of the wavefunction, 
  stored in psi_preix.txt  and t_prefix, as a function of time"""
  
  #load wfc and time axis
  psi = np.loadtxt("psi_" +prefix+".txt" , dtype = complex)
  t   = np.loadtxt("t_"   +prefix+".txt" , dtype = float)
  Eout   = np.loadtxt("envelope_"   +prefix+".txt" , dtype = float)
  #conversion to us
  t   = t*10**(6)
  #creation of the figure
  fig , ax = plt.subplots(1 , 1 , figsize = (8,8) ,  dpi = 300)
  #append data to the figure
  ax.plot(t , abs(psi)[:,0]**2 , label = r"State $|0\rangle$")
  ax.plot(t , abs(psi)[:,1]**2 , label = r"State $|1\rangle$")

  if D == 4:
    ax.plot(t , abs(psi)[:,2]**2 , label = r"State $|2\rangle$")
    ax.plot(t , abs(psi)[:,3]**2 , label = r"State $|3\rangle$")
  
  ax.plot(np.nan , ls = "--", c = "grey", alpha = 0.7,  label = "Envelope function" )
  ax.legend(loc = 0)

  ax1 = ax.twinx()
  ax1.plot(t , Eout , ls = "--", c = "grey", alpha = 0.7)
  
  #personalization
  ax.set_xlabel(r"Time $(\mu s)$")
  ax.set_ylabel("r$|\Psi|^2$")
  ax1.set_ylabel("Envelope intensity")

  #save fiugre
  plt.savefig(prefix+".png")

