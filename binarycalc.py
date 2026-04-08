ans = float(input("what is the decimal: "))

def decimal_to_binary(ans):
    if ans == 0:
        return "0"
    binary = ""
    while ans > 0:
        remainder = ans % 2
        binary = str(remainder) + binary  # Prepend remainder
        ans = ans // 2
    return binary

print(decimal_to_binary(ans))  # Output: 1010