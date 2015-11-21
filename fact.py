def fact(x):
	if x == 1:
		return 1
	
	return x * fact(x - 1);
	
user_input = raw_input('input: ')

print fact(int(user_input))