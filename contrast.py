import cv2
import numpy as np
from matplotlib import pyplot as plt


def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    """
    Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the image.

    Parameters:
    image (numpy array): Input image (grayscale or color)
    clip_limit (float): Threshold for contrast limiting
    tile_grid_size (tuple): Size of grid for histogram equalization

    Returns:
    numpy array: Image with enhanced contrast
    """
    if len(image.shape) == 2:  # Grayscale image
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
        return clahe.apply(image)
    elif len(image.shape) == 3:  # Color image
        # Split the image into its respective channels
        channels = cv2.split(image)
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
        # Apply CLAHE to each channel
        equalized_channels = [clahe.apply(channel) for channel in channels]
        # Merge the equalized channels back into a color image
        return cv2.merge(equalized_channels)
    else:
        raise ValueError("Unsupported image format!")


# Load an example image (replace 'path_to_image.jpg' with your image file)
image = cv2.imread('test/frame_0000.jpg', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Apply CLAHE to the image
clip_limit = 2.0
tile_grid_size = (8, 8)
enhanced_image = apply_clahe(image, clip_limit, tile_grid_size)

# Plot the original and enhanced images for comparison
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Contrast Image')
plt.imshow(enhanced_image, cmap='gray')
plt.axis('off')

plt.show()
