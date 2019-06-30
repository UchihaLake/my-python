import math

def circle(r):
    for i in range(2 * r):
        for j in range(2 * r):
            distance_to_centre = math.sqrt((i - r)*(i - r) + (j - r)*(j - r))
            if distance_to_centre > r-0.5 and distance_to_centre < r + 0.5:
                print("*", end = '')
            else:
                print(" ", end = '')
        print()

if __name__ == "__main__":
    r = int(input("The radius: "))
    circle(r)
