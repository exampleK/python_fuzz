import itertools as its
words = "1234568790"
r =its.product(words,repeat=1)
dic = open("c://1.txt","a")
for i in r:    
    dic.write("".join(i))    
    dic.write("".join("\n"))

dic.close()
