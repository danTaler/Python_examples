# heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams 

# check if two strings are Anagrams!
#sort the strings and check sequence!

STRING_A = 'heart1'
STRING_B = 'heart1'
STRING_C = 'heart2'


common = set(STRING_A) & set(STRING_B) & set(STRING_C)
print(common)

def sort_string(str1, str2):
    # Sorting a string  
    res1 = ''.join(sorted(str1))
    res2 = ''.join(sorted(str2))
    if res1 == res2:
        return True
    else:
        return False


anagram = sort_string(STRING_A,STRING_B)
print(anagram)

