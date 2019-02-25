def compare_strings(string1, string2):
    if type(string1) != str or type(string2) != str:
        return 0
    if string1 == string2:
        return 1
    if len(string1)>len(string2):
        return 2
    if string1 != string2 == "learn":
        return 3

result1 = compare_strings(1, "learn")
result2 = compare_strings("learn", "learn")
result3 = compare_strings("python", "learn")
result4 = compare_strings("pyth", "learn")

print(result1, result2, result3, result4)