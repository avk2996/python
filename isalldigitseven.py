def isAllDigitsEven(m):
  while m>0:
    if m%2 == 1:
      return False
    m //= 10
  return True
