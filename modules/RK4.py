import numpy as np
from numba import njit , complex64 , complex128
from Potentials import potential1_qb , potential2_qb , potential1_qq , potential2_qq
im = 1j

@njit
def rk4_qb(psi0 , wr , wl , E_in , potential , ti , tf , N , S , w1 , w2):
    """Function that performs the time evolution with RK4 method usign potential_qb"""
   #conversion of Rabi frequencies in the form accepted by potential_qb
    wrr1 = np.zeros(5 , dtype = complex64)
    wrr2 = np.zeros(5 , dtype = complex64)
    wrr1[0]  = (wr[1] + im*wr[2])*0.5
    wrr1[1]  = wr[0] + wr[3]
    wrr1[2]  = wr[0] - wr[3]
    wrr1[3]  = w1 - wl[0]
    wrr1[4]  = w1 + wl[0]
    
    wrr2[0]  = (wr[1] + im*wr[2])*0.5
    wrr2[1]  = wr[0] + wr[3]
    wrr2[2]  = wr[0] - wr[3]
    wrr2[3]  = w2 - wl[0]
    wrr2[4]  = w2 + wl[0]

   #definition of time array
    dt = (tf-ti)/N
    t = np.linspace(ti , tf , N+1)
    #assignement of RK coefficients
    K0 =  np.zeros(2 , dtype = complex128)
    K1 =  np.zeros(2 , dtype = complex128)
    K2 =  np.zeros(2 , dtype = complex128)
    K3 =  np.zeros(2 , dtype = complex128)
    #check if the number of points saved on the output file
    if N%S != 0 :
        a     = int(N/S)+2
    else:
        a     = int(N/S)+1
    #assign variables to store output data
    tff    = np.zeros(a)
    psif0  = np.zeros(a , dtype = complex128)
    psif1  = np.zeros(a , dtype = complex128)
    E_out   = np.zeros(a)
    #load the initial condition on output data
    psif0[0] = psi0[0]
    psif1[0] = psi0[1]
    tff[0]   = t[0]
    if "potential1" in str(potential):
      E_out[0]  = E_in[0,0]
    else:
      E_out[0] = E_in[0,0] + E_in[0,1]
    i          = 1

   #RK4 cycle
    for j in range(1 , N+1):
    
        V  = potential(t[j-1] , dt , wrr1 , wrr2, w1 , w2 , E_in[j-1,:])
        
        K0 = np.dot(V[0] , psi0)
        K1 = np.dot(V[1] , psi0 + 0.5*dt*K0)
        K2 = np.dot(V[1] , psi0 + 0.5*dt*K1)
        K3 = np.dot(V[2] , psi0 + dt*K2)

        psi0 = psi0 + dt/6*(K0 + 2*K1 + 2*K2 + K3)
        #renormalizaton of computed solution
        norm   = np.sqrt(np.dot(psi0.conjugate() , psi0))
        psi0   = psi0/norm

       #append to output data
        if j%S == 0 or j == N:

            psif0[i] = psi0[0]
            psif1[i] = psi0[1]
            tff[i]   = t[j]
            if "potential1" in str(potential):
              E_out[i]  = E_in[j,0]
            else:
              E_out[i] = E_in[j,0] + E_in[j,1]
            i = i + 1
   
    psiff = np.column_stack((psif0 , psif1))
    return psiff , tff , E_out


@njit
def rk4_qq(psi0 , wr , wl , E_in , potential , ti , tf , N , S , w1 , w2 ):
  #definition of time array
  dt = (tf-ti)/N
  t = np.linspace(ti , tf , N+1)
  
  #assignement of RK coefficients
  K0 =  np.zeros(4 , dtype = complex128)
  K1 =  np.zeros(4 , dtype = complex128)
  K2 =  np.zeros(4 , dtype = complex128)
  K3 =  np.zeros(4 , dtype = complex128)
  #check if the number of points saved on the output file
  if N%S != 0 :
      a     = int(N/S)+2
  else:
      a     = int(N/S)+1
  #assign variables to store output data
  tff    = np.zeros(a)
  psif0  = np.zeros(a , dtype = complex128)
  psif1  = np.zeros(a , dtype = complex128)
  psif2  = np.zeros(a , dtype = complex128)
  psif3  = np.zeros(a , dtype = complex128)
  E_out   = np.zeros(a)
  #load the initial condition on output data
  psif0[0] = psi0[0]
  psif1[0] = psi0[1]
  psif2[0] = psi0[2]
  psif3[0] = psi0[3]
  tff[0]   = t[0]
  if "potential1" in str(potential):
      E_out[0]  = E_in[0,0]
  else:
    E_out[0] = E_in[0,0] + E_in[0,1]
  i        = 1
  #RK4 cycle
  for j in range(1 , N+1):
  
      V  = potential(t[j-1] , dt , wr , wl , w1 , w2 , E_in[j-1,:] )
      
      K0 = np.dot(V[0] , psi0)
      K1 = np.dot(V[1] , psi0 + 0.5*dt*K0)
      K2 = np.dot(V[1] , psi0 + 0.5*dt*K1)
      K3 = np.dot(V[2] , psi0 + dt*K2)

      psi0 = psi0 + dt/6*(K0 + 2*K1 + 2*K2 + K3)
      #renormalizaton of computed solution
      norm   = np.sqrt(np.dot(psi0.conjugate() , psi0))
      psi0   = psi0/norm
      #append to output data
      if j%S == 0 or j == N:

          psif0[i] = psi0[0]
          psif1[i] = psi0[1]
          psif2[i] = psi0[2]
          psif3[i] = psi0[3]
          tff[i]   = t[j]
          if "potential1" in str(potential):
            E_out[i]  = E_in[j,0]
          else:
            E_out[i] = E_in[j,0] + E_in[j,1]
          i = i + 1
  
  psiff = np.column_stack((psif0 , psif1 , psif2 , psif3))
  return psiff , tff , E_out
