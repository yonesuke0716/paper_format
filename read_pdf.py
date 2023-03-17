from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO


pdf_file_path = "Vuforia Developer Agreement.pdf"

with open(pdf_file_path, "rb") as pdf_file:
    output = StringIO()
    resource_manager = PDFResourceManager()
    laparams = LAParams()
    text_converter = TextConverter(resource_manager, output, laparams=laparams)
    page_interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for i_page in PDFPage.get_pages(pdf_file):  # 1ベージずづ処理
        page_interpreter.process_page(i_page)

    output_text = output.getvalue()
    output.close()
    text_converter.close()

print(output_text)
