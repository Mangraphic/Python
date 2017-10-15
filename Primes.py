t = int(input("Limit: "))
v = int(input("Show non-prime numbers? (1 = YES    0 = NO) ")) #reason why is shown in console

for n in range(2,t+1):
	for x in range(2,n):
		if n % x == 0:
			if v == 1:
				print(n, 'equals', x, '*', n//x)
				break
			elif v == 0:
				break
	else:
		print(n,"is a prime number")

print("")
input("To exit the programm press enter")
