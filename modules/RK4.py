#Code that implements the 4th order Runge Kutta method for the ququart and qubit 
#systems with a given potential and envelope function.

#import python packages
import numpy as np
from   numba import njit , complex64 , complex128

#from qqEvol.modules impoPotentials import potential1_qb , potential1_qq , potential2_qb , potential2_qq

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

  V , E    = potential(t[0] , dt , wr , wl  , envelope , D , env_in)
  E_out[0] = E[2]
  i              = 1 

  #RK4 cycle
  for j in range(1 , N+1):
  
      V , E  = potential(t[j-1] , dt , wr , wl  , envelope , D , env_in)
      
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

          psif[: , i]   = psi0
          t_out[i]      = t[j]
          E_out[i]      = E[2]

          i = i + 1
     
  psiff = np.column_stack((psif[0,:] , psif[1,:] , psif[2,:] , psif[3,:]))
  return psiff , t_out , E_out

#njit
def rk4_qb(psi0 , wr , wl , envelope , env_in , potential , ti , tf , N , S , D ):
    """Function that performs the time evolution with RK4 method usign potential_qb"""
   #conversion of Rabi frequencies in the form accepted by potential_qb
    
    if "potentia1" in potential:
      print("ciao")
      wrr = np.zeros(5 , dtype = complex) 
      w1  = env_in[1]

      wrr[0]  = (wr[1] + im*wr[2])*0.5
      wrr[1]  = wr[0] + wr[3]
      wrr[2]  = wr[0] - wr[3]
      wrr[3]  = w1 - wl[0]
      wrr[4]  = w1 + wl[0]
    else:
      
      w1  = env_in[2]
      w2  = env_in[3]
      
      wrr = np.zeros((5,2) , dtype = complex)
      wrr[0,0]  = (wr[1] + im*wr[2])*0.5
      wrr[1,0]  = wr[0] + wr[3]
      wrr[2,0]  = wr[0] - wr[3]
      wrr[3,0]  = w1 - wl[0]
      wrr[4,0]  = w1 + wl[0]

      wrr[0,1]  = (wr[1] + im*wr[2])*0.5
      wrr[1,1]  = wr[0] + wr[3]
      wrr[2,1]  = wr[0] - wr[3]
      wrr[3,1]  = w2 - wl[0]
      wrr[4,1]  = w2 + wl[0]

  
   #definition of time array
    t = np.linspace(ti , tf , N+1)
    dt = t[1]
    #assignement of RK coefficients
    K0 =  np.zeros(D , dtype = complex)
    K1 =  np.zeros(D , dtype = complex)
    K2 =  np.zeros(D , dtype = complex)
    K3 =  np.zeros(D , dtype = complex)
    #check if the number of points saved on the output file
    if N%S != 0 :
        a     = int(N/S)+2
    else:
        a     = int(N/S)+1
    
    #assign variables to store output data
    t_out  = np.zeros(a)
    psif   = np.zeros((D , a) , dtype = complex)
    E_out  = np.zeros(a)

    #load the initial condition on output data
    psif[: , 0]    = psi0
    t_out[0]       = t[0] 

    V , E    = potential(t[0] , dt , wrr , envelope , D , env_in)
    E_out[0] = E[2]
    i        = 1 

   #RK4 cycle
    for j in range(1 , N+1):
    
        V  = potential(t[j-1] , dt , wrr , envelope , D , env_in)
        
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
            psif[: , i]   = psi0
            t_out[i]      = t[j]
            E_out[i]      = E[2]
            
            i = i + 1
   
    psiff = np.column_stack((psif[0,:] , psif[1,:]))
    return psiff , t_out , E_out

