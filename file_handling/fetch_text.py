from docx import Document
file_path = r"C:\Users\altaf\PycharmProjects\pythonProject11\file_handling\Myself.docx"
doc = Document(file_path)
text = ""
for paragraph in doc.paragraphs:
    text+=paragraph.text+"\n"

print(text)
