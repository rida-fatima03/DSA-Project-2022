#pip install fpdf
#PyFPDF is a Python library for creating PDF documents.
from fpdf import FPDF
# FPDF() class should be saved into a variable named pdf.
pdf = FPDF()
# Add a page
pdf.add_page()
#Set the textual style and size that you need in the pdf.
pdf.set_font("Arial", size = 15)
# create a cell
pdf.cell(200, 10, txt = "Bake O' Clock", 
        ln = 1, align = 'C')
# Insert another cell
pdf.cell(200, 10, txt = "Sample Text",
        ln = 2, align = 'C')
# Save the pdf with the extension.pdf.
pdf.output("Reciept.pdf")   
