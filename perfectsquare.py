def isPerfectSquare(n):
  r = 0
  while r*r < n:
    r += 1
  return r*r == n

print(isPerfectSquare(16),isPerfectSquare(17))
