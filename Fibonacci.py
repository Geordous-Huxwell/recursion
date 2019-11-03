def fib(n):
	num1 = 0;
	num2 = 1;
	for i in range(1,n):
		if(i%2==0):
			num1 = num1 + num2
		else:
			num2 = num1 + num2
	if(n%2==0):
		return num2
	else:
		return num1

print(fib(50000))