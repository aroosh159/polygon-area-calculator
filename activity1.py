# Define a function 'poly_area' to calculate the area of a polygon
def poly_area(c):
    # Initialize an empty list 'add' to store intermediate values
    add = []
    
    # Use a loop to iterate through the coordinates
    for i in range(0, (len(c) - 2), 2):
        # Calculate and append the cross product of consecutive coordinate pairs
        add.append(c[i] * c[i + 3] - c[i + 1] * c[i + 2])
    
    # Calculate and append the cross product of the last and first coordinate pairs
    add.append(c[len(c) - 2] * c[1] - c[len(c) - 1] * c[0])
    
    # Return the absolute value of half of the sum of all cross products
    return abs(sum(add) / 2)

# Prompt the user to input the number of sides of the polygon
no_sides = int(input('Input number of sides: '))
# Initialize an empty list 'cord_data' to store coordinates
cord_data = []

# Use a loop to input coordinates for each side of the polygon
for z in range(no_sides):
    print("Side:", z+1)
    print("Input the Coordinate:")
    # Input x-coordinate
    x = int(input('Input Coordinate x:'))
    # Input y-coordinate
    y = int(input('Input Coordinate y:'))
    # Append the coordinates to 'cord_data'
    cord_data.append(x)
    cord_data.append(y)
# Print the area of the polygon using the 'poly_area' function
print("\nArea of the Polygon:", poly_area(cord_data))
