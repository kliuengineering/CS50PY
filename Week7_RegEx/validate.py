import re

email = input("What's your email -> ").strip()

'''
if re.search("@", email):                   # re.search(pattern, string, flags=0)
    print("Valid")
else:
    print("Invalid")
'''


# how can we do better? we need more volcab
    # .                 any char except a newline
    # *                 0 or more reps
    # +                 1 or more reps
    # ?                 0 or 1 rep
    # {m}               m reps
    # {m, n}            m to n reps
    # ^                 starts with
    # $                 ends with
    # r"some text"      the r is "raw" string
    # []                supports the set of characters inside []
    # [^]               supports the set of complements of the set of chars inside []
    # \d                decimal digit
    # \D                not a decimal digit
    # \s                whitespace chars
    # \S                not a whitespace char
    # \w                word char + numbers + underscore
    # \w                not a word char
    # ()                grouping
    # (|)               or
    # (\s)              space

    # A|B               either A or B
    # (...)             a group
    # (?:...)           non-capturing version

    # re.search(pattern, string, flags=0)
    # flags can be
    #               re.IGNORECASE,
    #               re.MULTILINE,
    #               re.DOTALL

    # re.match(pattern, string, flag=0)
    # re.fullmatch(pattern, string, flag=0)
    # re.sub(pattern, repl, string, count=0, flags=0)


# regex -> finite state machine analogy

if re.search(r"^.+@.+\.edu$", email):                 # use r to indicate a raw screen
    print(email)
else:
    print("Invalid")
