import tabula
import pandas as pd
print('START::::::::::::::::::::::::::::::::::::::::::::::')
frames = []
for i in range(0,10): #in range(startPage, endPage):
    df = tabula.read_pdf("sample.pdf", multiple_tables=True, pages=i)[0]
    frames.append(df)
df = pd.concat(frames)
print('DATA CAPTURED::::::::::::::::::::::::::::::::::::::::::::::')
df.to_excel('sample.xlsx')
print('OPERATION END:::::::::::::::::::::::::::::::::::::::::::::')
