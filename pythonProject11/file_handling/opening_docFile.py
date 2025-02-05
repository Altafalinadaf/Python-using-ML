from docx import Document

doc=Document(r'C:\Users\altaf\OneDrive\Documents\my_test.docx')

text=""

for pharagraph in doc.paragraphs:
    text+=pharagraph.text +"\n"

print(text)