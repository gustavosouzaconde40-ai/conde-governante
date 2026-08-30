[PDF page 1 image attached. Read this image directly to extract content.]

Protocolo A | Uso restrito a medicao contratada pag. 1
PROTOCOLO DE MEDICAO A
Caracterizacao RF de Canal de Transmissao Reto em Aluminio
Documento independente — nao requer conhecimento de outros protocolos

Objetivo
Medir os parametros de espalhamento (S11, S21) de um canal de transmissao reto usinagem em bloco de Aluminio 6061,
com fita condutora centralizada, na faixa 0,5–3,0 GHz. O objetivo e verificar se a impedancia caracteristica permanece
proxima de 50 Ohm e se as perdas de retorno sao aceitaveis.
Hardware fornecido / a ser montado pelo medidor
• Bloco de Al 6061: 250 mm (comprimento) × 40 mm (largura) × 20 mm (altura).
• Canal usinado: 12 mm de largura × 10 mm de profundidade, centrado.
• Fita de CuBe (ou cobre berilio equivalente) 3,2 mm × 0,2 mm, centralizada no fundo do canal.
• Conectores SMA edge-mount nas duas extremidades (Rosenberger ou equivalente 50 Ohm).
• Tampa de 5 mm de Al (opcional para esta medicao; pode ficar aberta).
• Importante: Neste protocolo nao devem ser instalados quaisquer componentes ativos, PCBs ou elementos reativos no
canal. Medicao puramente passiva.
Instrumentacao necessaria
• VNA calibrado (NanoVNA V2 Plus4 ou superior, preferivel Keysight/R&S; ate 6 GHz).
• Kit de calibracao SOLT (Short-Open-Load-Thru) SMA.
• Cabos SMA de baixa perda, comprimento conhecido.
Procedimento
Calibrar o VNA na faixa 0,5–3,0 GHz (pelo menos 201 pontos).
Conectar o DUT (canal completo com SMA) entre as portas 1 e 2.
Registrar S11 e S21 em formato Touchstone (.s2p).
Repetir com a tampa instalada e sem a tampa.
Anotar temperatura ambiente e umidade.
Criterios de aceitacao (metas de engenharia)
Parametro Meta Faixa
S11 (retorno) < –20 dB 0,5–3 GHz
|Z0 – 50| < 2 Ohm 1 GHz
S21 (insercao) > –1,5 dB 0,5–3 GHz
Entregaveis solicitados
• Arquivo .s2p (tampa aberta e tampa fechada).
• Grafico S11 e S21 vs frequencia (PDF ou PNG).
• Tabela com Z0 extraido em 1,0 / 1,5 / 2,0 / 2,5 GHz.
• Foto do setup de medicao.
• Data, operador e instrumento utilizado.
Este protocolo e autocontido. Nao e necessario conhecer a aplicacao final do canal. Trata-se apenas de caracterizacao de uma linha de
transmissao mecanica.

