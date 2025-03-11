import os
import sys
import argparse
from pathlib import Path
try:
    from PIL import Image
    # Try to import the pillow_avif plugin for AVIF support
    try:
        from pillow_avif import AvifImagePlugin
    except ImportError:
        print("Warning: pillow_avif plugin not found. AVIF files might not be supported.")
except ImportError:
    print("Error: Pillow is required. Please install it with 'pip install Pillow pillow-avif-plugin'")
    sys.exit(1)


def convert_to_png(input_dir, output_dir=None, recursive=False):
    """
    Convert all images in the input directory to PNG format.
    
    Args:
        input_dir (str): Directory containing images to convert
        output_dir (str, optional): Directory to save converted images. 
                                     If None, saves in the same directory as input.
        recursive (bool): Whether to process subdirectories recursively
    """
    # Create output directory if specified and doesn't exist
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get list of files to process
    if recursive:
        # Walk through all subdirectories
        all_files = []
        for root, _, files in os.walk(input_dir):
            for file in files:
                all_files.append(os.path.join(root, file))
    else:
        # Only process files in the input directory
        all_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) 
                    if os.path.isfile(os.path.join(input_dir, f))]
    
    # Supported image formats by PIL
    supported_formats = {'.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp',  # JPEG
                         '.png',  # PNG
                         '.gif',  # GIF
                         '.webp',  # WebP
                         '.tiff', '.tif',  # TIFF
                         '.bmp',  # BMP
                         '.ico', '.cur',  # ICO
                         '.avif',  # AVIF
                         '.heic', '.heif',  # HEIC/HEIF
                         '.jp2', '.j2k', '.jpx', '.jpf',  # JPEG 2000
                         '.svg',  # SVG
                         '.ppm', '.pgm', '.pbm'  # Netpbm
                         }
    
    converted_count = 0
    failed_count = 0
    skipped_count = 0
    
    # Process each file
    for file_path in all_files:
        # Get file extension
        file_ext = os.path.splitext(file_path)[1].lower()
        
        # Skip if not a supported image format
        if file_ext not in supported_formats:
            skipped_count += 1
            continue
        
        try:
            # Create output path
            if output_dir:
                # Preserve directory structure when using recursive mode
                if recursive:
                    rel_path = os.path.relpath(file_path, input_dir)
                    rel_dir = os.path.dirname(rel_path)
                    
                    # Create subdirectory in output_dir if it doesn't exist
                    if rel_dir:
                        out_subdir = os.path.join(output_dir, rel_dir)
                        if not os.path.exists(out_subdir):
                            os.makedirs(out_subdir)
                    
                    # Get output file path
                    filename = os.path.basename(file_path)
                    base_name = os.path.splitext(filename)[0]
                    output_path = os.path.join(output_dir, rel_dir, f"{base_name}.png")
                else:
                    # Simple output path for non-recursive mode
                    filename = os.path.basename(file_path)
                    base_name = os.path.splitext(filename)[0]
                    output_path = os.path.join(output_dir, f"{base_name}.png")
            else:
                # Output in the same directory
                base_name = os.path.splitext(file_path)[0]
                output_path = f"{base_name}.png"
            
            # Skip if output file already exists
            if os.path.exists(output_path):
                print(f"Skipping: {file_path} (output file {output_path} already exists)")
                skipped_count += 1
                continue
            
            # Open and convert image
            with Image.open(file_path) as img:
                # Convert to RGB if the image has an alpha channel
                if img.mode == 'RGBA':
                    # Preserve transparency
                    img.save(output_path, 'PNG')
                else:
                    # Convert to RGB for other color modes
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    img.save(output_path, 'PNG')
            
            print(f"Converted: {file_path} -> {output_path}")
            converted_count += 1
            
        except Exception as e:
            print(f"Error converting {file_path}: {str(e)}")
            failed_count += 1
    
    # Print summary
    print("\nConversion Summary:")
    print(f"Converted: {converted_count}")
    print(f"Failed: {failed_count}")
    print(f"Skipped: {skipped_count}")


def main():
    parser = argparse.ArgumentParser(description='Convert images to PNG format')
    parser.add_argument('input_dir', help='Directory containing images to convert')
    parser.add_argument('-o', '--output-dir', help='Directory to save converted images')
    parser.add_argument('-r', '--recursive', action='store_true', 
                        help='Process subdirectories recursively')
    args = parser.parse_args()
    
    convert_to_png(args.input_dir, args.output_dir, args.recursive)


if __name__ == '__main__':
    main()