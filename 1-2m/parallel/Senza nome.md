COMPUTATIONAL PROBLEM: $$\pi \subseteq I \times S$$$$(i,s)\in\Pi \quad [i\pi S]$$s: soluzione a i
Algoritmo che risolve $\pi$: implementa funzione $$A\pi:I\rightarrow S \quad \forall i\in I: i\pi A_{\Pi}(i)\in S$$
Con algoritmi, vogliamo studiare lower/upper bound:
- upper bound: esiste $A_\Pi$ che risolve $\pi$ tale che $T_A(n)=O(f(n))$
- lower bound: ogni $A_\Pi$ che risolve $\pi$ è tale che $T_A(n)=\Omega(f(n))$
Lower bound molto più forte e difficile da trovare
Ordine di $f(n)$: difficoltà di $\Pi$

CATEGORIE DI PROBLEMI:
- TRACTABLE: problemi che ammettono soluzioni polinomiali $$\exists A_{\pi}:T_{A_{\pi}}(n)=O(n^k), k>0$$
- PROVABLY INTRACTABLE: problemi che ammettono lower bound esponenziale $$\exists c>1: \forall A_{\pi}(n):T_{A_\pi}(n)=\Omega(c^n)$$
- UNDECIDABLE/UNSOLVABLE: problemi che non ammettono algoritmi (e.g. Halting problem) $$\pi_{halt}: I=\{<M,x>, M \text{Turing machine}, x\in\{0,1\}^*\}; S=\{yes,no\}$$$<M,x>\pi_{halt}$yes <-> $M(x)$ halts
- INTRACTABLE: non si conoscono lower bound esponenziali nè upper bound polinomiali
	- grande interesse pratico
	- forti proprietà strutturali: alg polinomiale per problema semplice dà alg polinomiali per tutti

Standardizzare problemi computazionali
ABSTRACT DECISION PROBLEMS: $$\pi_D\subset I\times S, S=\{yes,no\}$$Formulazione:
- descrizione di istanza genercica
- Domanda su istanza
Problema è proprio funzione
OPTIMIZATION PROBLEM: $$\pi_{opt}\subseteq I \times S, \quad c:S\rightarrow N\cup\{ +\infty \}$$
$\forall i\in I$, determina

Associare decision problem a problema approssimazione, tecnica standard, aggiungere istanza con numero naturale che rappresenta upper/lower bound a funzione obiettivo
Non totalmente equivalente, ma alg polinomiale per decision può essere usare come subroutine per risolvere alg approssimazione