import config
import pandas as pd

def atlikums_positive(atlikums, list):
    for i in range(len(list)):
        if (atlikums<0)==True:
            price=list[i][1]
            if (list[i][2]+atlikums<0)==True:
                # sell=atlikums
                print("I",price)
                print("I",atlikums)
                atlikums = list[i][2]+atlikums
                print("I",atlikums)
                print("I",list[i][2])
                list[i][0]=0
                list[i][1]=0
                list[i][2]=0
                print("I",list)
                # print(list,"|?:",atlikums))
            else:
                sell=atlikums
                print("!!!!Orginal_Buy_Price: ",price)
                print("???Units_Sold: ",sell)
                print("!!!!Orginal_Buy_Units: ",list[i][2])
                atlikums = list[i][2]+atlikums
                print("?Remainder_of_orginal_units_after_sale:",atlikums)
                print("?Remainder_of_orginal_units_after_sale: ",atlikums)
                list[i][0]=round(atlikums*list[i][1])
                print("Remainder_of_orginal_EUR(BUY)_value:",list[i][0])
                list[i][2]=atlikums
                print("?Remainder_of_orginal_units_after_sale:",list[i][2])
                print("E",list) #ORGINAL SELL PRICE, ORGINAL EUR 
                break
file_path=config.file_path
df = pd.read_excel(file_path)
fifo_list=[]
for index, row in df.iterrows():
    if row['BTC'] > 0:
        fifo_list.append([round(row['EUR'],2), round(row['EUR/BTC'],2),row['BTC']])
        print(fifo_list)
    else:
        for i in range(len(fifo_list)):
            if (row["BTC"]<0)==True:
                if (fifo_list[i][2]+row['BTC']<0)==True:
                    pass
                elif (fifo_list[i][2]+row['BTC']>0)==True:
                    atlikums_positive(row['BTC'], fifo_list)
                    break        
