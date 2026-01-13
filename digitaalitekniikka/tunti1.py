print(int('23',4))
print(int('1010',2))
#analoginen singnaali on 0-2 volttiin
#tasoja on 5
#mikä on kahden peräkkäisen tason ero volteissa?
import numpy as np
tasot = np.linspace(0,2,5)
print(tasot)
#pineni arvo on 0, suurin 5 volttia
#ABC, on 3 bittinen, eli 2 kantaisessa 1*2**0=2
#mikä on tasojen väli
bitit=3
vali2=5/(8-1)
print(vali2)
tasot2 = np.linspace(0,5, 2**bitit)
print(tasot2)
#arvo on 0-5,bitit on 10
#Mikä on taso numero 31 volttimäärä?
bitit2=10
tasojenmaara= 2**bitit2
tasot3 = np.linspace(0,5, tasojenmaara)
print(tasot3[31])
print('----------TAI---------------')
#väli on volttimäärä
vali3=5/(tasojenmaara-1)
print(vali3*31)