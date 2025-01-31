##Functions to check if the input data refer to supported dimensions and modes and return the correspondind functions to use##
#
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
    mode_error = "Envelope function mode not supported"
    raise TypeError(mode_error)
  return envelope , potential
#
