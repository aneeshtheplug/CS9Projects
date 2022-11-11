def reverseWithoutDigits(s):
    if len(s) == 0:
        return s
    if s[len(s)-1].isdigit() == True:
        return reverseWithoutDigits(s[:len(s)-1])
    else:
        return reverseWithoutDigits(s[:len(s)-1]) + s[len(s) - 1] 

assert reverseWithoutDigits("") == ""
assert reverseWithoutDigits("CS9") == "SC"
assert reverseWithoutDigits("4h3LL00!") == "!LLh"
assert reverseWithoutDigits("123454321") == ""