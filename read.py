import pandas as pd
from functions import pages, beskrivelse

pdf = "Faktura - kort.pdf"

# SIDEANTAL, virker
pages = pages(pdf)
# print(pages)

# BESKRIVELSE COLUMN, virker
df1 = beskrivelse(pdf, 1)
df2 = beskrivelse(pdf, 2)
besk = pd.concat([df1, df2], axis=0)
df = besk
# dfs = []
# ranges = []
# for i in range(1, pages + 1, 1):
#     ranges.append(1)
#     dfs = beskrivelse(pdf, len(ranges))
#     df =

