# 📐 Themis Vector Space Model (TVSM)

Themis abandona heurísticas lineares simples em favor de um modelo vetorial tridimensional para calcular a **Magnitude de Inovação** ($\| \vec{I} \|$) de um projeto.

Nossa abordagem modela a patentiabilidade como um vetor no espaço $\mathbb{R}^3$, onde cada eixo representa uma dimensão crítica da análise técnica-jurídica.

---

## 1. As Dimensões do Vetor

Definimos o vetor de inovação $\vec{I}$ como:

$$ \vec{I} = \begin{bmatrix} \mathcal{H} \\ \mathcal{Z} \\ \mathcal{C} \end{bmatrix} $$

Onde:

### $\mathcal{H}$: Densidade de Informação (Shannon Entropy)
Baseada na Teoria da Informação de Shannon, mede a quantidade de "surpresa" ou informação técnica contida no texto. Textos genéricos têm entropia baixa; textos técnicos densos têm entropia alta.

$$ \mathcal{H}(X) = - \sum_{i=1}^{n} p(x_i) \log_2 p(x_i) $$
Normalized to $[0, 1]$.

### $\mathcal{Z}$: Sofisticação Léxica (Zipfian Deviation)
Mede o desvio do vocabulário em relação à distribuição padrão da linguagem (Lei de Zipf). Projetos inovadores tendem a usar terminologias raras e específicas ("Technical Density").

$$ \mathcal{Z} = \frac{\sum_{w \in W} \text{len}(w) \cdot \mathbb{I}(w \notin \text{Common})}{\|W\|} $$
Normalized to $[0, 1]$.

### $\mathcal{C}$: Conformidade Legal (Legal Compliance)
O inverso do risco detectado. Quanto menos padrões de bloqueio (Art. 10 LPI - Business Methods, Software puro) o texto apresenta, maior sua conformidade.

$$ \mathcal{C} = \frac{1}{1 + \sum (w_p \cdot n_p)} $$

Onde $w_p$ é o peso do padrão sensível e $n_p$ é o número de ocorrências.

---

## 2. A Métrica: Magnitude de Inovação

A pontuação final não é uma soma, mas a **Norma Euclidiana** do vetor projetado. Isso recompensa o equilíbrio entre as três dimensões.

$$ \| \vec{I} \| = \sqrt{\mathcal{H}^2 + \mathcal{Z}^2 + \mathcal{C}^2} $$

### Normalização Final

Como o valor máximo teórico de cada componente é 1.0, a magnitude máxima possível é $\sqrt{3} \approx 1.732$.
O **Themis Score ($S_{themis}$)** é calculado percentualmente:

$$ S_{themis} = \left( \frac{\sqrt{\mathcal{H}^2 + \mathcal{Z}^2 + \mathcal{C}^2}}{\sqrt{3}} \right) \cdot 100 $$

---

## 3. Interpretação Geométrica

- **Vetor Curto ($\| \vec{I} \| \to 0$):** Projeto genérico, vocabulário pobre, alto risco legal. (Ex: "App de entrega").
- **Vetor Longo ($\| \vec{I} \| \to 1.73$):** Alta densidade técnica, termos específicos, "clean" de riscos legais. (Ex: "Método de compressão neural via quantização dinâmica").

---

*"A justiça não é cega; ela é matematicamente precisa."* — **Themis Engine**
