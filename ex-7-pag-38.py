s=str(input('introduceti sirul de caractere: '))
#a)
print(s.count("A"))
#b)
s1=""
for i in range(0,len(s)) :
    s1=s.replace("A","*")
print(s1)
#c)
s2=""
for i in range(0,len(s)) :
    s2=s.replace("B","")
print(s2)
#d)
s3=""
for i in range(0,len(s)) :
    s3=(s.count("MA"))
print(s3)
#e)
s4=""
for i in range(0,len(s)) :
    s4=(s.replace("MA","TA"))
print(s4)
#f)
s5=""
for i in range(0,len(s)):
    s5=s.replace("TO","")
print(s5)  
