x=int(input('Time in sec : '))
d=x//86400
print('Days: ')
print(d)
x=x%86400
h=x//3600
print('Hours: ')
print(h)
x%=3600
m=x//60
print('Minutes: ')
print(m)
x%=60
s=x
print('Seconds: ')
print(s)

