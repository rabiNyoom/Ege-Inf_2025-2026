from turtle import *
k = 20
screensize(5000, 5000)
tracer(0)
lt(90)

for _ in range(6):
    fd(71*k)
    rt(90)
    fd(73*k)
    rt(90)
up()
fd(18*k)
rt(90)
fd(22*k)
lt(90)
down()
for _ in range(6):
    fd(45*k)
    rt(90)
    fd(58*k)
    rt(90)
up()
for x in range(0, 100):
    for y in range(0, 100):
        goto(x*k, y*k)
        dot(4, 'red')
update()
done()
# 46 * 52
