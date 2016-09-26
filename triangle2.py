triangle_height = int(raw_input("Give me the height of the triangle to print: "))
triangle_width = triangle_height + (triangle_height - 1)
empty_space = triangle_height - 1
print_times = 1

print "\n"

for i in range(triangle_height):
    print " " * empty_space + ("*" * print_times)
    print_times += 2
    empty_space -= 1

print "\n"
