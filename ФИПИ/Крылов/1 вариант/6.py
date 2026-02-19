from turtle import *
screensize(5000, 5000)
tracer(0)
k = 10
lt(90)

for _ in range(4):
    fd(9*k)
    lt(180)
    bk(10*k)
    rt(90)

up()

bk(7*k)
lt(90)
fd(3*k)
rt(90)

down()

for _ in range(2):
    fd(17*k)
    lt(90)
    fd(20*k)
    lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(2, 'red')
update()
done()

# 591
