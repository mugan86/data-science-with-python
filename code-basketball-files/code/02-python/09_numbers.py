##########################
# NUMBERS AND OPERATIONS
##########################

import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_FLOOR, ROUND_CEILING

print("############## NUMBERS & OPERATIONS ##############\n")

# --- Basic arithmetic ---
a = 15
b = 4

print("a + b =", a + b)   # suma
print("a - b =", a - b)   # resta
print("a * b =", a * b)   # multiplicación
print("a / b =", a / b)   # división (float)
print("a // b =", a // b) # división entera
print("a % b =", a % b)   # módulo (resto de la división)
print("a ** b =", a ** b) # potencia (a elevado a b)
print("pow(a, b) =", pow(a, b)) # equivalente a a**b
print("abs(-a) =", abs(-a))     # valor absoluto

# --- Floating point numbers ---
x = 3.14159
y = 2.71828

print("\nx + y =", x + y)
print("x * y =", x * y)
print("x / y =", x / y)

###################
# ROUNDING NUMBERS
###################

num1 = 3.14159
num2 = 3.5
num3 = 2.5
num4 = -3.5

print("\n############## ROUNDING NUMBERS ##############\n")

# --- Built-in round() ---
print("round(num1, 2):", round(num1, 2))   # 3.14 (2 decimales)
print("round(num1):", round(num1))         # 3
print("round(3.5):", round(num2))          # 4 (half to even)
print("round(2.5):", round(num3))          # 2 (half to even)
print("round(-3.5):", round(num4))         # -4 (half to even)

# --- math.floor() and math.ceil() ---
print("\nmath.floor(3.9):", math.floor(3.9))   # 3 (hacia abajo)
print("math.ceil(3.1):", math.ceil(3.1))       # 4 (hacia arriba)
print("math.floor(-3.9):", math.floor(-3.9))   # -4
print("math.ceil(-3.9):", math.ceil(-3.9))     # -3

# --- math.trunc() ---
print("\nmath.trunc(3.9):", math.trunc(3.9))   # 3 (trunca decimales)
print("math.trunc(-3.9):", math.trunc(-3.9))   # -3

# --- f-string formatting (solo visual) ---
pi = 3.14159
print(f"\nUsing f-string with 2 decimals: {pi:.2f}")  # "3.14"

# --- Decimal for precise control ---
print("\nDecimal rounding:")
print("ROUND_HALF_UP 2.5 ->", Decimal("2.5").quantize(Decimal("1"), rounding=ROUND_HALF_UP))    # 3
print("ROUND_HALF_DOWN 2.5 ->", Decimal("2.5").quantize(Decimal("1"), rounding=ROUND_HALF_DOWN))# 2
print("ROUND_FLOOR 2.7 ->", Decimal("2.7").quantize(Decimal("1"), rounding=ROUND_FLOOR))        # 2
print("ROUND_CEILING 2.1 ->", Decimal("2.1").quantize(Decimal("1"), rounding=ROUND_CEILING))    # 3
