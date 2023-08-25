from fpdf import FPDF
import pandas as pd

content = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
for index, row in content.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 22, 200, 22)

    for i in range(22, 280, 10):
        pdf.line(10, i, 200, i)

    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)
    for i in range(row["Pages"]-1):
        pdf.add_page()

        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

        for j in range(12, 280, 10):
            pdf.line(10, j, 200, j)



# w=width, h= height, txt=content, align=text alignment, ln=# of breaklines, border=border size
pdf.output("output.pdf")
