# 34

# 35

# 36

# 37

# 38

# 39

# 40

# 41
## $\phi^4$ Theory
$\phi^4$ Theory obeys the Lagrangian
$$
\mathcal L = \frac 1 2 (\partial_\mu\phi)^2 - \frac 1 2 m^2\phi^2 - \frac \lambda {4!} \phi^4
$$
We want to be able to calculate the Green's Function
$$
\bra\Omega T\phi(x)\phi(y)\ket\Omega
$$
for an arbitrary amount of fields.
The Hamiltonian for such a Theory is
$$
H = H_\text{free} + H_\text{int}
$$
where in our case
$$
H_\text{int} = \int \text d^3x \frac \lambda {4!}\phi^4(x)
$$
We define the field operator at a reference time $t_0$ as the usual Fourier decomposition $\phi_S(t_0, x)$. We define the interaction picture field operator
$$
\phi_I(t,x) = e^{iH_0(t-t_0)}\phi_S(t_0,x)e^{-iH_0(t-t_0)} 
$$
which is then
$$
\phi_I(t,x) = \int\text d\tilde p \frac 1 {\sqrt{2E_p}}\left(a_p e^{-ipx} + a_p^\dagger e^{ipx}\right)|_{x^0=t-t_0}
$$
to get the Heisenberg picture field we then need to use the Operator
$$
U(t,t_0)= e^{iH_0(t-t_0)} e^{-iH(t-t_0)}
$$
as
$$
\phi_H(t,x) = U^\dagger(t,t_0) \phi_I(t_0,x) U(t,t_0)
$$
rewriting $U$ for an arbitrary $t$ and $t'$ we get
$$
U(t,t') = T\left\{\exp\left[-i\int_{t'}^t \text dt'' H_I(t'')\right]\right\}
$$
After some calculations, we arrive at the expression we wanted to find previously
$$
\bra\Omega T\{\phi(x)\phi(y)\}\ket\Omega = \lim_{T\rightarrow\infty(1-i\epsilon)}\frac{\bra0 T\biggl\{\phi_I(x)\phi_I(y)U(T,-T)\biggr\}\ket 0}{\bra0U(T,-T)\ket0}
$$
with $\ket\Omega$ being
$$
\ket\Omega = \lim_{T\rightarrow\infty(1-i\epsilon)}(e^{-iE_0(t_0-(-T))}\braket{\Omega|0})^{-1}U(t_0,-T)\ket0
$$


## Wick's Theorem:
We wish to calculate the term
$$
\bra 0 T\{\phi_I(x_1)\cdots\phi_I(x_n)\}\ket 0
$$
decomposing the field into positive and negative frequencies gives
$$
	\phi^+_I(x) = \int \text d\tilde p \frac{1}{\sqrt{2E_p}}a_p e^{-ipx}
$$
$$
\phi_I^-(x) = \int \text d\tilde p \frac{1}{\sqrt{2E_p}}a_pe^{ipx}
$$
where we have
$$
\phi_I^+ \ket 0 = 0,\;\;\;\; \bra 0\phi_I^- = 0
$$
we then define the Wick contraction
$$
W(\phi(x), \phi(y)) = \cases{
[\phi^+(x), \phi^-(y)] & , for $x^0 > y^0$\\
[\phi^+(y), \phi^-(x)] & , for $y^0 > x^0$
}
$$
And the Wick contraction is equal to the Feynman propagator
$$
W(\phi(x), \phi(y)) = D_F(x-y)
$$
And the first term is for two fields is then
$$
T\{\phi(x)\phi(y)\} = N\left\{\phi(x)\phi(y) + W(\phi(x),\phi(y))\right\}
$$
And in the general case we have
$$
T\{\phi(x_1)\cdots\phi(x_n)\} = N\{\phi(x_1)\cdots\phi(x_n) + \text{all possible contractions}\}
$$
Only fully contracted terms contribute to the final term, because
$$
\bra 0 N(\text{any operator})\ket 0 = 0
$$
That means that the Time ordering of fields is equal to all the possible Feynman propagator pairs
$$
\bra 0 T\{\phi_1\phi_2\phi_3\phi_4\} \ket0 = D_F(x_1-x_2)D_F(x_3-x_4)
$$
$$
+ D_F(x_1-x_3)D_F(x_2-x_4) + D_F(x_1-x_4)D_F(x_2-x_3)
$$
## Feynman Diagrams
We can apply the Wick Theorem by considering propagations between spacetime points, using Feynman Diagrams.
![[Pasted image 20241206023243.png]]
We want to look at the numerator of $\bra\Omega T\{\phi(x)\phi(y)\}\ket\Omega$ in $\phi^4$ theory.
$$
\bra 0 T\left\{\phi(x)\phi(y) + \phi(x)\phi(y)\left[-i\int\text dt H_I(t)\right] +\cdots\right\}\ket0
$$
The first term is the free field result, the second term is
$$
\bra 0 T\left\{\phi(x)\phi(y) \left(\frac{-i\lambda}{4!}\right)\int\text d^4z\phi(z)\phi(z)\phi(z)\phi(z)\right\}\ket0
$$
now using Wick's theorem we get 3 terms where x and y are connected and 12 terms where x is connected to z and y is connected to z.
$$
= 3\left(\frac{-i\lambda}{4!}\right)D_F(x-y)\int\text d^4z D_F(z-z)^2
$$
$$
+ 12\left(\frac{-i\lambda}{4!}\right)\int\text d^4z D_F(x-z)D_F(y-z)D_F(z-z)
$$
These terms can be understood as two different Feynman Diagrams.
![[Pasted image 20241206030203.png]]
A more complicated Feynman Diagram is given by the formula
![[Pasted image 20241206140102.png]]
Where we have three free continuous variables $z,w,u$. We can rename each variable to each other which results in $3!$ Diagrams. Looking at the $z$ fields we can choose 2 fields to contract with each other, resulting in $3$ choices, and then we have two choices left to connect to outer fields, so $3\cdot2$ choices. This can then also be done for the $w,u$ fields. The $u,w$ fields, when renamed, interact completely equivalently, meaning that we are overcounting by 2, so we have to divide by 2 to get the actual number. All these diagrams can be represented by one diagram
![[Pasted image 20241206145546.png]]
We calculate a Feynman Diagrams Symmetry factor through the procedure 
![[Pasted image 20241206160727.png]]
From this we get the result
$$
\bra 0 T\left\{\phi_{I,x}\phi_{I,x}\exp\left[-i\int\text dt H_I(t)\right]\right\}\ket0 = \begin{pmatrix}
\text{sum of all possible}\\
\text{diagrams of two}\\
\text{external points}
\end{pmatrix}
$$
And the Feynman rules in position space
![[Pasted image 20241206161213.png]]
and in momentum space
![[Pasted image 20241206162328.png]]

Finally,
$$
\bra\Omega T[\phi(x_1)\cdots\phi(x_n)]\ket\Omega = \begin{pmatrix}
\text{sum of all connected diagrams}\\
\text{with $n$ external points}
\end{pmatrix}
$$


# 42
## The S-Matrix
the cross section is defined by
$$
\sigma = \frac{\text{number of scattering events}}{\rho_A\ell_A\rho_B\ell_B A}
$$
between two clouds of particles with length $\ell$, particle density $\rho$ and cross sectional area $A$.

We get the scattering amplitude with
$$
f(E) \propto \frac{1}{E-E_0 + i\Gamma/2},\;\;\;\; \sigma \propto |f(E)|^2
$$
And for our use
$$
f = \frac{1}{p^2-m^2 + im\Gamma} \approx \frac{1}{2E_p(p^0 - E_p + i(m/E_o)\Gamma/2)}
$$
with which we can get the decay rate of an unstable particle
$$
\tau = (m/E_p)\Gamma
$$

#### Scattering Amplitudes
We will want to calculate scattering amplitudes. We define the state
$$
\ket\phi = \int\text d\tilde p \frac{1}{\sqrt{2E_p}}\phi(k)\ket k, \;\; \ket k = \sqrt{2E_k}a_k^\dagger\ket 0
$$
with usual normalizing conditions. The probability we want to compute is
$$
\mathcal P = |\langle\underbrace{\phi_1\phi_2\cdots}_\text{present}|\underbrace{\phi_A\phi_B}_{\text{past}}\rangle|^2
$$
where we call the past state the in and the present state the out particle. The present state is a state of several wavepackets for each final-state particle. We relate the probability to the idealized state vectors defined before
$$
\langle p_1p_2\cdots|k_Ak_B\rangle_\text{in}
$$
As these states are the time evolutions after an infinite amount of time
$$
\langle p_1p_2\cdots|k_Ak_B\rangle_\text{in} = \lim_{T\rightarrow\infty}\langle p_1p_2|e^{-iH(2T)}|k_Ak_B\rangle
$$
and thus we define
$$
\langle p_1p_2\cdots|k_Ak_B\rangle_\text{in} := \langle p_1p_2\cdots|S|k_Ak_B\rangle
$$
where we isolate the interaction part $T$ by $S = 1+ iT$. We can then apply momentum conservation and we get
$$
\langle p_1p_2\cdots|iT|k_Ak_B\rangle = (2\pi)^4 \delta(k_A+k_b-\Sigma p_f)\cdot i\mathcal M(k_A,k_b\rightarrow p_f)
$$
### The scattering Matrix $i\mathcal M$
$$
i\mathcal M = \text{sum of all connected, amputated diagrams}
$$
The derivation makes no sense, haven't understood it yet



# 43

# 44

# 45

# 46

# 47
