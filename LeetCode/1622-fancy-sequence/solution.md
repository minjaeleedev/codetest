# Introduction

We can combine several `addAll` operations and `multAll` operations into a single operation, represented by the pair $(a, b)$, which transforms any integer $x$ into $ax + b$:

- Initially, $(a, b) = (1, 0)$.
- When we encounter the `addAll(inc)` operation, we increase $b$ by `inc`.
- When we encounter the `multAll(m)` operation, we multiply both $a$ and $b$ by $m$.

We use the array $v$ to store the original sequence (that is, the values inserted by each `append(val)` operation). We also use two arrays $a$ and $b$ to store the pairs described above, where $(a_i, b_i)$ represents the result obtained by condensing all operations before $v_i$ is added to $v$.

When we encounter the operation `getIndex(idx)`, we consider both $(a_{idx}, b_{idx})$ and $(a_l, b_l)$:

- Before $v_{idx}$ is inserted into $v$, all previous operations can be condensed into $(a_{idx}, b_{idx})$.
- So far, all operations can be summarized as $(a_l, b_l)$.

Therefore, the operation applied to $v_{idx}$ is equivalent to transforming the pair $(a_{idx}, b_{idx})$ into $(a_l, b_l)$, which we denote as $(a_o, b_o)$. In other words,

$$
\begin{cases}
a_{idx} \cdot a_o = a_l \\
b_{idx} \cdot a_o + b_o = b_l
\end{cases}
$$

The answer to the `getIndex(idx)` operation is therefore

$$a_o \cdot v_{idx} + b_o$$

How do we solve for $a_o$ and $b_o$? From the equations above, we obtain

$$
\begin{cases}
a_o = \dfrac{a_l}{a_{idx}} \\[6pt]
b_o = b_l - b_{idx} \cdot \dfrac{a_l}{a_{idx}}
\end{cases}
$$

At first glance this seems straightforward, but we must note that after many `addAll` and `multAll` operations, $(a, b)$ may become very large, exceeding the range of integer types in most programming languages. One solution would be to use high-precision arithmetic, but that would make the implementation significantly more complex.

Fortunately, the problem only requires the result modulo $10^9 + 7$, which allows us to use the concept of a **modular multiplicative inverse**.

---

# Prerequisites

Let the modulus be $m$ (where $m = 10^9 + 7$ in this problem). For an integer $a$, if there exists another integer $a^{-1}$ ($0 < a^{-1} < m$) such that

$$a \cdot a^{-1} \equiv 1 \pmod{m}$$

then $a^{-1}$ is called the **multiplicative inverse** of $a$.

If $a$ is a multiple of $m$, then $a^{-1}$ clearly does not exist. When $a$ is not a multiple of $m$, we have

$$a \cdot a^{-1} = km + 1, \quad k \in \mathbb{N}$$

Rearranging gives

$$a^{-1} \cdot a - k \cdot m = 1$$

If $m$ is prime, then according to Bézout's identity, $\gcd(a, m) = 1$, which guarantees that integers $a^{-1}$ and $k$ satisfying the equation exist.

If $(a_0^{-1}, k_0)$ is one solution, then

$$(a_0^{-1} + cm, \; k_0 + ca), \quad c \in \mathbb{Z}$$

are also solutions. Therefore, there must exist a solution $a^{-1}$ such that

$$0 < a^{-1} < m$$

which is exactly the multiplicative inverse we seek.

How can we compute $a^{-1}$? A simple method is to use **Fermat's Little Theorem**, which states that

$$a^{m-1} \equiv 1 \pmod{m}$$

Thus,

$$
\begin{aligned}
a^{m-1} \cdot a^{-1} &\equiv a^{-1} \pmod{m} \\
\Rightarrow \quad a^{m-2} \cdot a \cdot a^{-1} &\equiv a^{-1} \pmod{m} \\
\Rightarrow \quad a^{m-2} &\equiv a^{-1} \pmod{m}
\end{aligned}
$$

Therefore, the multiplicative inverse of $a$ is

$$a^{-1} = a^{m-2} \mod m$$

We can compute $a^{m-2}$ efficiently using **fast exponentiation**, which runs in $O(\log m)$ time. For more details, see the editorial for *50. Pow(x, n)*.

The multiplicative inverse allows us to convert division into multiplication in modular arithmetic. For example,

$$\frac{b}{a} \equiv b \cdot a^{-1} \pmod{m}$$

This works because multiplication satisfies the distributive property under modulo:

$$(a \times b) \bmod m = ((a \bmod m) \times (b \bmod m)) \bmod m$$

Division, however, does not satisfy this property directly. Using the multiplicative inverse allows us to safely perform division under modulo arithmetic.

---

# Approach 1: Use modular inverse for the getIndex operation

## Intuition

From the equations derived earlier,

$$
\begin{cases}
a_o = \dfrac{a_l}{a_{idx}} \\[6pt]
b_o = b_l - b_{idx} \cdot \dfrac{a_l}{a_{idx}}
\end{cases}
$$

we can replace division with multiplication using the multiplicative inverse:

$$
\begin{cases}
a_o \equiv a_l \cdot a_{idx}^{-1} \pmod{m} \\
b_o \equiv b_l - b_{idx} \cdot a_l \cdot a_{idx}^{-1} \pmod{m}
\end{cases}
$$

The final answer is

$$(a_o \cdot v_{idx} + b_o) \bmod m$$

## Complexity Analysis

Let $n$ be the maximum number of elements contained in the sequence $v$.

- **Time complexity**: $O(\log m)$

  The `getIndex(idx)` operation takes $O(\log m)$ time because it requires computing a modular inverse. All other operations take $O(1)$ time.

- **Space complexity**: $O(n)$.

---

# Approach 2: Use multiplicative inverse during the append operation

## Intuition

In the Introduction we observed that:

> The operation applied to $v_{idx}$ is equivalent to transforming the pair $(a_{idx}, b_{idx})$ into $(a_l, b_l)$.

Instead of solving the system of equations, we can directly compute

$$a_l \cdot \frac{v_{idx} - b_{idx}}{a_{idx}} + b_l$$

However, this expression cannot be evaluated safely without using a multiplicative inverse, because we cannot guarantee that $v_{idx} - b_{idx}$ is divisible by $a_{idx}$.

Even with high-precision arithmetic, fractional values could appear and propagate errors. By using the multiplicative inverse, we instead compute

$$a_l \cdot (v_{idx} - b_{idx}) \cdot a_{idx}^{-1} + b_l$$

which ensures that all operations remain within integer arithmetic under modulo.

Therefore, when we encounter an `append(val)` operation and all previous operations are summarized as $(a_{l'}, b_{l'})$, we transform the value before storing it:

$$(val - b_{l'}) \cdot (a_{l'})^{-1}$$

When we later process `getIndex(idx)`, we can simply return

$$a_l \cdot v_{idx} + b_l$$

## Complexity Analysis

Let n be the maximum number of elements that can be included in the sequence v.

- **Time complexity**: $O(\log m)$

The append(val) operation requires computing a modular inverse and therefore takes O(logm) time. All other operations take O(1) time.

- **Space complexity**: $O(n)$.