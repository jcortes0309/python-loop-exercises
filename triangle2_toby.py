# Toby's example as another solution to the triangle2 exercise

height = int(raw_input("Give me the height of the triangle to print: "))

for row_num in range(height):
    base_width = 2 * height - 1
    num_stars = (row_num * 2) + 1
    num_spaces = (base_width - num_stars) / 2
    spaces = " " * num_spaces
    stars = "*" * num_stars
    print spaces + stars
