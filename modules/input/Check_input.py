##Functions to check if the input data refer to supported dimensions and modes and return the correspondind functions to use##
#
def check_qbmode(data , allowed_qbmode , mand_input):
  if "qb_mode" in data:
    if data["qb_mode"] in allowed_qbmode:
      mand_input.append(allowed_qbmode[data["qb_mode"]][1])
    else:
      raise ValueError(f"Speciefied qbmode {data["qb_mode"]} not supported")
  else:
    data["qb_mode"] = "off"
  
  return data ,  allowed_qbmode[data["qb_mode"]][0] , mand_input , allowed_qbmode[data["qb_mode"]][2]

def check_dimensions(data , allowed_dimensions , mand_input):
  if data["qb_mode"] == "off":
    if data["D"] in allowed_dimensions:
      mand_input.append(allowed_dimensions[data["D"]])
    else:
      raise ValueError(f"Number of dimensions {data["D"]} not supported")
  else:
    raise ValueError(f"Missing mandatory input data D")
  
  return mand_input

def check_mandin(data , mand_input):
  for key in mand_input:
    if key not in data:
      raise ValueError(f"Missing mandatory input data {key}")
    
def check_envelope(data , allowed_envelope , mand_input ):
  if data["env_mode"] not in allowed_envelope:
    raise ValueError(f"Specified envmode {data["env_mode"]} not supported")
  else:
    for key in allowed_envelope[data["env_mode"]][0]:
        mand_input.append(key)

  return allowed_envelope[data["env_mode"]][1] , mand_input




    









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



