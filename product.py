def product(list):
	multiplication = 1
	for i in list:
		multiplication *= i
	return multiplication
print product([4,5,5])