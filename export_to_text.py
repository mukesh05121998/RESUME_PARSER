import PyPDF2
import docx

class ExportToText:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def pdf_to_text(self):
        text = ""
        with open(self.file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        return text
    
    def docx_to_text(self):
        text = ""
        doc = docx.Document(self.file_path)

        for paragraph in doc.paragraphs:
            text += paragraph.text

        return text
    
    def txt_to_text(self):
        text = ""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        return text


