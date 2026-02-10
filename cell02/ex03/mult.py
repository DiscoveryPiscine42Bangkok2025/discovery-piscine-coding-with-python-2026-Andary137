import sys

print("Enter the first number:")
try:
    num1 = int(input())
except ValueError:
    sys.exit()

print("Enter the second number:")
try:
    num2 = int(input())
except ValueError:
    sys.exit()

result = num1 * num2

print(f"{num1} x {num2} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    # กรณีผลลัพธ์เป็น 0 โจทย์ให้พิมพ์แบบนี้เป๊ะๆ
    print("The result is positive and negative.")