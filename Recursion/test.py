# def reverse_string(s):
#     """Return the reverse of the input string."""
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s

# print(reverse_string('hamza'))

# def return_sum_upto_n(num):
#     sum = 0
#     for element in range(1,num + 1): # +1 beacuse of exclusion
#         sum = element + sum
#     return sum

# print(return_sum_upto_n(4))

def is_prime_alt(n):
    number_of_divisors = 0 #called Flag in programming
    for i in range(1, n + 1):
        if n % i == 0: #that is divisible
            number_of_divisors = number_of_divisors + 1
    
    
    
    if number_of_divisors == 2:
        return True
    else:
        return False
    
print(is_prime_alt(6))   