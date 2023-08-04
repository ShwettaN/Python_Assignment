# Prime Numbers
primes = []

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_up_to(limit):
    for num in range(2, limit + 1):
        if checkPrime(num):
            primes.append(num)
    return primes


limit = 50
prime_numbers = find_primes_up_to(limit)

print("Result 1: ", prime_numbers)

#Print User Input Table
number = int(input('Enter a number '))

for i in range(1, 11):
   print(number, '*', i, '=', number*i)

# Print palindrome string taking input as string
def isPalindrome(s):
	return s == s[::-1]

s=input('Enter a string ')
ans = isPalindrome(s)

if ans:
	print("Palindrome")
else:
	print("Not a Palindrome")


# Reverse a String
def revString(input_string):
    return input_string[::-1]


input_string = input("Enter a string: ")
reversed = revString(input_string)

print("Reversed string:", reversed)