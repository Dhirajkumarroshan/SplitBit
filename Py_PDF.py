import PyPDF2
import openpyxl

# Open the PDF file in binary mode
pdfFileObj = open('C:/Users/BR/Downloads/Story.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Get the first page
pageObj = pdfReader.pages[0]

# Extract the text from the page
text = pageObj.extract_text()

# Split the text into lines
lines = text.splitlines()

# Create an Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active

# Write the data to the Excel file
row_num = 1
for line in lines:
    sheet.cell(row=row_num, column=1).value = line
    row_num += 1

# Save the Excel file
wb.save('output.xlsx')

# Close the PDF file
pdfFileObj.close()