import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

input1 = form.getvalue('input1')
input2 = form.getvalue('input2')
operation = form.getvalue('operation')

# Debug output
print(f"<p>Received input1: {input1}</p>")
print(f"<p>Received input2: {input2}</p>")
print(f"<p>Selected operation: {operation}</p>")

try:
    input1 = float(input1)
    input2 = float(input2)
except ValueError:
    print("<p>Error: Inputs must be numbers.</p>")
    exit()

result = None
error_message = None

if operation == 'add':
    result = input1 + input2
elif operation == 'sub':
    result = input1 - input2
elif operation == 'mul':
    result = input1 * input2
elif operation == 'div':
    if input2 != 0:
        result = input1 / input2
    else:
        error_message = "Error: Division by zero is not allowed."

if result is not None:
    if result > 100:
        result *= 2
    elif result < 0:
        result += 50

if error_message:
    print(f"<p>{error_message}</p>")
else:
    print(f"<p>The result is: {result}</p>")
