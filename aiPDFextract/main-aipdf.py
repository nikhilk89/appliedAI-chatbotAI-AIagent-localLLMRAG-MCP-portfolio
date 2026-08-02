import io
import json
import os
import pypdfium2 as pdfium
from google import genai
from google.genai import types
from PIL import Image, ImageEnhance

# Use API Key
client = genai.Client(api_key="Enter LLM key")

def preprocess_image(image: Image.Image) -> Image.Image:
    # Convert into Grayscale to identify color noise
    gray_img = image.convert("L")

    # increase Contrast
    enhancer = ImageEnhance.Contrast(gray_img)
    enhanced_img = enhancer.enhance(2.0)  # Doubles image contrast

    # increase Sharpness
    sharpness = ImageEnhance.Sharpness(enhanced_img)
    sharpened_img = sharpness.enhance(1.5)

    return sharpened_img.convert("RGB")


def pdf_to_images(pdf_path: str, dpi: int = 300):
#convert to images
    pdf_doc = pdfium.PdfDocument(pdf_path)
    images = []

    for page in pdf_doc:
        pil_img = page.render(scale=dpi / 72).to_pil()
        processed_img = preprocess_image(pil_img)
        images.append(processed_img)

    return images


def extract_data_with_gemini(images: list) -> str:
#send to gemini with instructions and checkbox. form values

    prompt = """
    You are an expert document extraction system specializing in handwritten and scanned tax/intake forms.

    INSTRUCTIONS FOR CHECKBOXES & SELECTIONS:
    - Examine all checkboxes (`[ ]`) and radio buttons
    - A box is considered CHECKED/SELECTED if:
      1. There is a checkmark (✓), cross (X), slash (/), dot, or stroke INSIDE the box.
      2. There is a handwritten mark TOUCHING or OVERLAPPING the box edges or label numbers (e.g. a checkmark crossing through '(1) [ ]').
    - Do NOT ignore stray marks or scribbles near option numbers—they indicate user intent.
    -Extract text EXACTLY as written inside each physical bounding box/line.
    -Do NOT move state abbreviations or ZIP codes to separate JSON fields if they are physically written on the street address line.
    Task:
    Extract all fields, text, and form selections accurately into a clean JSON output.
    For questions with checkboxes, explicitly state which options are selected (`true`) or unselected (`false`).
    """

    contents = []
    contents.extend(images)
    contents.append(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.0  # Lower temperature
        )
    )
    return response.text

# Pipeline Execution
if __name__ == "__main__":
    input_pdf = "hwscan.pdf"
    output_file = "extracted_data.json"

    try:
        print(f"Rendering '{input_pdf}' to high-res image ")
        page_images = pdf_to_images(input_pdf, dpi=300)

        print(f"Sending {len(page_images)} image to Gemini LLM")
        structured_json = extract_data_with_gemini(page_images)

        print("\n JSON Extracted")
        print(structured_json)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(structured_json)

        print(f"\nSaved extracted data to '{output_file}'")

    except Exception as e:
        print(f"Error during processing: {e}")