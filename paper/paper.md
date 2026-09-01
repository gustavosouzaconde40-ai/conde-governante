title: "Conde-Ruler: a Python ruler for measuring the Conde current"
tags:

Conde_current
geophysical_measurement
time_series
Python
authors:
name: Gustavo Alves Conde
affiliation: 1
affiliations:
name: Independent Researcher, Baixo Guandu, ES, Brazil
index: 1
date: 2026-08-31
bibliography: paper.bib
Resumo
Conde-Ruler é um pacote Python leve que fornece uma "régua" programática e reproduzível para medir e caracterizar a corrente de Conde a partir de séries temporais de observações.

Declaração de necessidade
A medição precisa e reproduzível de correntes oceânicas e costeiras é fundamental para muitas aplicações científicas e de engenharia. A corrente de Conde é comumente relatada por diferentes plataformas e processada com scripts específicos que raramente são compilados para reutilização.

Características
Pré-processamento de séries temporais: reamostragem uniforme, tratamento de lacunas, remoção de tendências.
Extração de corrente de Condé: algoritmos para estimar amplitude e fase locais.
Estatísticas resumidas e diagnósticos.
Controle de qualidade
O Conde-Ruler inclui um conjunto de testes unitários e de integração (pytest) que avalia a importabilidade, a consistência numérica em dados sintéticos e os principais casos extremos. O repositório fornece um pequeno conjunto de dados de exemplo. A integração contínua (GitHub Actions) está configurada para executar o conjunto de testes em todas as versões do Python suportadas (3.9, 3.10, 3.11) a cada push e pull request.

Disponibilidade
Código-fonte: GitHub — https://github.com/gustavosouzaconde40-ai/conde-governante
Licença: MIT
Instalação: pip install.
Versões do Python suportadas: 3.9, 3.10 e 3.11
Conjuntos de dados grandes: arquivados no Zenodo (DOI a ser adicionado).

Referências
Conde, G. A. (2026). Conde-Ruler. GitHub repository.
