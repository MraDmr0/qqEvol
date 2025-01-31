##Functio that starts the RK4 calculation
def evolution(rk , envelope , potential , data):
  #extract initial condition and frequencies
  psi_in , wr , wl , data = rk[1](data)
  #compute envelope function
  E_in = envelope(int(data["N"]) , float(data["ti"] ) , float(data["tf"] ) , float(data["F1"] ) , float(data["F2"] ) , float(data["t0"] ) , float(data["t1"] ) , float(data["sigma1"]), float(data["sigma2"]), float(data["t00"]) , float(data["t11"]))
  #call rk4
  psi_out , t_out , E_out = rk[0](psi_in , wr , wl , E_in , potential , float(data["ti"]) , float(data["tf"]) , int(data["N"]) , int(data["S"]) , float(data["w1"]), float(data["w2"]))
  return psi_out , t_out , E_out
#







  