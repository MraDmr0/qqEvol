import numpy as np
from numba import njit , complex128

#definition of local variables (meV s)
h_bar = 6.582119569E-13
im = 1j
#
@njit
def potential1_qb(t0 , dt , wr1 , wr2, w1 , w2 , E_in ):
    """
    Function that computes the qubit potential at the three times needed for the RK4 algorithm.
    
    wr is intended as the following array:

    wr[0]  = (wr[1] + im*wr[2])*0.5
    wr[1]  = wr[0] + wr[3]
    wr[2]  = wr[0] - wr[3]
    wr[3]  = w - wl
    wr[4]  = w + wl
    
    The Larmor frequency is the difference between the two states
    """
    #Variables assignement
    V    = np.zeros((3,2,2) , dtype = complex128)

    t = np.array([t0 , t0+0.5*dt , t0+dt])
    
    for k in range(3):
      V[k,1,1] = wr1[1]*np.cos(w1*t[k])
      V[k,1,0] = wr1[0].conjugate()*(np.exp(-im*t[k]*wr1[3])+np.exp(im*t[k]*wr1[4]))
      V[k,0,1] = wr1[0]*(np.exp(im*t[k]*wr1[3])+np.exp(-im*t[k]*(wr1[4])))   
      V[k,0,0] = wr1[2]*np.cos(w1*t[k])
    V *= -im*E_in[0]
    
    return V


@njit
def potential2_qb(t0 , dt , wr1 , wr2, w1 , w2 , E_in):
    """
    Function that computes the qubit potential at the three times needed for the RK4 algorithm.
    
    wr is intended as the following array:

    wr[0]  = (wr[1] + im*wr[2])*0.5
    wr[1]  = wr[0] + wr[3]
    wr[2]  = wr[0] - wr[3]
    wr[3]  = w - wl
    wr[4]  = w + wl
    
    The Larmor frequency is the difference between the two states
    """
    #Variables assignement
    V1    = np.zeros((3,2,2) , dtype = complex128)
    V2    = np.zeros((3,2,2) , dtype = complex128)

    t = np.array([t0 , t0+0.5*dt , t0+dt])
    
    for k in range(3):
      V1[k,1,1] = wr1[1]*np.cos(w1*t[k])
      V1[k,1,0] = wr1[0].conjugate()*(np.exp(-im*t[k]*wr1[3])+np.exp(im*t[k]*wr1[4]))
      V1[k,0,1] = wr1[0]*(np.exp(im*t[k]*wr1[3])+np.exp(-im*t[k]*(wr1[4])))   
      V1[k,0,0] = wr1[2]*np.cos(w1*t[k])
    V1 *= -im*E_in[0]

    for k in range(3):
      V2[k,1,1] = wr2[1]*np.cos(w2*t[k])
      V2[k,1,0] = wr2[0].conjugate()*(np.exp(-im*t[k]*wr2[3])+np.exp(im*t[k]*wr2[4]))
      V2[k,0,1] = wr2[0]*(np.exp(im*t[k]*wr2[3])+np.exp(-im*t[k]*(wr2[4])))   
      V2[k,0,0] = wr2[2]*np.cos(w2*t[k])
    V2 *= -im*E_in[1]
    
    return V1+V2


@njit
def potential1_qq(t0 , dt , wr , wl , envelope , D , env_in ):
  """Function that computes the qubit potential at the three times needed for the RK4 algorithm.
     The Rabi frequencies are given in matrix form, while Larmor frequencies are intended as the energy of each level in meV"""

  V   = np.zeros((3 , D , D) , dtype = complex128)
  t   = np.array([t0 , t0+dt*0.5 , t0+dt])
  
  E   = np.array(3)
  E   = envelope(t , env_in)
  w1  = env_in[0]
  for k in range(3):
    for i in range(D):
      for j in range(D):
        V[k,i,j] = wr[i,j]*np.exp((im/h_bar)*(wl[i] - wl[j])*t[k])
  
    V[k,:,:] *= -im*E[0,k]*np.cos(w1*t[k])

  return V , E[0]

@njit
def potential2_qq(t0 , dt , wr , wl , w1 , w2 , envelope , D , env_in):
  """Function that computes the qubit potential at the three times needed for the RK4 algorithm.
     The Rabi frequencies are given in matrix form, while Larmor frequencies are intended as the energy of each level in meV"""
  V   = np.zeros((3,D,D)  , dtype = complex128)
  V1  = np.zeros((3,D,D) , dtype = complex128)
  V2  = np.zeros((3,D,D) , dtype = complex128)
  t   = np.array([t0 , t0+dt*0.5 , t0+dt])

  E   = np.array((2,3))
  E   = envelope(t , env_in)
  w1  = env_in[0]
  w2  = env_in[1]

  
  for k in range(3):
    for i in range(D):
      for j in range(D):
        V[k,i,j] = wr[i,j]*np.exp((im/h_bar)*(wl[i] - wl[j])*t[k])
  
    V1[k,:,:] = -im*E[0,k]*np.cos(w1*t[k])*V[k,:,:]
    V2[k,:,:] = -im*E[1,k]*np.cos(w2*t[k])*V[k,:,:]

    E[0,0] = E[0,0] + E[1,0]

  return V1 + V2 , E[0,0]


