from file_type_identifier import FileTypeIdentifier
from export_to_text import ExportToText
from name_extarct import extract_names

def main():

    file_path = r"C:\Users\hp\Desktop\New-York-Resume-Template-Creative.pdf"
    file_identifier = FileTypeIdentifier(file_path)
    file_type = file_identifier.identify_file_type()
    if file_type == '.pdf':
        pdf_reader = ExportToText(file_path)
        text = pdf_reader.pdf_to_text()
        print(text)
    if file_type == '.docx' or file_type == '.doc':
        docx_reader = ExportToText(file_path)
        text = docx_reader.docx_to_text()
        print(text)
    if file_type == '.txt':
        txt_reader = ExportToText(file_path)
        text = txt_reader.txt_to_text()
        print(text)

    names = extract_names(text)
 
    if names:
        print(names) 

main()
