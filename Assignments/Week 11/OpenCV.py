import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate and plot histograms for RGB channels
def plot_color_histogram(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Separate the color channels
    channels = ['Red', 'Green', 'Blue']
    colors = ('r', 'g', 'b')
    
    # Plot histograms
    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Number of Pixels')
    
    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])
    
    plt.legend(channels)
    plt.show()

# Example usage
plot_color_histogram('path_to_your_image.jpg')
