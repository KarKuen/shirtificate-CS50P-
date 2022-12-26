from fpdf import FPDF

def main():
    name = start()
    pdf = image()
    pdf = header(pdf)
    pdf = text(pdf, name)
    final(pdf)

def start():
    return(input('Name: ').title())

def image():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image('shirtificate.png', 8, 50, 190)
    return(pdf)

def header(pdf):
    pdf.set_font('helvetica', 'B', size=40)
    pdf.text(50, 30, txt='CS50 Shirtificate')
    return(pdf)

def text(pdf, name):
    pdf.set_font('helvetica', 'B', size=20)
    pdf.set_text_color(255)
    pdf.cell(190, 200, txt=f'{name} took CS50', align='C')
    return(pdf)

def final(pdf):
    pdf.output('shirtificate.pdf')

if __name__ == '__main__':
    main()