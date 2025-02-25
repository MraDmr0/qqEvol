from itertools import chain
import sys


#

class Check_input:
    
    def __init__(self , data , all_qbmode , all_dim , all_env, all_pot): 
        
        self.data       = data
        self.all_qbmode = all_qbmode
        self.all_dim    = all_dim
        self.all_env    = all_env
        self.all_pot    = all_pot
        self._key       = []
        self._value     = []
        self.env_in     = []
        self.env        = None
        self.pot        = None
        self.rk         = None
        self.setin      = None

    def check_dim(self):
        if "D" in self.data:
            if str(self.data["D"]) in self.all_dim:
                self._key += [(self.all_dim[str(self.data["D"])])]
            else:
                 print(f"Error: the specified value '{self.data['D']}' for 'D' is not supported")
                 sys.exit(1)
        else:
            print(f"Error: missing mandatory input data 'D'")
            sys.exit(1)
        
    def check_qbmode(self):
        if "qb_mode" not in self.data:
            self.data["qb_mode"] = "off"

        if self.data["qb_mode"] not in self.all_qbmode:
            print(f"Error: the specified value '{self.data['qb_mode']}' for 'qb_mode' is not supported")
            sys.exit(1)
        
        self._key   += [(self.all_qbmode[str(self.data["qb_mode"])][0])]
        self.setin  = self.all_qbmode[str(self.data["qb_mode"])][1]
        self.rk     = self.all_qbmode[str(self.data["qb_mode"])][2]

        if self.data["qb_mode"] == "off":
            self.check_dim()
        else:
           self.data["D"] = 2

    def check_env(self):
        if "env_mode" in self.data:
            if str(self.data["env_mode"]) in self.all_env:
                self._key   += [(self.all_env[str(self.data["env_mode"])][0])]
                self.env_in += [(self.all_env[str(self.data["env_mode"])][0])]
                self.env     = self.all_env[str(self.data["env_mode"])][1]
                
            else:
              print(f"Error: the specified value '{self.data['env_mode']}' for 'env_mode' is not suppoprted")
              sys.exit(1)
        else:
            print(f"Error: missing mandatory input 'env_mode'") 
            sys.exit(1)

    def check_pot(self):
        if self.data["qb_mode"] in self.all_pot:
            if self.data["env_mode"] in self.all_pot[str(self.data["qb_mode"])]:
                self.pot = self.all_pot[str(self.data["qb_mode"])][str(self.data["env_mode"])]

    def check_data(self):
        self._key  = list(chain(*self._key))
        self.env_in = list(chain(*self.env_in))
        for key in self._key:
            if key in self.data:
                self._value += [(self.data[key])]
            else:
                print(f"Error: missing mandatory input '{key}'")       
                sys.exit(1)  
        
        i = 0
        for key in self.all_env[str(self.data["env_mode"])][0]:
          self.env_in[i] = float(self.data[key])
          i +=1