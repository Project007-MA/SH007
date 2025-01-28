import cv2
import numpy as np

def calculate_mse(original, reconstructed):
    mse = np.mean((original - reconstructed) ** 2)
    return mse

def calculate_psnr(original, reconstructed):
    mse = calculate_mse(original, reconstructed)
    if mse == 0:
        return float('inf')  # When the MSE is zero, the PSNR is infinite
    max_pixel = 255.0  # Assuming 8-bit depth images
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    return psnr

# Load the images (both original and reconstructed should be of same size and type)
original_image = cv2.imread('frames_data1/frame_0029.jpg')
reconstructed_image = cv2.imread('adaptive_interpolation_noise_removal.jpg')

# Convert images to grayscale if they are colored (Optional)
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
reconstructed_image = cv2.cvtColor(reconstructed_image, cv2.COLOR_BGR2GRAY)

psnr_value = calculate_psnr(original_image, reconstructed_image)
print(f"PSNR value is {psnr_value} dB")

import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
import cv2

# Load your images
original_image = cv2.imread('frames_data1/frame_0029.jpg', cv2.IMREAD_GRAYSCALE)
reconstructed_image_noise = cv2.imread('adaptive_interpolation_noise_removal.jpg', cv2.IMREAD_GRAYSCALE)
reconstructed_image_const = cv2.imread('adaptive_interpolation_noise_removal.jpg', cv2.IMREAD_GRAYSCALE)

# Convert images to float data type
original_image = img_as_float(original_image)
reconstructed_image_noise = img_as_float(reconstructed_image_noise)
reconstructed_image_const = img_as_float(reconstructed_image_const)

# Calculate MSE and SSIM for original vs. noise
mse_noise = mean_squared_error(original_image, reconstructed_image_noise)
ssim_noise = ssim(original_image, reconstructed_image_noise, data_range=reconstructed_image_noise.max() - reconstructed_image_noise.min())

# Calculate MSE and SSIM for original vs. constant
mse_const = mean_squared_error(original_image, reconstructed_image_const)
ssim_const = ssim(original_image, reconstructed_image_const, data_range=reconstructed_image_const.max() - reconstructed_image_const.min())

# Plot the images and display MSE and SSIM
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5), sharex=True, sharey=True)
ax = axes.ravel()

# Original image
ax[0].imshow(original_image, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0].set_xlabel(f'MSE: 0.00, SSIM: 1.00')
ax[0].set_title('Original image')

# Image with noise
ax[1].imshow(reconstructed_image_noise, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[1].set_xlabel(f'MSE: {mse_noise:.2f}, SSIM: {ssim_noise:.2f}')
ax[1].set_title('Image with noise')

# Image plus constant
ax[2].imshow(reconstructed_image_const, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[2].set_xlabel(f'MSE: {mse_const:.2f}, SSIM: {ssim_const:.2f}')
ax[2].set_title('Image plus constant')

plt.tight_layout()
plt.show()



