[PDF page 1 image attached. Read this image directly to extract content.]

Protocolo E | Uso restrito a medicao contratada pag. 1
PROTOCOLO DE MEDICAO E
Caracterizacao de Detector de Limiar de RF (Comparador de Alta Velocidade)
Documento independente — nao requer conhecimento de outros protocolos

Objetivo
Caracterizar a resposta de um circuito detector baseado em diodo Schottky (HSMS-2860 ou equivalente) seguido de
comparador de alta velocidade (ADCMP601 ou equivalente) quando excitado por pulsos de RF de amplitude variavel.
Circuito sob teste
• Entrada RF → capacitor de acoplamento 100 pF → diodo HSMS-2860 → rede RC (1 kOhm + 10 nF) → entrada
nao-inversora do ADCMP601.
• Limiar (Vth) ajustavel entre 0,3 V e 0,6 V (meta nominal 0,4 V).
• Saida digital do comparador monitorada por contador ou logica de aquisicao (Arduino Nano, FPGA ou osciloscopio
digital).
Procedimento
Aplicar pulsos de amplitude conhecida (0,2 V a 1,5 V de pico) na entrada RF.
Para cada amplitude, registrar se o comparador dispara (saida vai a nivel alto).
Determinar o limiar efetivo de deteccao (menor amplitude que produz disparo consistente).
Medir a taxa de falsos positivos com a entrada terminada em 50 Ohm (sem sinal).
Medir a taxa de falsos negativos para amplitudes 20 % acima do limiar.
Variar o limiar Vth e repetir os itens 3–5.
Entregaveis
• Curva de probabilidade de deteccao vs amplitude de entrada (para Vth = 0,4 V).
• Taxa de falsos positivos (eventos/s) com entrada terminada.
• Largura minima de pulso que ainda e detectada de forma confiavel.
• Foto do circuito e do setup.
Este protocolo caracteriza apenas o front-end de deteccao. Nao envolve a linha de transmissao longa, multiplos elementos controlados
nem qualquer sequencia temporal especifica de excitacao.
