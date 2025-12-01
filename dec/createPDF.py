from fpdf import FPDF

pdf = FPDF(orientation = 'P',unit = 'pt',format = 'A4')
pdf.add_page()

pdf.image('IMG_20191031_200556.jpg',w=80,h=50)
pdf.set_font(family="Times",style = 'B',size= 24)
pdf.cell(w=0,h=50,text="Priti",align='C',ln = 1)
pdf.set_font(family="Times",style='B',size=14)
pdf.cell(w=0,h=50,text="Description",ln=1)
pdf.set_font(family="Times",size=12)

pdf.output('output.pdf')