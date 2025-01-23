# 41

## Group Axioms
a Group $\mathcal G$ is a set with an operator $\star$ that obeys the following properties:
1. **Closure** For every pair of elements $g_i, g_j \in \mathcal G$ there exists a $g_k\in \mathcal G$ such that$$g_i\,\star\,g_j=g_k $$
2. **Associativity** The $\star$ operation is associative. For all $g_i,g_j,g_k \in \mathcal G$$$(g_i\,\star g_j)\star g_k= g_i\,\star(g_j\,\star g_k) $$
3. **Unit element** $\mathcal G$ contains a unique element $I$ such that for all $g\in\mathcal G$ $$I\,\star g = g\,\star I = g$$this means that $I\,\star I = I$
4. **Inverse Element** For all $g\in \mathcal G$ there exists an element $g^{-1}\in\mathcal G$ such that$$g\,\star g^{-1} = g^{-1}\,\star g=I$$
If a Group contains a finite number $n$ elements then it is called a finite Group of order $n$.

For every integer $n$ there is a group $\mathbb Z_n$ called the cyclic group with the property that its $n$th element is $a^{n-1}$ and that $a^n = I$.

For every integer $n$ there is a group of order $2n$ called $\mathcal D_n$ the Dihedral group. It is the group of symmetries of an $n$-gon

## Subgroups
A Group $\mathcal G$ contains a subgroup $\mathcal G_s$ if it contains a subset $A \subset \mathcal G$ that is a group under the same operation $\star$.

Example: $\mathbb Z_4$ contains $\mathbb Z_2$.

### Direct Product
Let $\mathcal G$ and $\mathcal K$ be groups with element $g_i$ and $k_j$ respectively. where $i = 1,\cdots, n_g$ and $j= 1,\cdots, n_k$. We define a new element $(g_a, k_i$) with the multiplication rule
$$
(g_a,k_i)(g_b,k_j) =(g_a\,\star g_b, k_i\,\star k_j)
$$
These are elements of the direct product $\mathcal G \times \mathcal K$, also called the Kronecker product. Here, $\mathcal G\times \mathcal K \cong \mathcal K \times \mathcal G$.

### Lagrange's Theorem
If a group $\mathcal G$ of order $N$ has a subgroup $\mathcal H$ of order n, then $n$ divides $N$.
The ratio $N/n=k$ is called the index of $\mathcal H$ in $\mathcal G$.

from Lagrange's Theorem follows:
let $\mathcal G$ be a finite group. Then you have the sequence $a^m$, $m=1,\cdots$. As the Group is finite we have two indeces $k,l$ such that $a^k = a^l$, so we have an element $a^{k-l} = I$. The element $a$ then generates a cylic subgroup, and from Lagrange's Theorem we know that $k-l$ divides $|G|$.

$$
\mathcal Z_6 = \mathcal Z_2 \times \mathcal Z_3
$$
## Presentations
A presentation of a finite group is a list of its generators and how they interact. One group may have several presentations
$$
\mathcal D_3 = \langle a,b| a^3 = b^2 = e; bab^{-1} = a^{-1}\rangle
$$
$\mathcal D_3$ has two generators, so it is of *rank* two.

## Normal Subgroup
Let $\mathcal H$ and $\mathcal G$ be groups, with $\mathcal H \subset \mathcal G$. If all elements of $\mathcal H$ are left in $\mathcal H$ under conjugation with all elements of $\mathcal G$ then $\mathcal H$ is a normal subgroup.
$$
g\,h_i\, g^{-1} = h_j\in\mathcal H,\;\;\;\forall g\in\mathcal G
$$
We write $\mathcal H \triangleleft \mathcal G$.
A group without normal subgroups is called *simple*



# 42


# 43

# 44

# 45

# 46

# 47



12.7
13.3
15.3
8.6
9.5
8


| Sheet | Points | out of |
| ----- | ------ | ------ |
| 1     | 12.7   | 20     |
| 2     | 13.3   | 20     |
| 3     | 15.3   | 20     |
| 4     | 8.6    | 20     |
| 5     | 9.5    | 20     |
| 6     | 8      | 20     |
| 7     | 3      | 20     |
| 8     | 7      | 20     |
| 9     |        | 20     |
| 10    |        | 20     |
| 11    |        | 20     |
| 12    |        | 20     |
| 13    |        | 20     |
