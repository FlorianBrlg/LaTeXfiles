
# Electrostatics

## Coulomb's Law
The force between two points with charges $q_1$ and $q_2$ is
$$
F = kq_1q_2\frac{r_1-r_2}{|r_1-r_2|^3} = kq_1q_2\frac{\tilde r}{|\tilde r|^3}
$$
where $k$ is a proportionality constant. In esu $k=1$, in SI units $k=\frac{1}{4\pi \epsilon}$. 
## Electric Field
The electric field is a field that gets created by an electric charge $q_1$. It is defined at every point $r$ in space by
$$
E(r) = kq_1\frac{r-r_1}{|r-r_1|^3} = kq_1\frac{\tilde r}{|\tilde r|^3}
$$
If there is only 1 charge, $r_1$ is normally set to $0$.
If there are multiple electric fields $E_i$ then the total electric field is the sum of all of them.
$$
E(r) = \sum_i E_i = \frac{1}{4\pi\epsilon}\sum_i q_i\frac{r-r_i}{|r-r_i|^3}
$$
If instead of explicit charges we have a charge density $\rho(x)$ then we substitute the sum for an integral
$$
E(r) = \frac{1}{4\pi\epsilon}\int\text dx' \rho(x')\frac{r-x'}{|r-x'|^3}
$$
where $\text d x'$ is the integral over all space, $\text dx\text dy\text dz$.