import math
def Quadric_Equation(a: float, b: float, c: float):
    # d = math.pow(b,2) - 4*a*c
    d = (b**2) - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Here is 2 roots of the equation x1 = {x1:.2f}, x2 = {x2:.2f}"
    if d == 0:
        x = (-b / (2*a))
        return f"Here is only 1 root of the equation x = {x:.2f}"
    else:
        return f"Cant solve {d:.2f} < 0"


def main():
    req = input("Enter a, b, c separated by space: ")
    a, b, c = map(float, req.split())
    result = Quadric_Equation(a, b, c)
    print(result)

if __name__ == "__main__":
    main()
