from collections import Counter

s = "leetcode"
Output: 0

freq = Counter(s)

for i in s:
    if freq[i] == 1:
        print(i)
        break
