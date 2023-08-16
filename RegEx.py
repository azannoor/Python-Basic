import re


phone=['+92249475240', '+92096110858','+91044895184']
string=''.join(phone)
x=re.findall("\+92\d*",string)
if x:
    print(x)
txt='The capital city of Pakistan is Islamabad'
find=re.search("^The.*Islamabad$",txt)
if find:
    print("Yes its a match")
    
#find and replace

find2=re.sub("Islamabad","karachi",txt)
print(find2)