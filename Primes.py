t = int(input("Schranke der Zahlen: "))
v = int(input("Sollen nicht-Primzahlen mit angezeigt werden? (1 = JA    0 = NEIN) "))

for n in range(2,t+1):
	for x in range(2,n):
		if v == 1:
			if n % x == 0:
				print(n, 'equals', x, '*', n//x)
				break
	else:
		print(n,"ist eine Primzahl")

print("")
input("Zum beenden des Programms drücken Sie Enter")
print("")
