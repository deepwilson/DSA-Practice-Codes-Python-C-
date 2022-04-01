s = "ADOBECODEBANC"
t = "ABC"
# s = "a"
# t = "aa"


i = 0
j = 0

t_ = t
sub = ""
result = []

flag = False
while i < len(s):
  while j < len(s):
    char = s[j]
    # print(char)
    sub += char
    if char in t_:
      # t_ = t_.replace(char, "")
      target = list(t_)
      for idx, r in enumerate(target):
        if r==char:
          target[idx] = ""
          break
      
      target = "".join(target)
      t_ = target
      # print("*******", t_)
          
          
      
      if t_ == "":
        result.append(sub)
        sub = ""
        t_ = t
        flag = True
    if flag:
      flag = False
      j = i+1
      break
        
    
    j += 1
  if t_ != "":
    sub = ""
    
  i += 1

print(result)

t_ = t
final = ""

len_ = len(s)
for res in result:
  for i in res:
    if i in t_:
      t_= t_.replace(i, "")
    
  if t_ == "":
    if len(res) <= len_:
      final = res
      len_ = len(final)
    
    
  else:
    t_ = t
    final = ""
    
  
print("final", final)
      
    
      
    
    
