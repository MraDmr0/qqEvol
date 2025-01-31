# qqEvol_2.0

## Description of the package

This Python package allows to simulate the time evolution of a two (qubit) or four (ququart) level systems under the action of an oscillating scalar potential. The system is specified through its Larmor frequencies $\omega_{L}$ (energy levels), while the potential is determined by its oscillating frequency $\omega$, the Rabi frequencies $\omega_{i,j}$ that couples the different levels and an enevelope function. The time integration is carried out thanks to the standard Runge-Kutta fourth order algorithm optimized thanks to the numba package. 

```math
V(t)_{i,j} = -i F(t) cos( \omega t ) \omega _{i,j} \exp\left(-i( \omega ^ {j}_{L}-\omega^{i}_{L})t\right)
```
## Usage

The main calculation can be started from command line:

\$ python qqE.py qq.in > qq.out

where qq.in and qq.out are the input and output files respectively. The script is going to produce the files "psi_qq", "t_qq" and "envelope_qq" that contain the wavefucntions, the array of times and the points of the envelope function. The obtained resutls can be plotted with the "Plot.py" routine.

### Input file desctiption

#### Mandatory
- prefix                = name used for output files
- D                     = number of energy levels
- ti                    = initial time (s)
- tf                    = final time (s)
- N                     = number of time steps   
- S                     = number of interations between each result save
- pis0...psi3           = initial occupation of each state
- wl0...wl3             = Larmor frewuencies of the system. For the two level system there is only one and is given in (Hz). The four level
                        systems needs four values in (meV). 
- w00...w33             = Rabi frequencies of the system. For the two level system only use w00...w03 and intende as w_+
- w1                    = frequency of the first (or only) potential impulse
- F1                    = scaling factor of the potential
- mode                  = specifies the form of the envelope function
                        - "off"     : no potential
                        - "const"   : constant potential in [ti , tf]
                        - "singimp" : one sqare impulse of frequency "w1" in [t0 , t1]
                        - "gauss"   : one gaussian impulse of frequency "w1", spreading "sigma1" and centered in "t0"
                        - "2imp"    : two square impulses in [t0 , t1] with frequency "w1" and in [t00 , t11] with frewuency "w2"
                        - "2gauss"  : two gaussian impulses of frequencies "w1" and "w2", centered in "t0" and "t1" with spreadings "sigma1" and  
                                      "sigma2" 

#### Optional
- t0                      = begin of first impulse if square, or center of the first gaussian impulse 
- t1                      = end of first impulse if square, or center of the second gaussian impulse 
- t00                     = begin of the second square impulse
- t11                     = end of the second square impulse
- sigma1                  = spreading of the first gaussian impulse
- w2     (default w1)     = frequency of the second potential impulse
- sigma2 (default sigma1) = spreading of the second gaussian impulse

## Coming next

The code needs to be formalized and reorganized in a more logical and user-friendly way and provided with proper handling of errors and exceptions.

Mario Di Mare, 31/01/2025
