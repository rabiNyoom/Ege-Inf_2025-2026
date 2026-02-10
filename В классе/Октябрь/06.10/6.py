from turtle import *
lt(90)
screensize(3000, 3000)
tracer(0)
k = 5
for _ in range(4):
    fd(28*k); rt(90); fd(26*k); rt(90)
pu()
fd(8*k);rt(90);fd(7*k);lt(90)
pd()
for _ in range(4):
    fd(67*k);rt(90);fd(98*k);rt(90)
pu()
for x in range(-50, 50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()
# 420