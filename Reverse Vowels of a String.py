# https://leetcode.com/problems/reverse-vowels-of-a-string/
s = "hello"
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
l = 0
r = len(s)-1

char_list = list(s)
for i in s:
  char_list.append(i)


while l<len(s) and r>=0:

  if s[r] not in vowels:
    r -= 1 
  elif s[l] in vowels and s[r] in vowels and l < r:

    char_list[l], char_list[r] = char_list[r], char_list[l]
    l += 1
    r -= 1


  else:
    l += 1

return ("".join(char_list))

"""naive"""
# vowels = ["a", "e", "i", "o", "u"]
# print()
# vowel_list = []
# map_dict = {}

# for idx, i in enumerate(s):
#   if i in vowels:
#     vowel_list.append(i)

# result = ""
# for i in s:
#   if i in vowels:
#     result += vowel_list.pop()
#   else:
#     result += i
    
# print(result)


"""Ignore"""
# s = list(s)
#         i = 0 
#         j = len(s)-1
#         while i <= j:
#           print(s[i], s[j])
#           if s[i] in vowels and s[j] in vowels:
#             s[i],s[j] = s[j],s[i]
#             i += 1
#             j -= 1
#           elif s[i] in vowels and s[j] not in vowels:
#             # i += 1
#             j -= 1
#           elif s[i] not in vowels and s[j] in vowels:
#             i += 1
#             # j -= 1
#           elif s[i] not in vowels and s[j] not in vowels:
#             i += 1
#             j -= 1
#         return ("".join(s))
