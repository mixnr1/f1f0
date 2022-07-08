from itertools import count
import config
import pandas as pd

def atlikums_aprekinasana(nested_list, list):
    if list[3]>0: 
        nested_list.append([list[0], list[1], list[2], list[3]])
        print(nested_list)
    else:
        for i in range(len(nested_list)):
            if (list[3]<0)==True and ((nested_list[i][3]+list[3])>0)==True: 
                iegades_kurss=nested_list[i][2]
                iegades_datums=nested_list[i][0]
                pardotie_btc=list[3]
                iegades_vertiba=abs(round((pardotie_btc*iegades_kurss),2))
                atlikums_no_pardosanas=nested_list[i][3]+list[3]
                atlikuma_vertiba_no_pardosanas=round((iegades_kurss*atlikums_no_pardosanas),2)
                pardosanas_kurss=list[2]
                pardosanas_datums=list[0]
                pardosanas_vertiba=abs(round((pardotie_btc*pardosanas_kurss),2))
                pelna=round((pardosanas_vertiba-iegades_vertiba),2)
                nodoklis=round((pelna*0.2),2)
                #updated_fields_after_transaction
                nested_list[i][1]=atlikuma_vertiba_no_pardosanas #'EUR'
                nested_list[i][3]=atlikums_no_pardosanas #'BTC'
                # print("FINAL Pārdoti", abs(pardotie_btc), "BTC, kas iegādāti", iegades_datums, "par", iegades_kurss, "EUR (",round(iegades_vertiba,2),"EUR ). Pardosanas kurss (",pardosanas_datums,"):", pardosanas_kurss, "EUR/BTC; Pārdošanas vērtība:", round(pardosanas_vertiba, 2), "EUR. Peļņa:",pelna, "EUR. Nodoklis:",nodoklis, "EUR")
                print(nested_list, "FINAL SELL", abs(pardotie_btc),"| BUY_date",iegades_datums,"| BUY_rate",iegades_kurss,"| BUY_value",round(iegades_vertiba,2),"| SELL_date",pardosanas_datums,"| SELL_rate", pardosanas_kurss, "| SELL_value", round(pardosanas_vertiba, 2), "| Profit",pelna, "| TAX",nodoklis)
                break
            elif (list[3]<0)==True and ((nested_list[i][3]+list[3])<0)==True:
                iegades_kurss=nested_list[i][2]
                iegades_datums=nested_list[i][0]
                pardotie_btc=nested_list[i][3]#!!!!!!!!!!!!!!!!!!
                iegades_vertiba=abs(round((pardotie_btc*iegades_kurss),2))
                atlikums_no_pardosanas=nested_list[i][3]+list[3]
                atlikuma_vertiba_no_pardosanas=round((iegades_kurss*atlikums_no_pardosanas),2)
                atlikums_no_pardosanas_vertiba=round((atlikums_no_pardosanas*list[2]),2)
                pardosanas_kurss=list[2]
                pardosanas_datums=list[0]
                pardosanas_vertiba=abs(round((pardotie_btc*pardosanas_kurss),2)) 
                pelna=round((pardosanas_vertiba-iegades_vertiba),2)
                nodoklis=round((pelna*0.2),2)
                #updated_fields_after_transaction
                nested_list[i][1]=0 #'EUR'
                nested_list[i][3]=0 #'BTC'
                list[1]=atlikums_no_pardosanas_vertiba #'EUR'
                list[3]=atlikums_no_pardosanas #'BTC'
                # print("OUTGOING Pārdoti", pardotie_btc, "BTC, kas iegādāti", iegades_datums, "par", iegades_kurss, "EUR (",round(iegades_vertiba,2),"EUR ). Pardosanas kurss (",pardosanas_datums,"):", pardosanas_kurss, "EUR/BTC; Pārdošanas vērtība:", round(pardosanas_vertiba, 2), "EUR. Peļņa:",pelna, "EUR. Nodoklis:",nodoklis, "EUR")
                print(nested_list, "OUTGI SELL", pardotie_btc, "| BUY_date", iegades_datums, "| BUY_rate", iegades_kurss, "| BUY_value",round(iegades_vertiba,2),"| SELL_date",pardosanas_datums,"| SELL_rate", pardosanas_kurss, "| SELL_value", round(pardosanas_vertiba, 2), "| Profit",pelna, "| TAX",nodoklis)
                

file_path=config.file_path
df = pd.read_excel(file_path)
fifo_list=[]
for index, row in df.iterrows():
    atlikums_aprekinasana(fifo_list, [row['Datums'], row['EUR'], row['EUR/BTC'], row['BTC']])

# for i in fifo_list:
#     print(i)