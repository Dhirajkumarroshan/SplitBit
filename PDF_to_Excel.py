import PyPDF2
import pandas as pd

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text
    return text

def export_to_excel(text, excel_path):
    lines = text.split('\n')
    data = [line.split() for line in lines if line.strip()]

    df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4"])  # Adjust column names as needed

    df.to_excel(excel_path, index=False)

if __name__ == "__main__":
    pdf_path = "C:/Users/BR/Downloads/Story.pdf"
    excel_path = "C:/Users/BR/Downloads/output_excel_file.xlsx"

    text = extract_text_from_pdf(pdf_path)
    export_to_excel(text, excel_path)

    print(f"PDF content has been exported to {excel_path}")
