#! /usr/bin/python
print("Content-type: text/html \n")
import cgi
data = cgi.FieldStorage()

if data.getvalue('x') != None:
    list0 += [[int(data.getvalue('x')),int(data.getvalue('y'))]]
    x=int(data.getvalue('x'))
    y=int(data.getvalue('y'))
else:
    x = 0
    y = 0
    list0 = []


def plane():
    t = ""
    x0 = 0
    y0 = 0
    while y0 < 30:
        x0 += 1
        if x0 > 100:
            x0 = 0
            t += "\n"
            y0 += 1
        if x0 == x and y0 == y or [x0, y0] in list0:
            t += "X"
        else:
            t += "_"
    return t
print(plane(), "\n")
def button():
    print('''
\n
<form action="../cgi-bin/turtle_test.py" method="GET">
<select name="e" onchange="document.location.href=this.value">
<option value=''' + "?x=" + str(x) + "&y=" + str(y) + '''>Choose</option>
<option value=''' + "?x=" + str(x) + "&y=" + str(y - 1) + '''>Up</option>
<option value=''' + "?x=" + str(x + 1) + "&y=" + str(y) + '''>Right</option>
<option value=''' + "?x=" + str(x) + "&y=" + str(y + 1) + '''>Down</option>
<option value=''' + "?x=" + str(x - 1) + "&y=" + str(y) + '''>Left</option>
</select>
</form>''')
button()
print(data.getvalue('x'),data.getvalue('y'))