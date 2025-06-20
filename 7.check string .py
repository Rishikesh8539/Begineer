def are_anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(result)
