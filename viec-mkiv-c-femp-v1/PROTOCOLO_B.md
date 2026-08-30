[PDF page 1 image attached. Read this image directly to extract content.]

Protocolo B | Uso restrito a medicao contratada pag. 1
PROTOCOLO DE MEDICAO B
Caracterizacao de Descontinuidade RF Controlada por Tensao (Varactor)
Documento independente — nao requer conhecimento de outros protocolos

Objetivo
Caracterizar o comportamento de reflexao/transmissao de uma descontinuidade formada por um varactor (diodo de
capacitancia variavel) inserido em uma trilha de 50 Ohm, em funcao da tensao de polarizacao DC (0 a 5 V).
Dispositivo sob teste (DUT)
• PCB FR4 0,8 mm, dimensoes 20 mm × 15 mm, acabamento ENIG.
• Trilha 50 Ohm de 1,5 mm de largura.
• Gap de 0,5 mm entre a trilha e o pad do varactor.
• Varactor: Skyworks SMV1405 (ou equivalente C = 0,6–2,4 pF @ 0–5 V).
• Bias-tee discreto: C=100 pF (DC-block), L=100 nH (RF-choke), R=10 kOhm, C_bypass=10 nF.
• Conectores SMA IN e SMA OUT.
• Terminal de polarizacao DC (0–5 V) isolado do caminho RF.
Instrumentacao
• VNA 0,5–3 GHz calibrado.
• Fonte DC precisa 0–5 V (resolucao 10 mV ou melhor).
• Multimetro para confirmar tensao no pad do varactor.
Procedimento
Calibrar VNA.
Conectar DUT entre portas 1 e 2; polarizacao DC desconectada inicialmente.
Aplicar Vbias = 0,0 V e registrar S11 e S21 (0,5–3 GHz).
Repetir para Vbias = 0,5 / 1,0 / 1,5 / 2,0 / 2,5 / 3,0 / 3,5 / 4,0 / 4,5 / 5,0 V.
Em cada ponto, anotar se o comportamento e predominantemente reflexivo ou transmissivo na banda 1–2 GHz.
Extrair a capacitancia efetiva aproximada a partir do modelo de descontinuidade (opcional, se o medidor tiver software de
de-embedding).
Criterios de interesse (nao sao pass/fail rigidos)
• Em Vbias ≈ 0 V espera-se reflexao elevada (capacitancia maxima ≈ 2,3 pF).
• Em Vbias ≈ 5 V espera-se transmissao elevada (capacitancia minima ≈ 0,6 pF).
• Transicao deve ocorrer de forma monotona com a tensao.
• Nao ha meta numerica obrigatoria neste protocolo; o objetivo e mapear a curva completa.
Entregaveis
• Arquivos .s2p para cada valor de Vbias (nomear: S_0V0.s2p, S_0V5.s2p, … S_5V0.s2p).
• Tabela resumo: Vbias | |S11| @ 1,5 GHz | |S21| @ 1,5 GHz.
• Grafico |S11| e |S21| vs Vbias em 1,5 GHz.
• Foto do PCB e do setup.
Este protocolo caracteriza um unico elemento reativo controlado por tensao. Nao envolve multiplos dispositivos, logica digital nem
sequencias temporais.
