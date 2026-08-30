[PDF page 1 image attached. Read this image directly to extract content.]

Protocolo C | Uso restrito a medicao contratada pag. 1
PROTOCOLO DE MEDICAO C
Isolamento e Acoplamento Residual entre Descontinuidades em Linha de Transmissao
Documento independente — nao requer conhecimento de outros protocolos

Objetivo
Quantificar o acoplamento eletromagnetico residual (crosstalk) entre tres posicoes fixadas ao longo de um canal de
transmissao reto de 250 mm, quando cada posicao contem uma descontinuidade reativa (varactor ou equivalente passivo).
Configuracao mecanica
• Canal de Al 6061 250 × 40 × 20 mm (mesmo do Protocolo A).
• Tres rebaixos para PCB de 20 × 15 mm localizados nos centros aproximados:
Posicao 1: 60 mm a partir da extremidade de entrada
Posicao 2: 125 mm
Posicao 3: 190 mm
• Em cada rebaixo instala-se uma PCB identica a do Protocolo B (ou um short/open passivo equivalente).
• Distancia nominal entre centros ≈ 65 mm.
Procedimento
Instalar as tres PCBs. Polarizar todas em 0 V (ou deixar flutuando se passivas).
Medir S-parameters de ponta a ponta (porta 1 na entrada, porta 2 na saida).
Para isolamento local: usar sonda de campo proximo ou segundo VNA para medir acoplamento entre PCB adjacentes
(se disponivel).
Alternativa pratica: polarizar apenas uma PCB em 0 V (reflexao maxima) e as outras em 5 V (transmissao) e observar a
variacao de S11/S21.
Repetir para cada combinacao relevante de estados (pelo menos 4 combinacoes).
Meta de engenharia
Isolamento desejavel entre elementos adjacentes: melhor que –40 dB na banda 1–2 GHz. Valores piores que –30 dB
devem ser reportados com destaque.
Entregaveis
• Arquivos .s2p para cada combinacao de estados testada.
• Tabela de isolamento estimado (dB) entre pares de posicoes.
• Comentario qualitativo sobre a presenca ou ausencia de ressonancias entre elementos.
Este protocolo avalia apenas acoplamento residual entre descontinuidades. Nao envolve geracao de pulsos, deteccao digital nem
sequencias temporais.
