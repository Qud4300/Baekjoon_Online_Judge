n = int(input())
print(1 if (n%400==0 or (n%4==0 and n%100!=0)) else 0)