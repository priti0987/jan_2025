import PyPDF2

path="C:\\Users\\Dell\\Downloads\\Priti Fuse.pdf"
with open(path,"rb") as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        lines = page.extract_text().split("\n")
        for line in lines:
            if "E" in line:
                print(line)
