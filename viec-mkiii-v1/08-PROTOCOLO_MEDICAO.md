# Protocolo de Medicao VIEC-01

1. Calibrar VNA 1-2 GHz - SOLT
2. Medir S11 S21 da cavidade 50 ohm vazia
3. Inserir amostra / campo -> medir Zmeas = Z0*(1+S11)/(1-S11)
4. Calcular ratio = 376.73 / Zmeas
5. Verificar Crouzeix: numerical_range_bound(A) -> ||A|| <= 2*maxW
6. Se criterion = 2*maxW*Vin < 1.8V -> PASSOU
7. Registrar em CSV: f, S11, S21, Zmeas, ratio, maxW, norm2, passed
