##Functions to check if the input data refer to supported dimensions and modes and return the correspondind functions to use##
#
def check_data(data , mand_data , std_data , env_data , pot_data , rk_data):
  for key in mand_data:
    if key not in data:
      data_error = "Missing data {key}"
      raise TypeError(data_error)
  
  for key in std_data:
    if key not in data:
      data[key] = std_data[key]
  
  for key in rk_data:
    if key not in data:
      data_error = "Missing data {key}"
      raise TypeError(data_error)

  for key in env_data:
    if key not in data:
      data_error = "Missing data {key}"
      raise TypeError(data_error)
    
  for key in pot_data:
    if key not in data:
      data_error = "Missing data {key}"
      raise TypeError(data_error)
    

def check_dimensions(D , allowed_dimensions , allowed_rk):
  #check if input dimension in supprted ones
  if D in allowed_dimensions:
    print("Simulation of " + allowed_dimensions[D] + " system\n" )
    #return the corresponding rk4 function
    rk = allowed_rk[D]
  #error message
  else:
    dimensional_error = "Number of energy levels not supported"
    raise TypeError(dimensional_error)
  return rk
#
def check_envelope(D , mode , allowed_envelopes , allowed_potentials):
  #check if input mode in supported ones
  if str(mode) in allowed_envelopes:
    #return the corresponding envelope and potential functions
    envelope   = allowed_envelopes[mode]
    potential  = allowed_potentials[mode][D]
  #error message
  else:
    mode_error = "Envelope function mode not supported {mode}"
    raise TypeError(mode_error)
  return envelope , potential
#
def check_pot(qb_mode , allowed_qbmode):
  if str(qb_mode) not in allowed_qbmode:
    qb_error = "qbmode not supported {qb_mode}"
    raise TypeError(qb_error)



