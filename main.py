from file_type_identifier import FileTypeIdentifier
from export_to_text import ExportToText
from resume_parser import resumeparse

def main():

    file_path = r"C:\Users\chauh\Dropbox\My PC (LAPTOP-FK372CTA)\Downloads\Resume (4).pdf"
    file_identifier = FileTypeIdentifier(file_path)
    file_type = file_identifier.identify_file_type()
    if file_type == '.pdf':
        pdf_reader = ExportToText(file_path)
        text = pdf_reader.pdf_to_text()
        response = resumeparse.read_file(file_path)
        print(response)
    
main()