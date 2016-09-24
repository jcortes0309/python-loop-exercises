width = int(raw_input("Enter width of box: "))
height = int(raw_input("Enter height of the box: "))

print "*" * width
for i in range(height):
    print "*" + (" " * (width - 2)) + "*"
print "*" * width
