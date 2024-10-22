import re

# Search

txt_a = "Its raining at my place"
x = re.search("raining", txt_a)
if x:
    print("Searched successfully")
else:
    print("No match")

y = re.search("^Its.*place$", txt_a)
if y:
    print("Yes, match is successful")
else:
    print("No, Match found")

# find all
txt_b = "The rain in spain"
a = re.findall("ai", txt_b)
print(a)
b = re.findall("in", txt_b)
print(b)

txt_c = "Its quater 8 in the morning"
z = re.findall("[a-zA-Z]", txt_c)
print(z)
y = re.findall("[0-9]",txt_c)
print(y)
b = re.findall("[1234]", txt_c)
if b:
    print("Pattern matched")
else:
    print("No matches found")

# match
pattern = "^a...3$"
str_b = "abcd3"
res = re.match(pattern, str_b)
if res:
    print("Match successful")
else:
    print("Match unsuccessful")

str_c = "abcdefg3"
res_c = re.match(pattern, str_c)
if res_c:
    print("Match successful")
else:
    print("Match unsuccessful")

str_d = "axyz3"
res_d = re.match(pattern, str_d)
if res_d:
    print("Match successful")
else:
    print("Match unsuccessful")

pattern_a = "^.b...3$"
str_x = "abcdg3"
res_x = re.match(pattern_a, str_x)
if res_x:
    print("Match successful")
else:
    print("Match unsuccessful")

str_x = "John age is 29"
rep = re.sub("\s", "", str_x)
print(rep)

rep_y = re.sub("\d", "a", str_x)
print(rep_y)