# Enter your code here. Read input from STDIN. Print output to STDOUT
"""Problem Statement
You wish to help Ashish, who possesses a collection of N strings, some of which may be duplicated, and has been assigned the task of finding the kth unique string.

If the number of unique strings is less than k, he needs to display -1. Considering you are Ashish's best friend can you assist him with this challenge?

Input Format
The first line contains an integer N denoting the number of strings.

The next N lines contain strings.

The next line contains an integer k.

Output Format
The output contains the kth distinct string. If there are less than k unique string display -1."""


n = int(input())
string= []
for _ in range(n):
  string.append(input().strip())
k = int(input())
from collections import Counter
count = Counter(string)
unique = []
for s in string :
  if count[s] == 1:
    unique.append(s)
if k <= len(unique):
    print("output: ",unique[k - 1])
else:
    print(-1)