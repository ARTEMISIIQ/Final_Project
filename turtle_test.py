#! /usr/bin/python
print("Content-type: text/html \n")
import cgi
data = cgi.FieldStorage()
def x():
    t = ""
    x = 0
    y = 0
    while y < 30:
        x += 1
        if x > 100:
            x = 0
            t += "\n"
            y += 1
        t += "x"
    return t
print(x(), "\n")
def button():
    print('''
\n
<select name="">
<option value="Up">Up</option>
<option value="Right">Right</option>
<option value="Down">Down</option>
<option value="Left">Left</option>
</select>''')
button()