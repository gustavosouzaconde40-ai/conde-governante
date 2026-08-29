# Casamento 50 -> 376.73 ohm

L_match = (Zvac - Z0)/(2*pi*f) = (376.73-50)/(2*pi*1e9) ~ 52 nH
C_match = 1/(2*pi*f*Zvac) ~ 0.42 pF

Medicao: S11 < -20dB @ 1GHz
Positive-real: Re[Zmeas] > 0
Crouzeix: ||p(A)|| <= 2 * maxW
