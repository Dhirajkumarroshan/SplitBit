import PyPDF2
import csv

def extract_pdf_data(pdf_file):
    # Open the PDF file in binary mode
    with open(pdf_file, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty list to store extracted data
        data = []

        # Iterate through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page object
            page = pdf_reader.pages(page_num)
            
            # Extract text from the page
            text = page.extractText()

            # Split the text into lines
            lines = text.split('\n')

            # Extract relevant data from each line (customize this part based on your PDF structure)
            for line in lines:
                # Example: Extracting data assuming it's comma-separated
                data.append(line.split(','))

    return data

def export_to_csv(data, csv_file):
    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)

        # Write data to the CSV file
        csv_writer.writerows(data)

if __name__ == "__main__":
    # Replace 'your_pdf_file.pdf' with the path to your PDF file
    pdf_file_path = 'C:/Users/BR/Downloads/Story.pdf'

    # Replace 'output.csv' with the desired CSV file name
    csv_file_path = 'output.csv'

    # Extract data from the PDF
    extracted_data = extract_pdf_data(pdf_file_path)

    # Export data to CSV
    export_to_csv(extracted_data, csv_file_path)

    print(f"Data extracted from {pdf_file_path} and exported to {csv_file_path}")
