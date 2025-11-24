from PIL import Image
import os

# Folder that contains original images
input_folder = "images"

# Folder where resized images will be saved
output_folder = "resized_images"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Desired size (width, height)
new_size = (300, 300)

# Loop through all files in folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        
        # Open image
        img = Image.open(img_path)

        # Resize image
        resized_img = img.resize(new_size)

        # Save resized image to output folder
        save_path = os.path.join(output_folder, filename)
        resized_img.save(save_path)

        print(f"Resized: {filename}")

print("✔ All images resized successfully!")

