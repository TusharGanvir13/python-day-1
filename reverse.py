a = 789
n = 0
while (a>0):
    r = a%10
    n =  (n * 10) + r 
    a = a // 10
print(n)