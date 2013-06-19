# Enter your answrs for chapter 6 here
# Name: Olha Vasylevska


# Ex. 6.6
def is_palindrome(word):
	length = len(word)
	for i in range (length/2):
		if word[i]!=word[length-1-i]:
			return False
	return True

print is_palindrome("noon")

# Ex 6.8
def gcd(a, b):
	if b==0:
		return a
	else:
		r = a % b
		return gcd(b, r)

print gcd(8, 12)