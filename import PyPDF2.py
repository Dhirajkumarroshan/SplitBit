import PyPDF2

def read_and_format_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Initialize an empty string to store formatted text
        formatted_text = ""

        # Loop through all pages and extract text
        for page_num in range(num_pages):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            text = page.extract_text

            # Format the text as needed (you can customize this part)
            formatted_text += f"Page {page_num + 1}:\n{text}\n\n"

    return formatted_text

# Example usage
pdf_file_path = 'C:/Users/BR/Downloads/Story.pdf'  # Replace with the path to your PDF file
formatted_text = read_and_format_pdf(pdf_file_path)

# Print the formatted text
print(formatted_text)