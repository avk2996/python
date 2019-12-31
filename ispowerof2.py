def isPowerof2(n):
  if n == 1:
    return True
  if n % 2 == 1:
    return False
  return isPowerof2(n // 2)

isPowerof2(2)
isPowerof2(16)
isPowerof2(15)
