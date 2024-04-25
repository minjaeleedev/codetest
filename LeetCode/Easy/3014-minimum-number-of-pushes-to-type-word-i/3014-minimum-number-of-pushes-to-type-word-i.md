## 3014. Minimum Number of Pushes to Type Word I

You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

### Example 1:

> Input: word = "abcde"<br/>
> Output: 5<br/>
> Explanation: The remapped keypad given in the image provides the minimum cost.<br/>
> "a" -> one push on key 2<br/>
> "b" -> one push on key 3<br/>
> "c" -> one push on key 4<br/>
> "d" -> one push on key 5<br/>
> "e" -> one push on key 6<br/>
> Total cost is 1 + 1 + 1 + 1 + 1 = 5.<br/>
> It can be shown that no other mapping can provide a lower cost.

### Example 2:

> Input: word = "xycdefghij"<br/>
> Output: 12<br/>
> Explanation: The remapped keypad given in the image provides the minimum cost.<br/>
> "x" -> one push on key 2<br/>
> "y" -> two pushes on key 2<br/>
> "c" -> one push on key 3<br/>
> "d" -> two pushes on key 3<br/>
> "e" -> one push on key 4<br/>
> "f" -> one push on key 5<br/>
> "g" -> one push on key 6<br/>
> "h" -> one push on key 7<br/>
> "i" -> one push on key 8<br/>
> "j" -> one push on key 9<br/>
> Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.<br/>
> It can be shown that no other mapping can provide a lower cost.
 

### Constraints:

- t 1 <= word.length <= 26
- word consists of lowercase English letters.
- All letters in word are distinct.