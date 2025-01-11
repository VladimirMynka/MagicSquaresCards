# Примеры тривиального и нетривиального квадратов
### Info type
3_tfmn
### Keywords
~Dir2Примеры, ~неполные квадраты, ~квадратный магический квадрат, ~тривиальный, ~нетривиальный
### Text
Ниже приведены примеры тривиального и нетривиального квадратов 3/9:
$$
\begin{matrix}
X & X & X \\
O & O & O \\
O & O & O
\end{matrix}
\Leftrightarrow
\begin{cases}
E + x = a^2 \\
E - x + y = b^2 \\
E - y = c^2
\end{cases}
\Leftrightarrow
\begin{cases}
E = (a^2 + b^2 + c^2) / 3 \\
x = (2a^2 - b^2 - c^2) / 3 \\
y = (a^2 + b^2 - 2c^2) / 3
\end{cases}
$$
a, b, c - просто параметры.
Тривиальный:
$$
\begin{matrix}
O & O & O \\
X & X & X \\
O & O & O
\end{matrix}
\Leftrightarrow
\begin{cases}
E = e^2 \\
E - x - y = d^2 \\
E + x + y = f^2
\end{cases}
\Leftrightarrow
\begin{cases}
E = e^2 \\
x + y = e^2 - d^2 \\
x + y = f^2 - e^2
\end{cases}
$$
Нетривиальный: Вынуждены решать $2e^2 = f^2 + d^2$. e, d, f - теперь переменные.
```
