import PyPDF2

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

