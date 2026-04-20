def add(A,B):
    return A+B
def min(A,B):
    return A-B
def mul(A,B):
    return A*B
def div(A,B):
    return A/B
print("A:")
A = int(input())
print("B:")
B = int(input())
print("op: + - * /")
op = input()
if op == "+":
    print(add(A,B))
elif op == "-":
    print(min(A,B))
elif op == "*":
    print(mul(A,B))
elif op == "/":
    print(div(A, B))

