import copy

# Exercise 1 - Smallest Fraction Terms
def exercise1(numerator,denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce_fraction(numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        reduced_numerator = numerator // common_divisor
        reduced_denominator = denominator // common_divisor
        return (reduced_numerator, reduced_denominator)
    result = reduce_fraction(numerator,denominator)
    return result

# Exercise 2 - Magical Dates
def exercise2(day,month,year):
    return None

# Exercise 3 - All Sublists
def exercise3(l):
    return None

# Exercise 4 - English to Pig Latin Translator
def exercise4(word):
    return None

# Exercise 5 - Morse Code Encoder
def exercise5(message):
    return None

# Exercise 6 - Spelling Out Numbers
def exercise6(num):
    return None

# Exercise 7 - No Functions without Comments
def exercise7(filename):
    return None

# Exercise 8 - Justify any Text
def exercise8(filename,length):
    return None

# Exercise 9 - Knight's Challenge
def exercise9(start,end,moves):
    return None

# Exercise 10 - War of Species
def exercise10(environment):
    return None
