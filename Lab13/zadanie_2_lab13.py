import pandas as pd

def main():
    content = pd.read_excel("sample_pivot.xlsx")
    #print(content)
    loc_18 = content.loc[content["Units"]==18]
    wiersz = content.iloc[999]
    print(loc_18)
    print(wiersz)
    result = content.loc[content['Date'].dt.month == 8]
    print(result)
    x = content["Units"]
    y = content["Sales"]
    multiples = x * y
    content["Total Profit"] = multiples
    print(content)
    data = (content.groupby(by="Region").mean())
    print(data)

main()