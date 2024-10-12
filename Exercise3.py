n = 7
j = n + 2
k = j //4
for i in range(1, n+1):
    if (i <= k):
        print(" " * (k-i) + "*" * (2*i) + " " * (j-2*i-2*k) + "*" *(2*i) + " " * (k-i))
    else:
      print(" " * (i - 2*k+1) + "*" * (j-2*(i-2*k+1)) + " " * (i - 2*k+1))