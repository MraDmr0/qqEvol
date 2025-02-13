#Code that implements the 4th order Runge Kutta method for the ququart and qubit 
#systems with a given potential and envelope function.

#import python packages
import numpy as np
from   numba import njit , complex64 , complex128

#imaginary unit
im = 1j

@njit
def rk4_qq(psi0 , wr , wl , envelope , env_in , potential , ti , tf , N , S , D ):
  #definition of time array
  t  = np.linspace(ti , tf , N+1)
  dt = t[1]
  
  #definition RK coefficients
  K0 =  np.zeros(D , dtype = complex128)
  K1 =  np.zeros(D , dtype = complex128)
  K2 =  np.zeros(D , dtype = complex128)
  K3 =  np.zeros(D , dtype = complex128)
  
  #check the number of points to be saved on the output file
  if N%S != 0 :
      a     = int(N/S)+2
  else:
      a     = int(N/S)+1

  #define variables to store output data
  t_out  = np.zeros(a)
  psif   = np.zeros((D , a) , dtype = complex128)
  E_out  = np.zeros(a)

  #load the initial condition on output data
  psif[: , 0]    = psi0
  t_out[0]       = t[0]
 
  i              = 1 
  
  #RK4 cycle
  for j in range(1 , N+1):
  
      V , E_out  = potential(t[j-1] , dt , wr , wl  , envelope , D , env_in)
      
      K0 = np.dot(V[0] , psi0)
      K1 = np.dot(V[1] , psi0 + 0.5*dt*K0)
      K2 = np.dot(V[1] , psi0 + 0.5*dt*K1)
      K3 = np.dot(V[2] , psi0 + dt*K2)

      psi0 = psi0 + dt/6*(K0 + 2*K1 + 2*K2 + K3)

      #renormalizaton of solution
      norm   = np.sqrt(np.dot(psi0.conjugate() , psi0))
      psi0   = psi0/norm

      #append to output data
      if j%S == 0 or j == N:

          psif[: , i] = psi0
          t_out[i]    = t[j]
          if "potential1" in str(potential):
            E_out[i,0]  = E_out[0,0]
          else:
            E_out[i,0]  = E_out[0,0] + E_out[0,1]
          
          i = i + 1
  
  psiff = np.column_stack((psif[0,:] , psif[1,:] , psif[2,:] , psif[3,:]))
  return psiff , t_out , E_out

@njit
def rk4_qb(psi0 , wr , wl , envelope , env_in , potential , ti , tf , N , S , D ):
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

