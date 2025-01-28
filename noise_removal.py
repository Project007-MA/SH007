import cv2
import numpy as np


def adaptive_interpolation_noise_removal(image, block_size=15, threshold=5):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialize filtered image
    filtered_image = np.zeros_like(gray)

    # Apply adaptive interpolation
    for y in range(0, gray.shape[0], block_size):
        for x in range(0, gray.shape[1], block_size):
            block = gray[y:y + block_size, x:x + block_size]

            # Estimate noise level in the block
            noise_level = np.std(block)

            # Apply interpolation if noise level is above threshold
            if noise_level > threshold:
                interpolated_block = cv2.fastNlMeansDenoising(block, None, h=10)
            else:
                interpolated_block = block

            filtered_image[y:y + block_size, x:x + block_size] = interpolated_block

    return filtered_image


# Read input image
input_image = cv2.imread('test/frame_0028.jpg')

# Apply adaptive interpolation noise removal
output_image = adaptive_interpolation_noise_removal(input_image)

# Display input and output images
cv2.imshow('Input Image', input_image)
cv2.imshow('Output Image', output_image)
cv2.imwrite('adaptive_interpolation_noise_removal003.jpg', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
