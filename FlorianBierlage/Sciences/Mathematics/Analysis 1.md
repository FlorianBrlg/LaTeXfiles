# 2024

# 41
## Natural Numbers and Mathematical Induction
We define the Natural numbers, Integers, and Rational numbers.

$$
\mathbb N = \{1,2,\cdots\}
$$
$$
\mathbb N_0 = \{0,1,2,\cdots\} = \mathbb N \cup \{0\}
$$
$$
\mathbb Z = \{\cdots,-2,-1,0,1,2,\cdots\}
$$
$$
\mathbb Q = \left\{\frac{p}{q}|p\in\mathbb Z,\,q\in\mathbb N\right\}
$$
### Mathematical induction
let $A(n)$ be a statement about a natural number $n\in\mathbb N$. Then, if the following statements are true then $A(n)$ is true for all $n$.
- Induction hypothesis: $A(1)$ is true
- Induction step: For all $n$, if $A(n)$ is true, then $A(n+1)$ is true.
This can also be done for $n_0>1$, where the statement is changed such that $A(n)$ is true for all $n\geq n_0$. 

#### Def: Recursive Functions
A function can be defined recursively, by defining statements, $f(1), f(2), \cdots, f(n)$ and then defining an $f(n+1)$ that depends on the previous statements.
###### example (Fibonacci numbers):
let $F_0$ = 0, $F_1 = 1$, and $F_{n+2} = F_{n+1} + F_n$, then $F_n$ is called the $n$th Fibonacci number.

### Factorials and Binomial Coefficients
#### Def: Factorial
We define a function for all $n\in\mathbb N$, called the Factorial, designated $n!$. We define $0! = 1$ and $(n+1)! = n!\cdot (n+1)$. 
The factorial is the number of ways to rearrange (permute) $n$ elements.

#### Def: Binomial Coefficient
for $n\in\mathbb N_0$ and $k\in\mathbb N_0$ with $k\leq n$ we define
$$
{n\choose k} = \frac{n!}{k!(n-k)!}
$$
##### Recursive Formula for Binomial Coefficients
$$
{n\choose k} + {n\choose k+1} = {n+1\choose k+1}
$$
#### Def: Binomial Formula
for an $n\in\mathbb N$ and for $a,b\in \mathbb R$ we have
$$
(a+b)^n = \sum_{k=0}^n {n\choose k} a^k b^{n-k}
$$

## Real Numbers
##### Lemma 1 (if $p^2$ even, then $p$ even): 
let $p\in\mathbb N$, then if $p^2$ is even, then $p$ is even.
*Proof:* This is equivalent to if $p$ is uneven then $p^2$ is uneven. So, let $p$ be uneven, so $p = 2k + 1$. Calculating $p^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$. So we see that $p^2$ is uneven. Therefore, if $p^2$ is even, then $p$ must be even.

$\mathbb Q$ is not "complete".

##### Example
The Diagonal of the Unit square has the length $\sqrt 2$, and $\sqrt 2 \notin \mathbb Q$. 

let $\sqrt 2\in \mathbb Q$, then there exist irreducible numbers $p,q\in \mathbb N$ such that $p/q = \sqrt 2$. Square both sides and multiply by $q^2$. Then $p^2 = 2q^2$. So $p^2$ is even, and as such $p$ is even by Lemma 1, and $2q^2$ is even. As $2q^2 = p^2$ and $p$ is even, so $p = 2k$, we have that $2q^2 = 4k^2$ which means that $q^2 = 2k^2$ so $q^2$ is also even, and with that $q$ is even. this means that our ratio $p/q$ is still reducible, contradicting the original hypothesis, therefore $\sqrt2$ must not be in $\mathbb Q$. 

This is an example of a hole that is present in $\mathbb Q$ that we seek to fill in $\mathbb R$. 

### Field axioms of $\mathbb R$
We define two operations on $\mathbb R$.
- Addition $+:\mathbb R\times\mathbb R \rightarrow \mathbb R,\; (a,b)\rightarrow a+b$
- Multiplication $\cdot :\mathbb R\times\mathbb R\rightarrow\mathbb R,\;(a,b)\rightarrow ab$
$\mathbb R$ must obey the following 5 field properties
1. Commutativity: $a+b = b+a$, and $ab = ba$.
2. Associativity: $(a+b) + c = a + (b+c)$, and $(ab)c = a(bc)$.
3. Distributive property: $a(b+c) = ab + ac$.
4. Neutral Element: There exist $0,1\in\mathbb R$ such that $a + 0 = a$ and $a\cdot 1 = a$.
5. Inverse Element: For all $a\in\mathbb R$ there exist $(-a), a^{-1}\in\mathbb R$ such that $a + (-a) = 0$ and $aa^{-1} = 1$.

$\mathbb R$ also follows the ordering axioms, that is
- For all $a\in\mathbb R$ one of the following statements is true $$
a>0,\;\; a=0,\;\; -a>0
$$
- From $a>0$ and $b>0$ it follows that $a + b > 0$ and $ab > 0$.

##### Lemma 2 (Bernoulli Inequality)
Let $x\in\mathbb R$ such that $x>-1$ and $x\neq 0$. Let $n\in\mathbb N$ such that $n\geq 2$, then
$$
(1+x)^n > 1 + nx
$$
*Proof:* proof by Induction.
Let $x\neq 0$ and $x>-1$. Let $n = 2$.
$$
(1+x)^2 = 1 + 2x +x^2 > 1+2x,\;\;\;\;\;\text{from }x^2>0
$$
We assume the statement to be true for $n$ and we check for $n+1$.
$$
(1+x)^{n+1} = (1+x)^n(1+x) > (1+nx)(1+x) = 1 + nx +x +nx^2
$$
$$
= 1+(n+1)x+nx^2 > 1+(n+1)x
$$
Therefore we have $(1+x)^{n+1} > 1+(n+1)x$.
#### Def: Absolute value
For all $x\in\mathbb R$ we define
$$
|x| = \cases{x ,& if $x\geq0$\\ -x, &if $x<0$}
$$
This is called the absolute value of $x$.
###### Lemma 3 (Absolute Value Properties)
We have the following properties of the Absolute value
1. $|ab| = |a||b|$
2. $|a+b| \leq |a| + |b|$
3. $|a-b| \geq ||a|-|b||$
*proofs:*
1 Let $a,b\in\mathbb R$. Let both be positive. Then
$$
ab > 0 \rightarrow |ab| = ab. 
$$
$$
|a| = a, |b| =b\rightarrow |a||b| = ab
$$
Let one be negative (here $a<0$). Then
$$
ab < 0\rightarrow |ab| = -ab
$$
$$
|a| = -a, |b|=b\rightarrow |a||b|=-ab
$$
let both be negative. Then
$$
ab > 0\rightarrow |ab| = ab
$$
$$
|a| = -a, |b|=-b\rightarrow |a||b| = (-a)(-b) = ab
$$
Therefore $|ab| = |a||b|$ in all cases.

2 Let $a,b\in\mathbb R$. Then we have
$$
a\leq |a|,\;b\leq|b|\rightarrow a + b \leq |a| + |b|
$$
and
$$
-a\leq |a|,\,-b\leq|b|\rightarrow -(a+b) \leq |a| +|b|
$$
and therefore
$$
|a+b| \leq |a|+|b|
$$
3 Let $a,b\in\mathbb R$. Then
$$
|a| = |a+b-b| \leq |a-b|+|b| \rightarrow |a|-|b| \leq |a-b|
$$
$$
|b| = |b+a-a| \leq |b-a| +|b| \rightarrow |b|-|a| = -(|a|-|b|) \leq |b-a| = |a-b|
$$
and with that 
$$
||a|-|b|| \leq |a-b|
$$



# 42

# 43

# 44

# 45

# 46
Subsequences and Series
# 47

Radius of Convergence and Topology.

The Radius of convergence can be calculated with:
- Cauchy Hadamard: $$\sum_n a_n x^{b_n},\;\;\;\frac{1}{R} = \limsup_{n\rightarrow\infty} |a_n|^{1/b_n}$$
- Euler: $$\sum_n a_n x^n,\;\;\;\; \frac{1}{R} = \lim_{n\rightarrow\infty} \left|\frac{a_{n+1}}{a_n}\right|$$
A set $M$ is open in $X$ is open if
$$
\forall x\in M \exists \epsilon>0(B_\epsilon(x)\subset M)
$$
And it is closed if
$$
\exists x\in M \forall\epsilon>0\exists z(z\in B_\epsilon(x) \wedge z\in X\backslash M)
$$
with $B_\epsilon(z)$ being the open Ball:
$$
B_\epsilon(z) = \{x\in X | d(x,z)<\epsilon\}
$$

# 48

# 49

# 50

# 51

# 52

# 2025
# 1

# 2

# 3