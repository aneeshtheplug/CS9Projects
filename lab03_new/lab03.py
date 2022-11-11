def integerDivision(n,k):
    if n < k:
        return 0
    return 1 + integerDivision(n-k,k)

def collectEvenInts(listOfInt):
    if len(listOfInt) == 0:
        return []
    else:
        new_list = []
        if listOfInt[0] % 2 == 0:
            new_list.append(listOfInt[0])
            return new_list + collectEvenInts(listOfInt[1:])
        return collectEvenInts(listOfInt[1:])

def countVowels(someString):
    vowel_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if len(someString) == 0:
        return 0
    else:
        if someString[0] in vowel_list:
            return 1 + countVowels(someString[1:])
        return countVowels(someString[1:])

def reverseString(s):
    if len(s) == 0:
        return ""
    else:
        new_str = ""
        new_str = new_str + s[-1]
        return new_str + reverseString(s[0:-1])

def removeSubString(s, sub):
    if len(s) < len(sub):
        return s
    else:
        new_word = ''
        if s[0:(len(sub))] == sub:
            return new_word + removeSubString(s[len(sub):],sub)
        else:
            new_word = new_word + s[0]
            return new_word + removeSubString(s[1:],sub)
