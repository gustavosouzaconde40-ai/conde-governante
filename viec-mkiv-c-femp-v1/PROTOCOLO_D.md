[PDF page 1 image attached. Read this image directly to extract content.]

Protocolo D | Uso restrito a medicao contratada pag. 1
PROTOCOLO DE MEDICAO D
Fidelidade de Pulso em Linha de Transmissao de Banda Larga
Documento independente — nao requer conhecimento de outros protocolos

Objetivo
Avaliar a distorcao, alargamento e ringing de pulsos de curta duracao (1 ns e 16 ns) apos percorrer um canal de
transmissao reto de 250 mm. O foco e a fidelidade temporal do envelope do pulso, nao a interpretacao logica.
Instrumentacao
• Gerador de formas de onda arbitrarias ou SDR capaz de sintetizar:
– Pulso Gaussiano de largura ≈ 1 ns (amostragem ≥ 1 GSPS preferivel)
– Pulso Raised-Cosine de largura ≈ 16 ns (amostragem ≥ 60 MSPS)
• Osciloscopio de tempo real ≥ 2 GHz de banda (ou sampling oscilloscope) com sonda ativa.
• Alternativa aceitavel: SDR receptor com taxa ≥ 100 MSPS + pos-processamento.
DUT
Canal de Aluminio 250 mm com fita central (mesmo do Protocolo A), com ou sem as descontinuidades do Protocolo B
instaladas. Reportar claramente qual configuracao foi usada em cada captura.
Procedimento
Injetar o pulso de 16 ns na entrada; capturar na saida (pelo menos 10 aquisicoes).
Injetar o pulso de 1 ns (se o hardware permitir); capturar na saida.
Medir: largura a meia altura (FWHM), tempo de subida 10–90 %, overshoot (%), ringing residual apos o pulso principal.
Repetir com as descontinuidades polarizadas em 0 V e em 5 V (se instaladas).
Registrar a atenuacao de amplitude pico-a-pico.
Entregaveis
• Capturas de tela ou arquivos de forma de onda (CSV / binary) da entrada e da saida.
• Tabela: FWHM_in, FWHM_out, overshoot, ringing, atenuacao (dB).
• Comentario sobre a presenca de precursores ou echos multiplos.
Este protocolo avalia apenas a propagacao de um pulso unico. Nao envolve sequencias de multiplos pulsos, cadencia temporal especifica
nem deteccao por comparador digital.

