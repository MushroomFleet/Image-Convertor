# 🖼️ Image to PNG Converter 🔄

A simple yet powerful tool to convert images from various formats (including AVIF, JPEG, WebP, HEIC) to PNG format while preserving filenames and directory structure.

## ✨ Features

- 🔄 Converts images to PNG format while preserving transparency
- 📂 Supports recursive directory processing
- 🌈 Handles a wide variety of image formats (AVIF, JPEG, WebP, HEIC, GIF, etc.)
- 🔍 Easy to use command-line interface
- 🚀 Includes a user-friendly batch file for Windows users
- 📝 Detailed conversion reports and error handling

## 📋 Requirements

- Python 3.6 or higher
- Pillow library (automatically installed by the batch file)
- pillow-avif-plugin for AVIF support (automatically installed by the batch file)

## 🚀 Installation

### Method 1: Clone the Repository

```bash
# Clone this repository
git clone https://github.com/yourusername/image-to-png-converter.git

# Navigate to the project directory
cd image-to-png-converter

# Install required libraries
pip install Pillow pillow-avif-plugin
```

### Method 2: Download the Files Directly

1. 📥 Download `image_converter.py` and `convert_images.bat` from this repository
2. 📁 Place them in a directory of your choice
3. 🔧 The batch file will automatically check for dependencies and install them if needed

## 🎮 Usage

### Using the Batch File (Windows)

1. 🖱️ Double-click on `convert_images.bat`
2. 📂 Enter the path to your images when prompted
3. 📁 Optionally specify an output directory
4. ✅ Choose whether to process subdirectories
5. 🎉 Let the tool do its magic!

### Using the Python Script Directly

For more control, you can use the Python script directly:

```bash
# Basic usage
python image_converter.py /path/to/images

# With output directory
python image_converter.py /path/to/images -o /path/to/output

# Process subdirectories recursively
python image_converter.py /path/to/images -r

# Both output directory and recursive processing
python image_converter.py /path/to/images -o /path/to/output -r
```

## 📚 Command Line Arguments

| Argument | Description |
|----------|-------------|
| `input_dir` | Directory containing images to convert |
| `-o, --output-dir` | Directory to save converted images (optional) |
| `-r, --recursive` | Process subdirectories recursively (optional) |

## 🌟 Examples

### Example 1: Convert all images in a folder

```bash
python image_converter.py C:\Users\YourName\Pictures\vacation_photos
```

### Example 2: Convert all images and save to another folder

```bash
python image_converter.py C:\Users\YourName\Pictures\vacation_photos -o C:\Users\YourName\Pictures\vacation_photos_png
```

### Example 3: Convert all images including those in subfolders

```bash
python image_converter.py C:\Users\YourName\Pictures\vacation_photos -r
```

## 📊 Output

The tool provides a summary after conversion:

```
Conversion Summary:
Converted: 42
Failed: 0
Skipped: 3
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 🙏 Acknowledgements

- [Pillow](https://python-pillow.org/) - The Python Imaging Library
- All the open-source contributors that make projects like this possible 💖

## 📧 Contact

If you have any questions or feedback, please open an issue on this repository.

---

Made with ❤️ by [Your Name]
