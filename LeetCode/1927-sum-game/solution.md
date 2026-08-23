## Approach: Guess + Mathematical Induction Verification

### Intuition

#### Hint 1

If the number of question marks is odd, then Alice is definitely the winner.

#### Hint 1 Explanation

Since Alice goes first, the last question mark must be filled by Alice.

It is clear that, in the range [0,9], there is at most one digit d that can make the sum of the digits in the first half equal to the sum of the digits in the second half. Therefore, Alice can simply replace the last question mark with any digit other than d.

Thus, we only need to consider the case where the number of question marks is even.

#### Hint 2

If the number of question marks is 0, then Bob wins if and only if the sum of the digits in the first half equals the sum of the digits in the second half.

#### Hint 3

If the number of question marks is 2 and they appear on different sides, that is, one question mark is in the first half and the other is in the second half, then Bob wins if and only if the sum of the known digits in the first half equals the sum of the known digits in the second half.

#### Hint 3 Explanation

If the sum of the known digits in the first half is equal to that in the second half, Alice can choose either question mark and replace it with any digit d. Bob can then replace the other question mark with the same digit d. Therefore, Bob is guaranteed to win.

If the sums of the known digits in the two halves are not equal, Alice can choose the question mark in the half with the larger sum and replace it with 9. Since no digit greater than 9 can be chosen, Alice is guaranteed to win.

#### Hint 4

If the number of question marks is 2 and both appear on the same side, Bob wins if and only if the sum of the known digits on that side is exactly 9 less than the sum of the known digits on the other side.

Hint 4 Explanation

Bob can always ensure that the digits chosen for two consecutive question marks sum to 9. Specifically, if Alice replaces one question mark with a digit d, Bob can replace the other question mark with 9−d.

Therefore, if the above condition is satisfied, Bob is guaranteed to win. Otherwise:

If the difference exceeds 9, Alice replaces the question mark with 0.

If the difference does not exceed 9, Alice replaces the question mark with 9.

In either case, Bob cannot choose a digit in [0,9] that makes the sums of the two halves equal, so Alice is guaranteed to win.

#### Hint 5

Suppose the sum of the known digits in the first half is $n_0$, 
the number of question marks in the first half is $q_0$, 
the sum of the known digits in the second half is $n_1$, 
and the number of question marks in the second half is $q_1$. 
If $q_0+q_1$ is even, then Bob wins if and only if

$$ n_0 - n_1 = \frac {9}{2} (q_1 - q_0) \tag{1} $$

We can interpret this equation based on Hints 3 and 4. Without loss of generality, assume $q_0 \leq q_1 $.

- For the $q_0$
  question marks on the two sides, according to Hint 3, Alice and Bob can choose digits so that their contributions to the two halves cancel each other out.

- For the remaining $q_1-q_0$
  question marks in the second half, according to Hint 4, Alice and Bob can pair them up, with each pair contributing a total of 9.

- Therefore, for the sums of the two halves to become equal, the first half must initially have a sum that is $\frac {9}{2}(q_1-q_0)$ larger than the second half.

This gives Equation (1).

#### Hint 5 Explanation

We can prove Hint 5 rigorously using mathematical induction on the total number of question marks $q_0 + q_1$.

- According to Hints 3 and 4, Hint 5 holds when $q_0+q_1 = 2$ In this case, Bob is guaranteed to win if Equation (1) holds; otherwise, Alice is guaranteed to win. 

- Assume that Hint 5 holds when $q_0+q_1=k$. We now consider the case where $q_0+q_1=k+2$. Without loss of generality, assume $q_0 \leq q_1$.

- If Equation (1) already holds, then consider Alice's first move. If Alice chooses a question mark in the first half and replaces it with d, Bob replaces a question mark in the second half with the same digit d. If Alice instead chooses a question mark in the second half and replaces it with d, Bob replaces another question mark in the second half with 9−d. In both cases, the remaining game still satisfies Equation (1).

Therefore, the game can be reduced to the case of $q_0+q+1=k$, where, by the induction hypothesis, Bob is guaranteed to win.

- If Equation (1) does not hold, then we can write
$$ n_0 - n_1 = \frac {9}{2}(q_1-q_0) + \delta  $$
where $\delta \neq 0$

- If $\delta \gt 0 $, Alice replaces a question mark in the second half with 0.

If Bob chooses a question mark in the first half and replaces it with $d$, then

$$ (n_0 +d) - n_1 = \frac {9}{2}(q_1-q_0) +(\delta + d) \neq \frac {9}{2}((q_1-1)-(q_0-1))$$

Therefore, Equation (1) still does not hold.

If Bob instead chooses another question mark in the second half and replaces it with d, then

$$ n_0 - (n_1 +d) = \frac {9}{2}((q_1-2)-q_0) +(\delta + 9 - d) \neq \frac {9}{2}((q_1-2)-q_0)$$

Therefore, Equation (1) also does not hold.

- If $\delta \lt 0$, Alice replaces a question mark in the second half with 9.

    If Bob chooses a question mark in the first half and replaces it with d, then

    $$ (n_0 +d) - (n_1+9) = \frac {9}{2}(q_1-q_0) +(\delta -9+ d) \neq \frac {9}{2}((q_1-1)-(q_0-1))$$

    Therefore, Equation (1) still does not hold.

    If Bob instead chooses another question mark in the second half and replaces it with d, then


    $$ n_0 - (n_1 + 9 +d) = \frac {9}{2}((q_1-2)-q_0) +(\delta - d) \neq \frac {9}{2}((q_1-2)-q_0)$$

    Therefore, Equation (1) also does not hold.

In either case, the game can be reduced to the case of $q_0+q_1=k$ where Equation (1) does not hold. By the induction hypothesis, Alice is guaranteed to win.

Therefore, Hint 5 holds for all even values of $q_0+q_1$.

Finally, we traverse the string `num` to calculate $n_0$, $q_0$, $n_1$, and $q_1$. 
If $q_0+q_1$ is odd, Alice is guaranteed to win. 
Otherwise, the winner is determined by Equation (1).
