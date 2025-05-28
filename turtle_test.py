#! /usr/bin/python
print("Content-type: text/html \n")
import cgi
data = cgi.FieldStorage()

if data.getvalue('x') != None:
    x=int(data.getvalue('x'))
    y=int(data.getvalue('y'))
else:
    x = 0
    y = 0

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
        if x0 == x and y0 == y:
            t += "O"
        else:
            t += "X"
    return t
print(plane(), "\n")
def button():
    print('''
\n
<form action="../cgi-bin/turtle_test.py" method="GET">
<select name="e" onchange="document.location.href=this.value">
<option value=''' + "?x=" + str(x) + "&y=" + str(y) + "&dir=None"+ '''>Choose</option>
<option value=''' + "?x=" + str(x) + "&y=" + str(y - 1) + "&dir=90" + '''>Up</option>
<option value=''' + "?x=" + str(x + 1) + "&y=" + str(y) + "&dir=0"+'''>Right</option>
<option value=''' + "?x=" + str(x) + "&y=" + str(y + 1) + "&dir=-90"+ '''>Down</option>
<option value=''' + "?x=" + str(x - 1) + "&y=" + str(y) + "&dir=180"+ '''>Left</option>
</select>
</form>''')
button()
print(data.getvalue('x'),data.getvalue('y'))
while 0<1:
    if data.getvalue('dir') != None:
        if data.getvalue('dir') == "90":
            y -= 1
        elif data.getvalue('dir') == "0":
            x += 1
        elif data.getvalue('dir') == "-90":
            y += 1
        else:
            x -= 1