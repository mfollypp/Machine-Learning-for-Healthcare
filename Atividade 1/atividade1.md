# Atividade 1 - Regressão Logística

## Descrição do Data Set
`age`: Idade do paciente.
*  Idade pode influenciar o risco de doenças cardíacas.

`sex`: Sexo (1 = masculino; 0 = feminino).
* Homens e mulheres podem ter diferentes riscos cardíacos.

`cp`: Tipo de dor no peito (4 valores: 1 = angina típica; 2 = angina atípica; 3 = dor não anginosa; 4 = assintomática).
* Angina é uma dor no peito ou sensação de pressão que ocorre quando o músculo cardíaco não recebe oxigênio suficiente.

`trestbps`: Pressão arterial em repouso (mm Hg).
* Pressão alta pode ser um fator de risco para doenças cardíacas.

`chol`: Colesterol sérico em mg/dl.
* Níveis altos de colesterol podem levar a aterosclerose.

`fbs`: Açúcar no sangue em jejum > 120 mg/dl (1 = verdadeiro; 0 = falso).
* Açúcar elevado pode indicar diabetes, um fator de risco cardíaco.

`restecg`: Resultados do eletrocardiograma em repouso (0 = normal; 1 = com anormalidade na onda ST-T; 2 = hipertrofia ventricular esquerda).
* Anormalidades no ECG podem indicar problemas cardíacos.

`thalach`: Frequência cardíaca máxima atingida.
* Frequência cardíaca alta pode indicar boa saúde cardiovascular.

`exang`: Angina induzida por exercício (1 = sim; 0 = não).
* Angina durante exercício pode indicar doença arterial coronariana.

`oldpeak`: Depressão do segmento ST induzida por exercício em relação ao repouso.
* Depressão ST pode indicar isquemia miocárdica.

`slope`: Inclinação do segmento ST no pico do exercício (1 = subida; 2 = plana; 3 = descendente).
* Inclinação ST pode ajudar a diagnosticar a gravidade da isquemia.

`ca`: Número de vasos principais (0-3) coloridos por fluoroscopia.
* Mais vasos coloridos podem indicar maior gravidade da doença.

`thal`: 0 = normal; 1 = defeito fixo; 2 = defeito reversível.
* Defeitos no tálio podem indicar áreas de isquemia ou infarto.

`target`: Diagnóstico de doença cardíaca (1 = presença de doença; 0 = ausência de doença).
* Indica se o paciente tem ou não doença cardíaca.

## Análise Descritiva das Variáveis

|       |        age |         sex |         cp |   trestbps |      chol |         fbs |     restecg |   thalach |       exang |    oldpeak |      slope |          ca |       thal |      target |
|:------|-----------:|------------:|-----------:|-----------:|----------:|------------:|------------:|----------:|------------:|-----------:|-----------:|------------:|-----------:|------------:|
| count | 1025       | 1025        | 528        |  1025      | 1025      | 1025        | 1025        | 1025      | 1025        | 1025       | 951        | 1025        | 1025       | 1025        |
| mean  |   54.4341  |    0.69561  |   1.82955  |   131.612  |  246      |    0.149268 |    0.529756 |  149.114  |    0.336585 |    1.07151 |   1.49317  |    0.754146 |    2.3239  |    0.513171 |
| std   |    9.07229 |    0.460373 |   0.658702 |    17.5167 |   51.5925 |    0.356527 |    0.527878 |   23.0057 |    0.472772 |    1.17505 |   0.500216 |    1.0308   |    0.62066 |    0.50007  |
| min   |   29       |    0        |   1        |    94      |  126      |    0        |    0        |   71      |    0        |    0       |   1        |    0        |    0       |    0        |
| 25%   |   48       |    0        |   1        |   120      |  211      |    0        |    0        |  132      |    0        |    0       |   1        |    0        |    2       |    0        |
| 50%   |   56       |    1        |   2        |   130      |  240      |    0        |    1        |  152      |    0        |    0.8     |   1        |    0        |    2       |    1        |
| 75%   |   61       |    1        |   2        |   140      |  275      |    0        |    1        |  166      |    1        |    1.8     |   2        |    1        |    3       |    1        |
| max   |   77       |    1        |   3        |   200      |  564      |    1        |    2        |  202      |    1        |    6.2     |   2        |    4        |    3       |    1        |

> As colunas `age`, `cp` e `slope` tiveram seus valores 0 trocados por NaN pois indicam ausência de dado


---

## Referência de Imagens

### Histogramas:
| ![histogram_age](images/histograms/histogram_age.png) | ![histogram_chol](images/histograms/histogram_chol.png) |
|--------------------------------|--------------------------------|
| ![histogram_thalach](images/histograms/histogram_thalach.png) | ![histogram_trestbps](images/histograms/histogram_trestbps.png) |

### Foi observado:

* Maior porcentagem de pacientes com doenças cardíacas tem entre 40 - 54 anos
* Maior porcentagem de pacientes com doenças cardíacas tem 180 - 260 de colesterol
* Pacientes com frequência cardíaca máxima maior que 150 apresentam alguma doença cardíaca
* A pressão arterial em repouso é bem distribuída entre pacientes com e sem doença cardíaca

### Boxplots:
| ![boxplot_age](images/boxplots/boxplot_age.png) | ![boxplot_chol](images/boxplots/boxplot_chol.png) |
|--------------------------------|--------------------------------|
| ![boxplot_thalach](images/boxplots/boxplot_thalach.png) | ![boxplot_trestbps](images/boxplots/boxplot_trestbps.png) |

### Foi observado:

* Apenas a frequência cardíaca máxima (thalach) parece ser um maior indicador do grupo com doenças cardíacas, os outros estão bem distribuídos


### Pairplot (Gráfico de Dispersão):
![Pairplot](images/pairplot.png)

> Correlação Positiva: Se os pontos parecem formar uma linha inclinada para cima (da esquerda para a direita), indica que as duas variáveis tendem a aumentar juntas
>
> Correlação Negativa: Se a linha se inclina para baixo, isso significa que uma variável tende a diminuir à medida que a outra aumenta
>
> Nenhuma Correlação: Se os pontos estão espalhados aleatoriamente, sem um padrão claro, há pouca ou nenhuma correlação entre as variáveis

### Foi observado:

* Parece que a frequência cardíaca máxima (thalach) tende a diminuir com o avanço da idade
* As outras variáveis não parecem ter uma correlação aparente em vista que os pontos estão mais dispersos


---

## Teste de Correlação (Pearson)
> 1 = correlação perfeita
>
> -1 = correlação negativa perfeita
>
> 0 = sem correlação
>
> Valor-P (p-value): Avalia a significância estatística da correlação observada
>
> Se o p-valor for baixo, rejeitamos a hipótese nula e concluímos que há uma correlação significativa entre as variáveis (geralmente comparado por `p-valor <= 0.05`, no caso 5%)
>
> Se o p-valor for alto, não rejeitamos a hipótese nula, o que sugere que não há evidências suficientes para afirmar que existe uma correlação significativa

### `age` x `chol`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | 0.2198 | 0.0000 |

### `age` x `thalach`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | -0.3902 | 0.0000 |

### `age` x `trestbps`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | 0.2711 | 0.0000 |

### `age` x `cp`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | 0.1626 | 0.0002 |

### `chol` x `thalach`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | -0.0218 | 0.4863 |

### `chol` x `trestbps`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | 0.1280 | 0.0000 |

### `chol` x `cp`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | -0.0455 | 0.2964 |

### `thalach` x `trestbps`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | -0.0393 | 0.2091 |

### `thalach` x `cp`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | -0.1173 | 0.0070 |

### `trestbps` x `cp`
| Coef. Correlacao | P-Valor | 
 | --- | --- | 
 | 0.2131 | 0.0000 |

---

## Modelo Explicativo: Regressão Logística

```python
# Preparar os dados para o modelo
X = data[['age', 'sex', 'cp', 'chol', 'thalach', 'ca']].dropna()
y = data.loc[X.index, 'target']

# # Identificar variáveis contínuas
# continuous_vars = ['age', 'chol', 'thalach']

# # Normalizar apenas as variáveis contínuas
# X[continuous_vars] = (X[continuous_vars] - X[continuous_vars].min()) / (X[continuous_vars].max() - X[continuous_vars].min())

# Ajustar o modelo de regressão logística
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Resumo dos coeficientes: Valores negativos do intercepto levam a probabilidades baixas e valores positivos a probabilidades altas
coef = pd.DataFrame(model.coef_, columns=X.columns)
coef['Intercept'] = model.intercept_
```

O que é Regressão Logística?

* A regressão logística é uma técnica de modelagem estatística usada para prever a probabilidade de um resultado binário (com duas categorias) com base em uma ou mais variáveis independentes (também chamadas de preditoras). Ao contrário da regressão linear, que prevê um valor numérico contínuo, a regressão logística é usada para prever probabilidades que, em última análise, são classificadas em uma de duas categorias, como "sim/não", "sucesso/fracasso" ou "positivo/negativo".

Como Funciona?

* A regressão logística transforma a combinação linear das variáveis preditoras em uma probabilidade, utilizando a função logística (ou sigmoide). A função logística mapeia qualquer valor real em um intervalo entre 0 e 1, o que é ideal para prever probabilidades.


---

## Interpretação dos Resultados

### Coeficientes do Modelo (sem normalizar as variáveis):
|    |        age |      sex |       cp |        chol |   thalach |       ca |   Intercept |
|---:|-----------:|---------:|---------:|------------:|----------:|---------:|------------:|
|  0 | -0.0485356 | -2.53564 | -0.11936 | -0.00822811 |  0.031184 | -0.43818 |     3.50242 |

> Para calcular a probabilidade a partir do log-odds (intercepto) de 3.50242, podemos seguir os seguintes passos:
>
> Calcular o valor de: `e^(-3.50242) ~= 0.0301`
>
> Adicionar 1 ao resultado: `1 + 0.0301 = 1.0301`
>
> Calcular o inverso do resultado: `1/1.0301 = 0.9708`
>
> Portanto, a probabilidade é aproximadamente 0.9708, ou `97.08%`
>
> A probabilidade calculada a partir do intercepto é a probabilidade predita do evento ocorrer na ausência dos efeitos das variáveis preditoras
>
> Os coeficientes do modelo mostram como cada variável individualmente influencia essa probabilidade base
>
> Para prever corretamente o 𝑦 (o desfecho), é necessário considerar tanto o intercepto quanto todos os coeficientes associados às variáveis preditoras
>
> Interpretação dos Coeficientes:
>
> Coeficientes Negativos: Indicam que, conforme a variável aumenta, a probabilidade do evento diminui
>
> Coeficientes Positivos: Indicam que, conforme a variável aumenta, a probabilidade do evento aumenta

### AIC do modelo:
441.2955477421557

> Quanto menor o AIC melhor o modelo

### Odds Ratio:
|         |   Odds Ratio |
|:--------|-------------:|
| const   |   50.9664    |
| age     |    0.950171  |
| sex     |    0.0535761 |
| cp      |    0.894448  |
| chol    |    0.99091   |
| thalach |    1.03348   |
| ca      |    0.636721  |

> Sobre Odds Ratio:
>
> Normalizar as variáveis antes de calcular o odds ratio pode tornar a interpretação menos clara
>
> O odds ratio é diretamente ligado aos coeficientes do modelo: é a exponencial do coeficiente
>
> O odds ratio mostra como as chances do evento mudam com um aumento de uma unidade na variável preditora
>
> Odds Ratio = 1: Nenhuma associação. A variável não influencia nas chances do evento
>
> Odds Ratio > 1: Associação positiva. As chances do evento ocorrer aumentam com o aumento da variável

Os fatores de risco mais relevantes são:

* Frequência cardíaca máxima, mas influencia muito pouco a probabilidade de ter doença cardíaca pois o coeficiente é muito próximo de 0

### Coeficientes do Modelo (normalizando as variáveis):
|    |      age |     sex |        cp |    chol |   thalach |        ca |   Intercept |
|---:|---------:|--------:|----------:|--------:|----------:|----------:|------------:|
|  0 | -2.04973 | -2.1921 | -0.132445 | -1.6496 |   2.24911 | -0.396035 |     3.66558 |

### AIC do modelo:
441.29554774215563

### Odds Ratio:
|         |   Odds Ratio |
|:--------|-------------:|
| const   |   86.4322    |
| age     |    0.0905063 |
| sex     |    0.0535761 |
| cp      |    0.894448  |
| chol    |    0.0183213 |
| thalach |   32.7978    |
| ca      |    0.636721  |
---

## Conclusão

Os fatores de risco mais relevantes para a previsão da doença cardíaca é a `Frequência cardíaca máxima` e esses insights podem ser utilizados em prática clínica ou em futuros estudos `para direcionar os pacientes para exames mais específicos ou na descoberta da presença de algum tipo de doença cardíaca`