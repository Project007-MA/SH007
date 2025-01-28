import cv2

new_width = 900  # New width after resizing
new_height = 600  # New height after resizing
kernel_size = 5  # Kernel size for Gaussian blur
sigmaX = 0  # Standard deviation for Gaussian blur
clip_limit = 2.0  # Clip limit for CLAHE (adjust as needed)
tile_grid_size = (8, 8)  # Tile grid size for CLAHE
alpha = 0  # Alpha for normalization
beta = 255  # Beta for normalization
def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize using bi-cubic interpolation
    resized_image = cv2.resize(gray_image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    # Noise reduction using Gaussian blur
    blurred_image = cv2.GaussianBlur(resized_image, (kernel_size, kernel_size), sigmaX)

    # Apply CLAHE with adjusted parameters
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    equalized_image = clahe.apply(blurred_image)

    # Min-Max normalization
    normalized_image = cv2.normalize(equalized_image, None, alpha=alpha, beta=beta, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow("img", normalized_image)
    cv2.imwrite("img_results/normalize4.jpeg", normalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return normalized_image

#preprocess_image("img/4.jpg")