from turtle import *;

tracer(0);
screensize(3000, 3000);
k = 5;

lt(90);
for _ in range(6):
    fd(19*k); rt(90); fd(22*k); rt(90);
pu();
fd(3*k); rt(90); fd(1*k); lt(90);
pd();
for _ in range(6):
    fd(85*k); rt(90); fd(82*k); rt(90);
pu();
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k);
        dot(3, 'red');

update(); done();

# 74