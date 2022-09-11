from ast import literal_eval
from fileinput import filename
from bs4 import BeautifulSoup
import urllib3
import os
import re
import pandas as pd
from datetime import datetime

#### Global variable declaration #####
today = datetime.today().strftime('%Y-%m-%d') #declare today's date as date
df_list = []

http = urllib3.PoolManager()

#Import urls lists from excel file
os.chdir("C:\\Users\\macie\\OneDrive\\Data Science\\Python\\B3_Scrap")
assets_list = pd.read_excel("assets_list.xlsx")
#print(assets_list)

# ----- loop function to get data from web and create dataframe for the listed assets ----- #
for lab, row in assets_list.iterrows() :

    #get data from the web and turn it into a text (string)
    url = str(row['url'])
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data)

    raw = BeautifulSoup.get_text(soup)

    #separate string with relevant data
    sep_string = re.search('BVMF:(.*)Próximos Resultados', raw)
    sep_string = str(sep_string.group(1))

    #extract close price of the stock in the specified day
    close = re.search('Fechamento Anterior(.*)Var. Diária', sep_string)
    close = float(close.group(1).replace(',', '.')) #coerce variable to float and replace comma to dot

    #extract low price of the stock  in the specified day
    low = re.search('Var. Diária(.*)Receita', sep_string)
    low = str(low.group(1))
    low = low.split("-")
    low = low[0]

    low = float(low.replace(',', '.'))

    #extract high price of the stock in the specified day
    high = re.search('Var. Diária(.*)Receita', sep_string)
    high = str(high.group(1))
    high = high.split("-")
    high = high[1]

    high = float(high.replace(',', '.'))

    #Next step: transform extracted data into a vector

    asset_dict = { 'asset': row['asset'],
                'date': [today],
                'close': [close],
                'low': [low],
                'high': [high] }

    lab = pd.DataFrame(data=asset_dict)

    df_list.append(lab)
    print(lab)


#create the final dataframe
final = pd.concat(df_list)
print(final)

file_name = str('AssetExtract' + '_' + str(today) + ".xlsx")
final.to_excel(file_name)
