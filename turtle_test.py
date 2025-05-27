#! /usr/bin/python
print("Content-type: text/html \n")
import cgi
data = cgi.FieldStorage()
def x():
    t = ""
    for i in range(100):
        t += "x"
    print(t)  
for i in range(30):
    x()
def button():
    print('<input type="button" name="Up" value="Up">')
button()