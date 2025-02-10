# Math algorithms and utilities for solving mathematical problems.
#
# Common topics:
# - Prime number checking and generation
# - Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
# - Sieve of Eratosthenes (prime number generation)
# - Modular arithmetic (inverse, exponentiation, factorial)
# - Combinatorics (permutations, combinations, binomial coefficients)
# - Number theory (Euler's Totient function, Fibonacci sequence)
# - Matrix operations (multiplication, exponentiation)

import math
from functools import lru_cache

# ====================== Prime Numbers ======================

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Time Complexity: O(√n)
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Generate all prime numbers up to n using the Sieve of Eratosthenes.
    Time Complexity: O(n log log n)
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# ====================== GCD and LCM ======================

def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two numbers using Euclid's algorithm.
    Time Complexity: O(log min(a, b))
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Compute the least common multiple of two numbers.
    Time Complexity: O(log min(a, b))
    """
    return a * b // gcd(a, b)

# ====================== Modular Arithmetic ======================

def mod_inverse(a: int, mod: int) -> int:
    """
    Compute the modular inverse of a under modulo mod using the Extended Euclidean Algorithm.
    Time Complexity: O(log min(a, mod))
    """
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd_val, x, _ = extended_gcd(a, mod)
    if gcd_val != 1:
        raise ValueError("Modular inverse does not exist")
    return x % mod

def mod_pow(base: int, exp: int, mod: int) -> int:
    """
    Compute (base^exp) % mod using fast exponentiation (exponentiation by squaring).
    Time Complexity: O(log exp)
    """
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

def mod_factorial(n: int, mod: int) -> int:
    """
    Compute factorial of n under modulo mod.
    Time Complexity: O(n)
    """
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result

# ====================== Combinatorics ======================

def binomial_coefficient(n: int, k: int) -> int:
    """
    Compute the binomial coefficient C(n, k) using dynamic programming.
    Time Complexity: O(n * k)
    """
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]

@lru_cache(maxsize=None)
def catalan_number(n: int) -> int:
    """
    Compute the nth Catalan number using recursion with memoization.
    Time Complexity: O(n^2)
    """
    if n <= 1:
        return 1
    result = 0
    for i in range(n):
        result += catalan_number(i) * catalan_number(n - 1 - i)
    return result

# ====================== Number Theory ======================

def euler_totient(n: int) -> int:
    """
    Compute Euler's Totient function φ(n), which counts the number of integers up to n that are coprime with n.
    Time Complexity: O(√n)
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number using recursion with memoization.
    Time Complexity: O(n)
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ====================== Matrix Operations ======================

def matrix_multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """
    Multiply two matrices a and b.
    Time Complexity: O(n^3) for n x n matrices
    """
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_pow(matrix: list[list[int]], exp: int) -> list[list[int]]:
    """
    Raise a matrix to the power of exp using exponentiation by squaring.
    Time Complexity: O(n^3 log exp) for n x n matrices
    """
    result = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        exp = exp // 2
    return result
