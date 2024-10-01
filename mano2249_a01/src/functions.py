"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""
# Imports

# Constants
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    result = []
    for i in values:
        if i not in result:
            result.append(i)
    values = result
    print(values)
    return
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    line = fv.readline()
    while line != "":
        line1 = line.strip()
        for i in range(len(line1)):
            if line1[i].isdigit() or line1[i] == " " or line1[i].isalpha():
                if line1[i] == " ":
                    w += 1
                if line1[i].isalpha():
                    if line1[i].isupper():
                        u += 1
                    else:
                        l += 1
                if line1[i].isdigit():
                    d += 1
            else:
                r += 1
        line = fv.readline()
    return u, l, d, w, r
def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    index = -1          
    if sub in string:
        sub = sub[0]
        for i in string:
            if i in string:
                index += 1
            if i == sub:
                locations.append(index)
    return locations
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False 
        else:
            leap_year = True  
    else:
        leap_year = False 
    return leap_year

def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    count = 0
    if name[1].isalpha() or name[1] == "_":
        for i in range(len(name)):
            if name[i].isalpha() or name[i].isdigit() or name[i] == "_":
                count += 0
            else:
                count +=1
    else:
        count = 1
    if count != 0:
        valid = False 
    return valid

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    rows = len(a)
    cols = len(a[0])

    b = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(a[i][j])
        b.append(row)
    return b
def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            p = 0
            for k in range(len(a[i])):
                p += a[i][k] * b[k][j]
            row.append(p)
        c.append(row)
    return c
def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    i = 0
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        pl = word + "way"
    else:
        while word[i].lower() not in vowels:
            i += 1
        pl = word[i:len(word)] + word[0:(i)] + "ay"
    pl = pl.lower()
    if word[0:1].isupper():
        pl = pl[0:1].upper() + pl[1:len(pl)]
    return pl

def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in string:
        i = i.lower()
        if i.isalpha():
            shift = alphabet.index(i) + n
            new = alphabet[shift]
            estring += new
        elif i == ' ': 
            estring += i

        elif i.isdigit(): 
            estring += i
    estring = estring.upper()
    return estring
            
