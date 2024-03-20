import matplotlib.pyplot as plt

# Function to read data from the text file
def read_data(filename):
    """
    Reads data from a text file in the format:
    x y
    ...

    Args:
        filename: The name of the text file.

    Returns:
        A tuple containing two lists: x-axis data and y-axis data.
    """
    x_data = []
    y_data = []
    with open(filename, 'r') as f:
        for line in f:
            values = line.strip().split()
            x_data.append(float(values[0]))
            y_data.append(float(values[1]))
    return x_data, y_data

# Read data from the text file
x_data, y_data = read_data("22MS140.txt")

# Get user input for annotated points and labels
annotated_points = []
annotations = []
while True:
    x_coord = input("Enter x-coordinate of data point to annotate (or 'q' to quit): ")
    if x_coord.lower() == 'q':
        break
    try:
        x = float(x_coord)
        y_coord = input("Enter y-coordinate of data point: ")
        y = float(y_coord)

        # Find closest data point in the dataset (optional)
        closest_index = min(range(len(x_data)), key=lambda i: abs(x_data[i] - x))
        closest_y = y_data[closest_index]

        annotated_points.append((x, y))
        label = input("Enter label for this point: ")
        annotation = input("Enter a few words describing this point: ")
        annotations.append((label, annotation, closest_y))  # Include closest_y
    except ValueError:
        print("Invalid input. Please enter numbers or 'q' to quit.")

# Plot the data
plt.plot(x_data, y_data)

# Set labels and title
plt.xlabel("Wavenumber (cm-1)")
plt.ylabel("Intensity (a.u.)")
plt.title("FTIR Data - 22MS140.txt")

# Add annotations for user-selected points with data point value
for point, (label, annotation, closest_y) in zip(annotated_points, annotations):
    text = f"{label}\n{annotation}\n({point[0]:.2f}, {closest_y:.4f})"  # Include data point value
    plt.annotate(
        text,
        xy=point,
        textcoords="offset points",
        xytext=(0, -40),  # Adjust offset for downward placement
        ha='center'
    )
    plt.scatter(point[0], point[1], color='red', marker='o')  # Plotting marker separately

# Ensure plot elements are drawn in the correct order
plt.legend()  # Add legend if needed (may obscure annotations otherwise)
plt.tight_layout()  # Adjust layout to avoid overlapping elements

# Show the plot with grid
plt.grid(True)
plt.gca().invert_xaxis()
plt.show()
