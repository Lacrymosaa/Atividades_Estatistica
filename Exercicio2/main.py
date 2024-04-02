import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

for folder in ['AleatoriaSimples', 'Sistematica', 'Estratificada']:
    if not os.path.exists(folder):
        os.makedirs(folder)

dados_tabela1 = '''
O GE FE AE RF AT GR
1 1 2 20 4.0 14 4
2 1 2 15 5.3 12 4
3 1 1 14 8.5 3 2
4 1 5 14 9.0 40 5
5 1 2 18 7.6 15 3
6 1 2 16 7.4 15 3
7 1 3 13 5.7 30 5
8 1 3 4 2.5 31 4
9 1 2 16 9.4 23 4
10 1 4 16 9.8 43 4
11 1 1 16 10.5 7 3
12 1 1 11 10.8 3 2
13 1 2 10 12.0 17 3
14 1 1 16 12.8 14 3
15 1 2 13 13.2 27 4
16 1 2 15 13.9 18 4
17 1 2 16 14.7 15 4
18 1 4 13 17.3 24 5
19 1 2 13 23.3 23 3
20 1 2 19 14.7 19 4
21 1 3 15 18.8 23 4
22 1 2 12 19.4 16 4
23 1 4 14 23.3 42 5
24 1 1 12 4.6 1 1
25 1 2 18 16.2 23 4
26 1 1 10 18.8 6 3
27 1 1 6 3.0 0.5 1
28 1 5 14 8.5 42 5
29 1 2 12 8.7 12 4
30 1 3 15 9.1 20 4
31 1 1 12 4.6 10 4
32 1 2 17 5.3 18 4
33 1 4 16 8.1 36 4
34 1 3 14 7.0 27 4
35 1 1 12 9.0 27 3
36 1 2 15 9.0 18 4
37 1 1 16 8.0 8 3
38 1 4 9 6.7 34 4
39 1 2 16 4.0 13 4
40 1 3 12 6.5 26 4
41 1 3 12 8.5 32 5
42 1 1 16 9.0 11 5
43 1 4 12 4.0 30 4
44 1 3 14 4.5 37 5
45 1 2 13 7.0 11 3
46 1 1 14 7.0 17 3
47 1 5 15 6.5 42 4
48 1 4 16 4.6 30 4
49 1 3 14 5.3 24 4
50 1 1 17 5.7 8 3
51 1 3 14 14.7 23 3
52 1 2 20 15.0 21 4
53 2 5 14 4.6 25 5
54 2 2 12 8.7 15 4
55 2 2 14 9.1 10 5
56 2 1 13 7.4 10 3
57 2 2 12 8.1 13 4
58 2 2 12 6.3 12 4
59 2 4 14 6.7 20 5
60 2 5 12 9.8 20 4
61 2 2 13 11.1 20 4
62 2 1 12 11.6 7 3
63 2 4 16 13.6 36 4
64 2 3 16 7.0 25 5
65 2 2 12 16.0 18 5
66 2 4 14 16.2 33 5
67 2 2 12 16.6 15 5
68 2 3 16 18.8 9 4
69 2 1 17 19.4 11 3
70 2 2 16 13.9 12 3
71 2 1 16 4.0 7 5
72 2 2 16 5.3 14 3
73 2 2 9 5.7 18 4
74 2 3 17 5.0 22 3
75 2 1 14 14.7 3 3
76 2 1 16 16.0 13 4
77 2 2 15 19.4 20 5
78 2 2 15 9.0 10 4
79 2 4 10 9.4 30 4
80 2 1 9 3.7 4 3
81 2 2 13 8.5 23 5
82 2 1 11 6.0 5 5
83 2 3 10 8.5 13 5
84 2 2 14 8.7 12 5
85 2 1 13 5.0 10 5
86 2 1 16 9.4 6 5
87 2 2 14 4.6 4 5
88 2 4 12 5.3 15 4
89 2 2 16 4.5 19 4
90 2 2 12 8.0 20 4
'''
df_tabela1 = pd.read_csv(StringIO(dados_tabela1), delim_whitespace=True)

seed = 42

amostra_aleatoria_simples = df_tabela1.sample(n=15, random_state=seed)

passo = len(df_tabela1) // 15  
amostra_sistematica = df_tabela1.iloc[::passo][:15]

amostras_estratificadas = []
for _, grupo in df_tabela1.groupby('FE'):
    amostra_estratificada = grupo.sample(n=3, random_state=seed)
    amostras_estratificadas.append(amostra_estratificada)
amostra_estratificada = pd.concat(amostras_estratificadas)

amostra_aleatoria_simples.to_excel('AleatoriaSimples/amostra_aleatoria_simples.xlsx', index=False)
amostra_sistematica.to_excel('Sistematica/amostra_sistematica.xlsx', index=False)
amostra_estratificada.to_excel('Estratificada/amostra_estratificada.xlsx', index=False)

