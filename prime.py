def is_prime(x):
	if x < 2:
		return False
	for n in range(2, x - 1):
		if x % n == 0:
			return False
	return True
print is_prime(2)
print is_prime(11)
print is_prime(15)