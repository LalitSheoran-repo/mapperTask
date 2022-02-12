import pandas as pd
from fuzzywuzzy import  fuzz
df = pd.read_excel('dataset.xlsx')
df = df.drop(["_id"], axis=1)

filteredData = df.loc[(df['fuel'] == 'diesel') & (df['seatingCapacity'] == 3)]
filteredData = filteredData.values.tolist()
make = "mahindra"
modelVariant = "blazoGvw"

if any(filteredData):
    output = []

    for row in filteredData:
        makeMatch = fuzz.ratio(str(row[0]), make)
        modelMatch = fuzz.ratio(str(row[1]), modelVariant)
        variantMatch = fuzz.ratio(str(row[2]), modelVariant)
        output.append((makeMatch + modelMatch + variantMatch) / 3)

    score = max(output)
    result = filteredData[output.index(score)]
    print( {
        "make": result[0],
        "model": result[1],
        "variant": result[2],
        "fuel": result[3],
        "seatingCapacity": result[4],
        "Score": score
     })