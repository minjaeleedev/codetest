## Approach 1: Sorting and Median
### Intuition

First, let's think about when it's possible to make all grid elements equal.

Consider any two numbers in the grid, a and b, and a number x. 
Suppose we want to make both a and b equal to some value v. 
The only operation allowed is adding or subtracting xsome number of times. 
This means we must be able to reachvfrom bothaandbusingx`.

For this to be possible, the differences v - a and v - b must both be multiples of x, or equivalently:

(v−a)%x=0and(v−b)%x=0

Rearranging this, we get:

a%x=b%x=v%x

This tells us that all numbers in the grid must have the same remainder when divided by x. Otherwise, it is impossible to transform them into a single value using only x-sized steps.

For example, if grid = [[1, 8], [3, 5]] and x = 2, we cannot make all elements equal to any odd value because 8 is even, and adding 2 any number of times will always result in an even number. Similarly, we cannot make all elements equal to any even value because 1, 3, and 5 are odd, and adding 2 will always keep them odd. Since we cannot make all numbers have the same parity, it is impossible to make the grid uni-value.

Thus, our first step is to check if all numbers in the grid have the same remainder when divided by x. If they don't, we immediately return -1. Otherwise, our goal is to find the smallest number of operations required.

To make things easier, note that the arrangement of numbers in the grid doesn’t affect our task at all, since we can apply operations to any number, no matter its position. So, we can simplify the problem by flattening the grid into a one-dimensional array.

Now, which value should we aim to make all numbers equal to?

If we pick a value too large, then the smaller numbers will need many additions of x to reach it.
If we pick a value too small, then the larger numbers will need many subtractions of x.
A natural choice is the median of the numbers.

Why? The median is the balancing point that minimizes the total distance numbers need to move. By choosing the median, we ensure that half of the numbers shift up and the other half shift down, naturally minimizing the total number of operations.
For example, consider grid = [[2, 4], [6, 8]] with x = 2:

If we make all values 8, we need 3 + 2 + 1 + 0 = 6 operations.
If we choose 4 (the median), the operations reduce to 1 + 0 + 1 + 2 = 4.
In fact, selecting the median of the numbers always results in the smallest number of operations.

The median value of a set of numbers is the value at which half of the numbers in the set are below it, and the other half are above it.

Click here for a formal proof

To find the median, we first sort the array in non-decreasing order and then pick the middle value. Next, we iterate through the array again to calculate how many operations are needed for each number to reach the median, and then we sum these operations.

In C++, we can avoid fully sorting the array by using the nth_element function. This operation runs in linear time and ensures that the desired element is placed at the index it would occupy in a fully sorted array. For the median, this means the element will be placed at the middle index.

Algorithm
Initialize:
an empty array, called numsArray to store all numbers.
a variable result = 0 to store the total number of operations.
Flatten the grid into numsArray, by iterating over its elements and pushing them into it.
Sort numsArray in non-decreasing order.
Initialize length to the size of numsArray.
Store the median of the array (numsArray[length / 2]) in finalCommonNumber.
For each number in numsArray:
If number % x != finalCommonNumber % x, return -1, as we found two elements in the array with different remainders when divided by x.
Otherwise, increment result by the number of operations needed for this element to become equal to finalCommonNumber, i.e. abs(finalCommonNumber - number) / x.
Return result.