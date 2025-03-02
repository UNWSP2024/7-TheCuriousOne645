import math

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z1 - z2)**2)

def main():
    try:
        coord1 = tuple(map(float, input("Enter the first coordinate (x1, y1, z1): ").split()))
        coord2 = tuple(map(float, input("Enter the second coordinate (x2, y2, z2): ").split()))
        
        dist = distance(coord1, coord2)
        print(f"Distance between points: {dist}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for coordinates.")

main()
