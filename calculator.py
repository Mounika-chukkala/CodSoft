def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def parse_expression(expression):
    while '(' in expression:
        start = expression.rfind('(')
        end = expression.find(')', start)
        if start != -1 and end != -1:
            sub_result = parse_expression(expression[start + 1:end])
            expression = expression[:start] + str(sub_result) + expression[end + 1:]

    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] in '*/':
            left = float(tokens.pop())
            right_start = i + 1
            while right_start < len(expression) and expression[right_start].isdigit() or expression[right_start] == '.':
                right_start += 1
            right = float(expression[i + 1:right_start])
            if expression[i] == '*':
                tokens.append(multiply(left, right))
            else:
                tokens.append(divide(left, right))
            i = right_start - 1
        else:
            tokens.append(expression[i])
        i += 1

    expression = ''.join(map(str, tokens))

    result = 0
    current_num = ''
    current_op = '+'
    for char in expression:
        if char in '+-':
            if current_op == '+':
                result += float(current_num)
            elif current_op == '-':
                result -= float(current_num)
            current_num = ''
            current_op = char
        else:
            current_num += char

    if current_op == '+':
        result += float(current_num)
    elif current_op == '-':
        result -= float(current_num)

    return result

def calculator():
    expression = input("Enter the mathematical expression: ")
    result = parse_expression(expression)
    print(f"The result of '{expression}' is: {result}")

calculator()
