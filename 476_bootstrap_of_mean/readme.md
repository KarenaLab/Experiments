### P476 - Bootstrap com a média
------

#### Motivação e descrição do experimento
**Bootstrap** é uma das técnicas mais poderosas da estatística e que neste experimento será demonstrado o seu poder para estimar a média da população através de consecutivas amostragens.

Este experimento usará como base o texto do livro *Estatística Prática para cientistas de dados (Peter e Andrew Bruce)*.
> "Conceitualmente, pode-se imaginar o bootstrap como a replicação amostral original milhares ou milhões de vezes, de modo a ter a população hipotética que representa todo o conhecimento da amostra original (só que maior)"


#### Guia rápido do experimento
Este esperimento segue o algorítmo sugerido pelos autores e é descrito abaixo:
1. Extraia um valor da amostra, registre e **reponha**,
2. Repita o passo 1 *n* vezes,
3. Registre a **média** dos *n* valores reamostrados,

4. Repita os passos 1 à 3 *r* vezes,
5. Utilize os resultados de *r* para:
  a. Calcule o desvio padrão (usado para estimar o erro padrão da média da amostra),
  b. Construa um histograma ou boxplot,
  c. Encontre o intervalo de confiança,

Os valores *n* (tamanho da sub-amostra) e *r* (número de iterações ou repetições) é ajustado de forma arbitrária mas quanto maiores, mais precisa será a estimativa do intervalo de confiança. 


#### Resultados


#### Informações relevantes
