
```
import img2pdf
from PIL import Image

def convert_image_to_pdf(img_path, pdf_path=None):
    try:
        with Image.open(img_path) as image:
            if not pdf_path:
                pdf_path = img_path.rsplit(".", 1)[0] + ".pdf"
            pdf_bytes = img2pdf.convert(image.filename)
            with open(pdf_path, "wb") as file:
                file.write(pdf_bytes)
        print(f"Successfully created PDF: {pdf_path}")
    except FileNotFoundError:
        print("Error: The file was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    img_path = input("Enter the path to your image file: ")
    pdf_path = input("Enter the name for the output PDF file (e.g., output.pdf), or leave blank for auto-generation: ")
    pdf_path = pdf_path.strip() or None
    convert_image_to_pdf(img_path, pdf_path)

if __name__ == "__main__":
    main()
```

