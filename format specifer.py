# format specifer = {value:flags} formata value based on what flags are inserted

price1 = 3.14159
price2 = -932.65
price3 =32.36

# print(f"Price 1 is ${price1:.2f}")
# print(f"Price 2 is ${price2:.1f}")
# print(f"Price 3 is ${price3:.3f}")

# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")

# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:010}")
# print(f"Price 3 is ${price3:010}")

# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")

# print(f"Price 1 is ${price1:-^15}")
# print(f"Price 2 is ${price2:-^15}")
# print(f"Price 3 is ${price3:-^15}")

print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")
