import matplotlib.pyplot as plt 

def generate_images(xs: list[int], ys: list[int]) -> None:
    """Generate an image on matplotlib 
    """
    
    # xmin, xmax, ymin, ymax = 0, 10, 0, 10
    # ticks_frequency = 1

    # figure size
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(xs, ys) # plot the points

    plt.show()