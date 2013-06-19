# Enter your answrs for chapter 7 here
# Name:Olha Vasylevska


# Ex. 7.5
import math


def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)


def estimate_pi():
	sum = 0
	k = 0
	koef = 2 * math.sqrt(2) / 9801
	while True:
		a = factorial(4*k) * (1103 + 26390*k)
		b = factorial(k)**4 * 396**(4*k)
		formula = koef * a / b
		sum += formula
		
		if abs(formula) < 1e-15: break
		k += 1

	return 1 / sum

print estimate_pi()


# How many iterations does it take to converge?
2 iterations