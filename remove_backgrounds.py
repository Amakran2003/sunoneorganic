#!/usr/bin/env python3
"""
Background Removal Script for Vegetable Images
Automatically removes backgrounds from all images in the images folder
"""

import os
from PIL import Image
from rembg import remove
import glob

def remove_background_from_image(input_path, output_path):
    """Remove background from a single image"""
    try:
        print(f"Processing: {input_path}")
        
        # Open and process the image
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
        
        # Remove background
        output_data = remove(input_data)
        
        # Save the result
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)
        
        print(f"✅ Saved: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {input_path}: {str(e)}")
        return False

def main():
    """Main function to process all images"""
    # Define paths
    images_dir = "images"
    output_dir = "images/no_bg"
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    # Supported image formats
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.webp', '*.bmp', '*.tiff']
    
    # Find all image files
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(images_dir, extension)))
    
    if not image_files:
        print("❌ No image files found in the images directory")
        return
    
    print(f"Found {len(image_files)} image(s) to process")
    print("-" * 50)
    
    successful = 0
    failed = 0
    
    # Process each image
    for image_path in image_files:
        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)
        
        # Output as PNG to preserve transparency
        output_filename = f"{name}_no_bg.png"
        output_path = os.path.join(output_dir, output_filename)
        
        if remove_background_from_image(image_path, output_path):
            successful += 1
        else:
            failed += 1
    
    print("-" * 50)
    print(f"✅ Successfully processed: {successful} images")
    print(f"❌ Failed to process: {failed} images")
    print(f"\n🎉 Background-free images saved in: {output_dir}")
    
    if successful > 0:
        print("\n📝 Next steps:")
        print("1. Check the processed images in the 'images/no_bg' folder")
        print("2. Replace the original images in your HTML if you're satisfied")
        print("3. Update image paths in your HTML file if needed")

if __name__ == "__main__":
    main()
