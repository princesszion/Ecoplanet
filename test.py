# def sum(x, y):
# 		return(x+y)
# print(sum(sum(1,2), sum(3,4)))
#
#
# print(((10 >= 5*2) and (10 <= 5*2)))
# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"
#
# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT


# def is_power_of_two(n):
#     # Check if the number can be divided by two without a remainder
#     while n % 2 == 0 and n != 0:
#         n = n / 2
#     # If after dividing by two the number is 1, it's a power of two
#     if n == 1:
#         return True
#     return False
#
#
# print(is_power_of_two(0))  # Should be False
# print(is_power_of_two(1))  # Should be True
# print(is_power_of_two(8))  # Should be True
# print(is_power_of_two(9))  # Should be False


# number = 1
# while number < 7:
#     print(number, end=" ")
#     number += 1

for x in range(1, 10, 3):
    print(x)

# for x in range(10):
#     for y in range(x):
#         print(y)