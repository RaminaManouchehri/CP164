"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-02-15"
-------------------------------------------------------
"""
# Imports
from email.mime import base

# Constants
VOWELS = "aeiou"
def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x - 1, y) + recurse(x, y - 1)
    return ans
def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        ans = n
    else:
        ans = gcd(n, m % n)
    return ans
def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    if s == "":
        count = 0
    else:
        if (s[0]).lower() in VOWELS:
            count = vowel_count(s[1:]) + 1
        else:
            count = vowel_count(s[1:])
    return count
def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans = 1
    elif power == 1:
        ans = base
    elif power < 0:
        ans = (1 / base) * to_power(base, power + 1)
    else:
        ans = base * to_power(base, power - 1)
    return ans
def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = True
    if len(s) <= 1:
        palindrome = True
    else:
        if (s[0]).isalpha() and (s[-1]).isalpha():
            if (s[0]).lower() == (s[-1]).lower():
                palindrome = is_palindrome(s[1:-1])
            else:
                palindrome = False
    return palindrome
def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    new_set = []
    if len(bag) <= 1:
        new_set = bag
    else:
        new_set = bag_to_set(bag[:-1])
        if bag[-1] not in new_set:
            new_set.append(bag[-1])
    return new_set
    