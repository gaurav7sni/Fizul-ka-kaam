
<span style="font-size: 36px;">🖼️➡️📄 Image to PDF Converter</span>

A simple Python script that converts image files into high-quality PDFs. Perfect for quick image-to-PDF tasks on any device, including Android (Pydroid), Windows, and Linux!

✨ Features
- ✅ Single-image to PDF conversion
- 📝 Custom PDF file name input
- 🚫 Auto error handling (e.g., file not found)
- ⚡ Auto-generate PDF name if left blank
- 💻 Lightweight & easy to use

🚀 Requirements
- Python 3.x
- Install dependencies: `pip install img2pdf pillow`

🔧 Usage
1. Run the script: `python image_to_pdf.py`
2. Follow the prompts:
    - Enter the path to your image file: `/storage/emulated/0/Download/test_image.png`
    - Enter the name for the output PDF file (e.g., `output.pdf`): `myfile.pdf`
3. Successfully created PDF: `myfile.pdf`

💡 Tip: Leave the PDF name blank, and the script will auto-create one (e.g., `test_image.pdf`).

📂 Example Paths
- `/storage/emulated/0/Download/image.jpg` (Android)
- `C:\Users\Username\Pictures\image.png` (Windows)
- `/home/username/Pictures/image.jpg` (Linux)

⚠️ Notes
- Ensure the image file exists and is accessible.
- The script will overwrite any existing PDF with the same name.

