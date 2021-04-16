import random

lower ="abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num ="0123456789"
symbols="[]{}()*;/,_-"

output = lower + upper+num+symbols
length=16
password="".join(random.sample(output,length))
print(password)