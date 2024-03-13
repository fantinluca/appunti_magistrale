# $m\geq\frac{\log(|\mathcal{H}|/\delta)}{\epsilon}$
Let $\mathcal{H}$ be a finite hypothesis class, $\epsilon,\delta\in(0,1)$ and $m\geq\ldots$; then, for any probability distribution $\mathcal{D}$ and labeling function $f$  for which the realizability assumption holds, with probability $\geq1-\delta$ over the choice of a training set $S$ with $m$ i.i.d. samples, for every ERM hypothesis $h_S$ we have $L_{\mathcal{D},f}(h_S)\leq\epsilon$.
# $m_{\mathcal{H}}^{\text{UC}}(\epsilon,\delta)\leq\lceil\frac{\log(2|\mathcal{H}|/\delta)}{2\epsilon^2}\rceil$
Given a finite hypothesis class $\mathcal{H}$, a domain $Z$ and a loss function $l:\mathcal{H}\times Z\rightarrow[0,1]$, then:
- $\mathcal{H}$ has the uniform convergence property with sample complexity $\ldots$
- $\mathcal{H}$ is agnostic PAC learnable using the ERM algorithm with sample complexity $m_{\mathcal{H}}(\epsilon,\delta)\leq m_{\mathcal{H}}^{\text{UC}}(\epsilon/2,\delta)$
# $|L_V(h)-L_{\mathcal{D}}(h)|\leq\sqrt{\frac{\log(2/\delta)}{2m_V}}$
Given a loss function limited to $[0,1]$, $\forall \delta\in(0,1)$, then with probability $\geq1-\delta$ over the choice of V, $\ldots$
# $\forall h\in\{h_1,\ldots,h_r\}|L_V(h)-L_{\mathcal{D}}(h)|\leq\sqrt{\frac{\log(2r/\delta)}{2m_V}}$
Given an hypothesis class $\mathcal{H}=\bigcup_{i=1}^r\mathcal{H}_i$ and $h_i$ the hypothesis picked by the ERM algorithm from $\mathcal{H}_i$, given a loss function limited to $[0,1]$, $\forall\delta\in(0,1)$, then with probability $\geq1-\delta$ over the choice of V, $\ldots$
# $C_1\frac{d+\log(1/\delta)}{\epsilon^2}\leq m_{\mathcal{H}}^{\text{UC}}\leq C_2\frac{d+\log(1/\delta)}{\epsilon^2}$
Given an hypothesis class $\mathcal{H}$ from $\mathcal{X}$ to $\{0,1\}$ such that $\text{VCdim}(\mathcal{H})=d<+\infty$ and considering the 0-1 loss, then $\exists C_1,C_2$ constants such that:
- $\mathcal{H}$ has the uniform convergence property with sample complexity $\ldots\leq m_{\mathcal{H}}^{\text{UC}}\leq\ldots$
- $\mathcal{H}$ is agnostic PAC learnable with ERM with sample complexity $\ldots\leq m_{\mathcal{H}}\leq\ldots$
# $\forall h\in\mathcal{H} L_{\mathcal{D}}(h)\leq L_S(h)+C\sqrt{\frac{d+\log(1/\delta)}{2m}}$
Given an hypothesis class $\mathcal{H}$ with $\text{VCdim}(\mathcal{H})=d<+\infty$, then, with probability $\geq1-\delta$ over the choice of the training set $S\sim\mathcal{D}^m$, given $C$ universal constant: