# fmn-функция и c(m,n)
### Info type
3_tfmn
### Keywords
~Dir8fmn, ~неполные квадраты, ~квадратный магический квадрат, ~функция
### Text
Далее для удобства обозначим числитель dir-функции как f(m, n), а знаменатель как c(m, n). И теперь мы имеем аппарат для ёмкого описания всех нетривиальных 3-квадратных квадратов:
$$
\begin{matrix}
\text{группа} & \text{решение} & m(E, x, y) \\
\begin{matrix} O & X & O \\ O & O & X \\ O & O & O \end{matrix} & x = 4E^2dir(m, n) & m(k^2c(m, n), 4k^2f(m, n), y) \\
\begin{matrix} O & X & O \\ O & X & O \\ O & O & O \end{matrix} & y - x = 4E^2dir(m, n) & m(k^2c(m, n), x, 4k^2f(m, n) + x) \\
\begin{matrix} X & O & O \\ O & O & X \\ O & X & O \end{matrix} & y = 4A^2dir(m, n) & m(E, k^2c(m, n) - E, 4k^2f(m, n))
\end{matrix}
$$
Здесь мы видим сказанное выше: для каждой группы одна из переменных остаётся свободной. Для первой группы это y, для второй x, для третьей E.
```
