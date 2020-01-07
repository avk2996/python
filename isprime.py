#checking whether thge number is prime or not
def isPrime(n):
	if n<0: 
		print('the number is negative. please input positive number')
	if n>0:
		if n == 2:
			return True
		else:
			for i in range(2,n):
				if n%i == 0:
					return False
				else:
					return False
	
