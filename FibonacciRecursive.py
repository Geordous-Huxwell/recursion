def fibRecursive(n):
	if(n == 1):
		return 0
	elif(n==2):
		return 1
	else:
		return fibRecursive(n-1)+fibRecursive(n-2)

print(fibRecursive(5))

def fib(n):
	fibNum = [0,1]
	for i in range(2,n):
		fibNum.append(fibNum[i-1]+fibNum[i-2])
		fibNum[i-2]=0
	return fibNum[n-1]

print(fib(2))