# 1. Introduction to Programming

#  Programs are written in high-level languages (like Python).
#  Translators (Compiler / Interpreter) convert them into machine code.

# 2. What is Python?

#  Simple & easy to learn.
#  Free & open-source.
#  High-level language.
#  Portable (runs on different platforms).
#  Developed by Guido van Rossum.

# 3. First Python Program

#   python : print("Hello World")

# 4. Python Character Set

#  Letters: A–Z, a–z
#  Digits: 0–9
#  Special Symbols: +, -, *, /, %, etc.
#  Whitespaces: space, tab, newline, carriage return, formfeed
#  Other Characters: Supports ASCII & Unicode.

# 5. Variables

#  A variable is a name given to a memory location.
   
#    python : name = "Shradha"
#             age = 23
#             price = 25.99

# 6. Rules for Identifiers

#  Can contain letters, digits, underscore (_).

#   Example: myVariable, variable_1.
#            Cannot start with a digit (1variable ❌).
#            Cannot use special symbols (!, #, @, %, $).
#            Can be of any length.


# 7. Data Types

#  int → integers
#  float → decimal numbers
#  complex → complex numbers
#  str → strings
#  bool → True/False
#  None → null value

#  Example:python
#          age = 23
#          pi = 3.14
#          complex_num = 2 + 3j
#          A = True
#          name = "Shradha"

# 8. Keywords

#  Reserved words in Python (cannot be used as identifiers).
#  Examples: and, or, not, True, False, None, if, else, while, for, return, import, class, def, etc.

# 9. Comments

#  Single-line: # This is a comment
#  Multi-line:

#   python : """
#            This is a
#            multi-line comment
#            """   
# 10. Operators

#  Arithmetic: +, -, *, /, %, **
#  Relational: ==, !=, >, <, >=, <=
#  Assignment: =, +=, -=, *=, /=, %=, **=
#  Logical: and, or, not

#  11. Type Conversion

#  Automatic conversion when compatible: python
#                                        a, b = 1, 2.0
#                                        sum = a + b   # 3.0
    
#                                        python
#                                        a, b = 1, "2"
#                                        sum = a + b   # ❌ TypeError

# 12. Type Casting
 
#  Explicit conversion using functions:
#   int(y) → integer
#   float(y) → float
#   complex(real, imag) → complex number
#   str(y) → string
#   tuple(y) → tuple
#   list(y) → list
#   set(y) → set
#   dict(y) → dictionary
#   ord(y) → character → integer
#   hex(y) → integer → hexadecimal string
#   oct(y) → integer → octal string

#  Example: python
#           a, b = 1, "2"
#           c = int(b)
#           sum = a + c  # 3 

# 13. Input in Python

#  input() → always returns a string.
#  Convert to other types:
#   python : x = input("Enter a number: ")   # str
#           x = int(input("Enter a number: "))   # int
#           x = float(input("Enter a number: ")) # float

# 14. Practice Problems

#  Input 2 numbers & print their sum.
#  Input side of a square & print its area.
#  Input 2 floating-point numbers & print their average.
#  Input 2 integers a and b. Print True if a >= b, else False.                                       