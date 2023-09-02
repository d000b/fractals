import math
import matplotlib.pyplot as plt


def calculatePolygonCoordinates(n):
    if n < 3:
        raise ValueError("Number of sides must be at least 3")

    x_coordinates = []
    y_coordinates = []

    # Calculate the angle between each vertex
    angle = 2 * math.pi / n

    # Adjust the starting angle to make one side parallel to the x-axis
    start_angle = math.pi
    if n % 2 != 0:
        start_angle = math.pi / 2  # 90 degrees
    elif n % 4 == 0 :
        start_angle = math.pi / n

    for i in range(n):
        # Calculate the angle for the current vertex
        theta = start_angle + i * angle

        # Calculate the x and y coordinates within the circle
        x = 0.5 + 0.5 * math.cos(theta)
        y = 0.5 + 0.5 * math.sin(theta)

        # Append the coordinates to the lists
        x_coordinates.append(x)
        y_coordinates.append(y)

    return x_coordinates, y_coordinates


if __name__ == "__main__":

    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    fig.patch.set_facecolor('black')
    
    polygonSides = [3, 4, 5, 6, 7, 8, 9, 10]
    # polygonSides = [11, 12, 13, 14, 15, 16, 17, 18]
    for i, ax in zip(range(0, len(polygonSides)), axes.flatten()):
        x_coords, y_coords = calculatePolygonCoordinates(polygonSides[i])
        print(polygonSides[i])
        print("POLYGON_X_COORDS = ", x_coords)
        print("POLYGON_Y_COORDS = ", y_coords)
        
        ax.set_xlim(-0.1, 1)
        ax.set_ylim(-0.1, 1)
        ax.axis('off')
        ax.set_aspect('equal')
        ax.set_facecolor('black')

        x_coords.append(x_coords[0])
        y_coords.append(y_coords[0])
        ax.plot(x_coords, y_coords, color='white', linewidth=2)

    plt.show()
    