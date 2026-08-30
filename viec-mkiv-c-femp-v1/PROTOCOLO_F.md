[PDF page 1 image attached. Read this image directly to extract content.]

Protocolo F | Uso restrito a medicao contratada pag. 1
PROTOCOLO DE MEDICAO F
Comparacao de Trens de Pulso Periodicos versus Quase-Periodicos
Documento independente — nao requer conhecimento de outros protocolos

Objetivo
Comparar o residual de interferencia / ringing observado na saida de um canal de transmissao quando a excitacao e um
trem de pulsos com espacamento fixo versus um trem de pulsos com espacamento gerado por recorrencia linear (soma
dos dois intervalos anteriores). O foco e puramente temporal e de dominio de frequencia; nao ha interpretacao de dados.
Sequencias a gerar
Sequencia periodica (controle): espacamento constante T = 50 ns (ou 10 ns, conforme a capacidade do gerador).
Sequencia quase-periodica: intervalos gerados pela recorrencia d_n = d_(n-1) + d_(n-2), com semente d_0 = d_1 =
T_base (T_base = 16 ns ou 10 ns). Exemplo de intervalos (em multiplos de T_base): 1, 1, 2, 3, 5, 8, 13, 21, …
Ambas as sequencias devem conter o mesmo numero total de pulsos (ex.: 8 ou 16) e a mesma energia media.
DUT e instrumentacao
• Canal de transmissao do Protocolo A (com ou sem descontinuidades do Protocolo B).
• Gerador capaz de produzir as duas sequencias (AWG, SDR ou RFSoC).
• Osciloscopio ou receptor de banda larga na saida.
• Opcional: analise espectral do residual apos o ultimo pulso.
Procedimento
Transmitir a sequencia periodica; capturar a forma de onda completa na saida.
Transmitir a sequencia quase-periodica com a mesma energia; capturar.
Medir a energia residual (integral do |v(t)|^2) na janela de 100 ns apos o ultimo pulso em ambas as sequencias.
Comparar o espectro residual (FFT da janela pos-pulso).
Se descontinuidades estiverem instaladas, repetir com polarizacoes 0 V e 5 V.
Entregaveis
• Formas de onda completas (CSV) das duas sequencias.
• Valor da energia residual pos-pulso (periodica vs quase-periodica).
• Espectros residuais sobrepostos.
• Comentario quantitativo: a sequencia quase-periodica reduziu, aumentou ou nao alterou o residual de interferencia?
Este protocolo compara apenas duas cadencias temporais de excitacao. Nao revela a funcao de nenhum elemento individual, nao
menciona logica digital e nao exige conhecimento da aplicacao final do sistema.
