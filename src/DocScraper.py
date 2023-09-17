import requests
from io import BytesIO
import pdfminer
from pdfminer.high_level import extract_text

# Replace this URL with the URL of the PDF you want to scrape
pdf_url = 'https://www.chevron.com/-/media/shared-media/documents/chevron-sustainability-report-2022.pdf'

# Function to fetch and extract text from a PDF URL
def scrape_pdf_text(url):
    try:
        # Fetch the PDF file from the URL
        response = requests.get(url)
        response.raise_for_status()

        # Create a BytesIO object from the response content
        pdf_bytes = BytesIO(response.content)

        # Extract text from the PDF
        text = extract_text(pdf_bytes)

        return text
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    
# Replace this with the path to your local PDF file
pdf_path = 'Netflix_2022-ESG-Report-FINAL.pdf'

# Function to extract text from a local PDF file
def scrape_local_pdf(pdf_path):
    try:
        # Extract text from the local PDF file
        text = extract_text(pdf_path)

        return text
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    local = False
    
    if local:
        extracted_text = scrape_local_pdf(pdf_path)
    else:
        extracted_text = scrape_pdf_text(pdf_url)

    if extracted_text:
        # Print the extracted text
        print(extracted_text)
    else:
        print("Failed to extract text from the PDF.")
