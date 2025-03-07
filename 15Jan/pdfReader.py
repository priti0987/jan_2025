import PyPDF2
import re
#pdf reader
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    return emails
def read_pdf_line_by_line(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            lines = page.extract_text().split("\n")  # Extract text and split by lines
            for line in lines:
                #print(line)  # Process each line
                emails = extract_emails(line)
                emails = " ".join(emails)
                if emails :
                    print(emails)

pdf_path = "C:\\Users\\Dell\\Downloads\\QA3.pdf"
read_pdf_line_by_line(pdf_path)
