t = int(input("Limit of Numbers to count to: "))
v = int(input("Include non-prime numbers? (1 = YES    0 = NO) "))

for n in range(2,t+1):
	for x in range(2,n):
		if v == 1:
			if n % x == 0:
				print(n, 'equals', x, '*', n//x)
				break
	else:
		print(n," is a prime number")

print("")
input("To exit the programm press ENTER")
print("")
