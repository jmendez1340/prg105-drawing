
import turtle

def polygon (t, length):
   t.fd(length)
   t.lt(120)
   t.fd(length)
   t.lt(60)
   t.fd(length)
   t.lt(120)
   t.fd(length)
   t.lt(60)

def Bpolygon (t, length):
   t.bk(length)
   t.lt(120)
   t.fd(length)
   t.lt(60)
   t.fd(length)
   t.lt(120)
   t.fd(length)
   t.lt(60)
   t.fd(length)
   t.lt(60)

def Don (t, length):
   t.fd(length)
   t.lt(120)
   t.bk(length)
   t.lt(60)
   t.fd(length)
   t.lt(60)
   t.fd(length)
   t.lt(60)
   t.bk(length)
   t.lt(60)
   t.bk(length)
   t.lt(60)
   t.bk(length)
   t.lt(120)
   t.bk(length)
   t.lt(60)
   t.bk(length)
   t.lt(60)

def Queen (t, length):
   t.bk(length)
   t.lt(120)
   t.bk(length)
   t.lt(60)
   t.bk(length)
   t.lt(120)
   t.bk(length)
   t.lt(60)

def All (t, length):
   t.fd(length)
   t.lt(180)
   t.fd(length)
   t.lt(360)
   t.fd(length)
   t.lt(180)

def Drum (t, length):
   t.bk(length)
   t.lt(120)
   t.bk(length)
   t.lt(120)
   t.bk(length)
   t.lt(120)

def dead (t, length):
   t.bk(length)
   t.lt(120)
   t.fd(length)
   t.lt(60)
   t.fd(length)
   t.lt(120)
   t.bk(length)
   t.lt(60)







Cynthia = turtle.Turtle()
Cyn = turtle.Turtle()
bob = turtle.Turtle()
fred = turtle.Turtle()
Brian = turtle.Turtle()
Roger = turtle.Turtle()

polygon(Cynthia, 100)
Bpolygon(Cyn, 100)
Don(bob, 100)
Queen(fred, 100)
Drum(Roger, 100)
All(Brian, 100)


turtle.done()
