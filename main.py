from fpdf import FPDF
import pandas as pd

content = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font(family="Times", style="B", size=16)

for index, row in content.iterrows():
    pdf.add_page()
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 22, 200, 22)


# w=width, h= height, txt=content, align=text alignment, ln=# of breaklines, border=border size
pdf.output("output.pdf")
