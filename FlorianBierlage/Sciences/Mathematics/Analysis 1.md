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
### Completeness of $\mathbb R$
#### Def: Bounded Set, Upper (Lower) Bound
Let $M$ be a non-empty set, then $M$ is bounded above (below) if there exists a $k\in\mathbb R$ such that $x\leq k$ ($x\geq k$) for all $x\in M$. $k$ is then called an upper (lower) bound of $M$. $M$ is called Bounded if there is an upper and a lower bound.

#### Def: Supremum / Infimum
The Supremum is the smallest upper bound of the set, the infimum is the biggest lower bound of the set.
If the set $M$ is unbounded then we say that $\sup M = \infty$ and $\inf M = -\infty$. 

#### Axiom of Completeness
Every non-empty set $M\subset\mathbb R$ with an upper bound contains a supremum in $\mathbb R$. This is called $\sup M$.

#### Def: Maximum / Minimum
$m\in M$ is a Maximum (Minimum) of $M$, if $x\leq m$ ($x\geq m$) for all $x$. If $M$ has a Maximum (Minimum), then $\sup M = \max M$ ($\inf M = \min M$).

#### Theorem  
1. If $\sup M<\infty$ then for all $\epsilon>0$ there exists an $x\in M$ with $\sup M - \epsilon < x$
2. If $\sup M = \infty$ then for all $k>0$ there exists an $x\in M$ with $x>k$.
*proof:*
1. Proof by contradiction. Assume that the statement is untrue. Then there exists an $\epsilon>0$ for all $x\in M$ such that $\sup M - \epsilon \geq x$ which would mean that $\sup M - \epsilon$ is an upper bound, that is smaller than $\sup M$, which is a contradiction. Thus the Theorem holds.
2. Proof by contradiction. Assume that the statement is untrue. Then there exists a $k>0$ such that for all $x\in M$ $x\leq k$, that means that $k$ is an upper bound, but we know that there is no upper bound, so this is a contradiction. Thus the theorem holds.
# 42
Defining Intervals
- $[a,b] := \{x\in\mathbb R| a\leq x\leq b\}$ Closed Interval
- $(a,b) := \{x\in\mathbb R|a<x<b\}$ Open Interval
- $[a,b):=\{x\in\mathbb R|a\leq x< b\}$ Half open Interval
- $(a,b] := \{x\in\mathbb R|a<x\leq b\}$ Half open Interval
The length of these Intervals is $|a-b|$. 

#### Def: Nested Intervals
Let $I_n$ be a sequence of closed intervals with length $|I_n|$. Then $I_n$ is a nested Interval, if
1. $I_{n+1} \subset I_n$ for all $n\in\mathbb N$ 
2. $|I_n|\rightarrow 0$ for $n\rightarrow\infty$, so for all $\epsilon>0$ there exists an $I_n$ with $|I_n|<\epsilon$ 

##### Theorem: Nested Interval Principle
For every Nested Interval there exists an $x\in\mathbb R$ with $x\in\cap_n I_n$. 
*Proof:* With $I_n = [a_n,b_n]$ follows that $a_1 \leq \cdots \leq a_n \leq b_n \leq \cdots \leq b_1$. Let $M:= \{a_n|n\in\mathbb N\}$ then $b_n$ is an upper bound for all $n$. From the completeness of $\mathbb R$ we know that there exists an $a = \sup M$ such that $a_n \leq a \leq b_n$ for all $n$ and with that $a\in\cap_n I_n$. 

##### Lemma: Existence of $x/2$. 
let $x\in\mathbb R$ be a number. If $x\leq 0$ then there exists a number $x/2$ such that $x\leq x/2 \leq 0$. If $0\leq x$ then there exists a number $x/2$ such that $0\leq x/2 \leq x$.


##### Theorem: Existence of roots
For every $c\geq 0$ there exists exactly one $x\in\mathbb R_+ \cup \{0\}$ with $x^2 = c$. Then $x$ is the square root of $c$, $x = \sqrt c = c^{1/2}$. 
*Proof:*
Let $M = \{z\in\mathbb R| z\geq 0, z^2\leq c\}$. This set is not empty because $0\in M$. This set is bounded above 

### $\mathbb R$ is not countable

#### Def: Injectivity
a function $f:M\rightarrow N$ is injective if $f(x_1)=f(x_2) \rightarrow x_1=x_2$.
#### Def: Surjectivity 
a function $f:M\rightarrow N$ is surjective, if $\forall n\in N\exists m\in M (f(m) = n)$.
#### Def: Bijectivity
a function $f:M\rightarrow N$ is bijective if it is injective and surjective.

#### Def: Cardinality
two set $M$ and $N$ have an equal cardinality if there exists a bijective map from $M$ to $N$.
#### Def: Countability
a set $M$ is called countable if it is the empty set, if it is finite, or if it has an equal cardinality to $\mathbb N$. Otherwise it is uncountable.

##### Cantor's Theorem

## Complex Numbers

Add later

## Sequences

### Sequences, Convergence

#### Def: Sequence in $\mathbb R$, $\mathbb C$.
A sequence of complex (real) numbers is a map $f:\mathbb N \rightarrow \mathbb C$ ($\mathbb R$). We write $a_n := f(n)$.

#### Def: Convergence of a sequence
A sequence $a_n$ is called "convergent", if there exists an $a$ such that
$$
\forall \varepsilon>0\exists n_0\forall n>n_0 \;\;(|a_n-a|<\epsilon)
$$
And $a$ is called the Limit (Grenzwert) of a sequence.
If a sequence does not converge, then it diverges (it is divergent).
If the Limit is 0 then the sequence is a Nullfolge.

##### Def: Epsilon Neighborhood
We define the (open) Epsilon Ball, Epsilon Neighborhood as
$$
B_\epsilon(a) := \{z\in\mathbb C|\; |z-a|<\epsilon\}
$$
#### Def: Nearly All
Let $A(n)$ be a statement for $n\in \mathbb N$. $A(n)$ is true for nearly all $n$ if there exists an $n_0$ for which all $A(n)$ with $n>n_0$ are true.

##### Theorem: Uniqueness of the Limit
The Limit of a Sequence is Unique.
*Proof:* 

# 43
#### Def: Bounded Sequence
A Sequence $a_n$ is called bounded, if there is an $M\in \mathbb R$ such that $|a_n|\leq M$ for all $n\in\mathbb N$.

##### Theorem: Converging Sequences are Bounded
*Proof:* Let $n>n_0$ such that $|a_n - a| < 1$. Then we have $|a_n| = |a_n - a + a| \leq |a_n - a| + |a|$ which then, substituting the previous expression gives
$$
|a_n| < 1 + |a|
$$
Then we can choose a bound $M := \max(1+|a|, a_{n_0-1}, a_{n_0-2},\cdots,a_1,a_0)$

##### Theorem: Calculation rules for limits
let $a_n,b_n$ be sequences with $a_n\rightarrow a$ and $b_n\rightarrow b$. then
- $a_n + b_n \rightarrow a+b$
- $a_n b_n \rightarrow ab$
- for $b\neq 0$ $a_n/b_n \rightarrow a/b$.
##### Theorem: More calculation rules for limits
- $|a_n|\rightarrow|a|$
- $\bar a_n \rightarrow \bar a$
- $\text{Re } a_n \rightarrow \text{Re } a$
- $\text{Im }a_n\rightarrow \text{Im }a$
##### Theorem: Comparison rule for real sequences
let $a_n$ and $b_n$ be real sequences. If $a_n \leq b_n$ for nearly all $n$ then $a\leq b$.
*Proof:* let $\epsilon>0$ and $n_0$ such that
$$ a-\epsilon < a_n
$$
$$ b_n < b + \epsilon
$$
as well as
$$
a_n \leq b_n
$$
for all $n\geq n_0$. Then it follows that $a - b < 2\epsilon$. As $\epsilon$ is arbitrarily small this means that $a \leq b$. 
##### Theorem: Sandwich principle 
let $a_n,b_n,c_n$ be real sequences such that $a_n\rightarrow a,\,b_n\rightarrow a$. If $a_n \leq c_n\leq b_n$ for nearly all $n$ then $c_n\rightarrow a$.

#### Def: Asymptomatic Equality
Let $a_n,b_n$ be sequences. If $\lim_{n\rightarrow \infty}\,a_n/b_n = 1$ then they are asymptomatically equivalent.

#### Definition $\bar{\mathbb R}$
We define $\bar{\mathbb R} := \mathbb R \cup \{\infty\} \cup \{-\infty\}$

#### Def:  Divergence against $\pm\infty$
A sequence $a_n$ diverges against $\infty(-\infty)$, if for every $k\in\mathbb R$ there exists an $n_0$ such that $a_n\geq k (a_n\leq k)$ for all $n\geq n_0$.

### Monotone sequences

#### Def: Monotonically increasing / decreasing sequences
$a_n\subset\mathbb R$ is monotone increasing (decreasing) if $a_n\leq a_{n+1} (a_n\geq a_{n+1})$ for all $n\in\mathbb N$. If $a_n< a_{n+1}(a_n> a_{n+1})$ then it is strictly monotone increasing (decreasing).

##### Theorem: Every bounded monotone sequences converges
1. An increasing sequence converges against $\sup\{a_n|n\in\mathbb N\}$
2. A decreasing sequence converges against $\inf\{a_n|n\in\mathbb N\}$.
*proof:* 

##### Ex: Euler's number
The sequences $a_n =  \left(1+\frac{1}{n}\right)^n$ and $b_n = \left(1+\frac{1}{n}\right)^{n+1}$ define a nested Interval $I_n = [a_n,b_n]$, such that $|I_n|\rightarrow 0$, while $a_n\leq b_n$ for all $n\in\mathbb N$. 
*proof:* 

### Bolzano-Weierstraß Theorem

#### Def: Accumulation Point
For a sequence $a_n\subset \mathbb C$ the point $h\in\mathbb C$ is called an Accumulation Ppint if for every $\epsilon$ neighborhood of $h$ there exist infinitely many $n\in\mathbb N$ such that $a_n$ is contained in it. 

#### Def: Subsequence
let $a_n$ be a sequence and $n_n$ a strictly monotone increasing sequence in $\mathbb N$, then $a_{n_n}$ is a subsequence of $a_n$.

##### Theorem: Accumulation Point is limit of a subsequence
$h\in\mathbb C$ is an Accumulation Point of $a_n$ if and only if there exists a subsequence of $a_n$ that converges to $h$ 

##### Theorem: Bolzano Weierstraß, Real Version
Let $a_n\subset\mathbb R$ be bounded. Then $a_n$ has a converging subsequence. More precisely, $a_n$ has a biggest Accumulation point $h^+$ and a smallest accumulation point $h^-$. For every $\epsilon >0$ it is true that $h^- \leq a_n \leq h^+ + \epsilon$. For nearly all $n$. 
$$
h^+ := \limsup_{n\rightarrow\infty}a_n
$$
$$
h^- := \liminf_{n\rightarrow\infty} a_n
$$
##### Corollary: Bolzano Weierstraß
$a_n\subset\mathbb R$ converges if and only if $\limsup a_n = \liminf a_n$.

##### Theorem: Bolzano Weierstraß, Complex Version
Every bounded sequence in $\mathbb C$ has a converging subsequence.

### Cauchy Sequences

#### Def: Cauchy Sequence
a sequence $a_n\subset\mathbb C$ is Cauchy if for every $\epsilon>0$ there exists an $n_0$ such that
$$
|a_m-a_n|<\epsilon \;\;\;\;\;\;\forall m,n>n_0
$$
##### Cauchy Criteria
$a_n$ converges if and only if $a_n$ is a Cauchy sequence

## Series

### Converging Series
#### Def: Converging Series
For a sequence $a_n\subset \mathbb C$ you define a new sequence
$$
s_n := \sum_{k=1}^n a_k
$$
This sequence is called series. The sole $s_n$ are called partial sums. The Series is convergent, if the partial sum $s_n$ converges. If $s = \lim_{n\rightarrow\infty}s_n$ then we write $s=\sum_{k=1}^\infty a_n$.
### Convergence Criteria
#### Theorem: Cauchy-Criteria for Series
$\sum a_k$ converges if and only if for every $\epsilon>0$ there exists an $n_0$ such that $|a_{n+1} + \cdots a_{m}|<\epsilon$ for all $m>n\geq n_0$. 

#### Theorem: Direct Comparison Test
Let $|a_k|\leq|b_k|$. If $\sum |b_k|$ converges then $\sum a_k$ also converges, and $|\sum a_k|\leq \sum|b_k|$. If $\sum a_k$ diverges then $\sum |b_k|$ also diverges. 

#### Theorem: Leibniz Criteria for alternating Series
Let $a_n$ be a real monotone decreasing sequence converging to $0$, then $\sum (-1)^n a_n$ converges. For the Grenzwert we have that $|s-s_n|\leq a_{n+1}$ for all $n$. 


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