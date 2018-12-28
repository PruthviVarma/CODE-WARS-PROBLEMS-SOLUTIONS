def better_than_average(class_points, your_points):
    # Your code here
    return True if((sum(class_points)/len(class_points))<=your_points) else False
