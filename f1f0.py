import pandas as pd
import argparse
 

def atlikums_aprekinasana(nested_list, list):
    if list[3]>0: 
        nested_list.append([list[0], list[1], list[2], list[3]])
    else:
        for i in range(len(nested_list)):
            if (list[3]<0)==True and ((nested_list[i][3]+list[3])>0)==True: 
                iegades_kurss=nested_list[i][2]
                iegades_datums=nested_list[i][0]
                pardotie_btc=list[3]
                iegades_vertiba=abs((pardotie_btc*iegades_kurss))
                atlikums_no_pardosanas=nested_list[i][3]+list[3]
                atlikuma_vertiba_no_pardosanas=(iegades_kurss*atlikums_no_pardosanas)
                pardosanas_kurss=list[2]
                pardosanas_datums=list[0]
                pardosanas_vertiba=abs((pardotie_btc*pardosanas_kurss))
                pelna=pardosanas_vertiba-iegades_vertiba
                nodoklis=pelna*0.2
                nested_list[i][1]=atlikuma_vertiba_no_pardosanas 
                nested_list[i][3]=atlikums_no_pardosanas 
                print(pardosanas_datums,\
                ",", pardosanas_kurss, \
                ",", abs(pardotie_btc),\
                ",", pardosanas_vertiba, \
                ",",iegades_datums,\
                ",",iegades_kurss,\
                ",",iegades_vertiba,\
                ",",pelna, \
                ",",nodoklis)
                break
            elif (list[3]<0)==True and ((nested_list[i][3]+list[3])<0)==True:
                iegades_kurss=nested_list[i][2]
                iegades_datums=nested_list[i][0]
                pardotie_btc=nested_list[i][3]
                iegades_vertiba=abs((pardotie_btc*iegades_kurss))
                atlikums_no_pardosanas=nested_list[i][3]+list[3]
                atlikuma_vertiba_no_pardosanas=((iegades_kurss*atlikums_no_pardosanas))
                atlikums_no_pardosanas_vertiba=atlikums_no_pardosanas*list[2]
                pardosanas_kurss=list[2]
                pardosanas_datums=list[0]
                pardosanas_vertiba=abs(pardotie_btc*pardosanas_kurss)
                pelna=pardosanas_vertiba-iegades_vertiba
                nodoklis=pelna*0.2
                nested_list[i][1]=0 
                nested_list[i][3]=0 
                list[1]=atlikums_no_pardosanas_vertiba 
                list[3]=atlikums_no_pardosanas 
                print(pardosanas_datums,\
                ",", pardosanas_kurss,\
                ",", pardotie_btc,\
                ",", pardosanas_vertiba, \
                ",", iegades_datums, \
                ",", iegades_kurss, \
                ",", iegades_vertiba,\
                ",", pelna, \
                ",", nodoklis)

def main(input_file, column_name):
    file_path=input_file
    df = pd.read_excel(file_path)
    fifo_list=[]
    print("sell_date, sell_price, sell_amount, sell_value, buy_date, buy_price, buy_value, profit, tax")
    for index, row in df.iterrows():
        atlikums_aprekinasana(fifo_list, [row[column_name[0]], row[column_name[1]], row[column_name[2]], row[column_name[3]]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FIFO calculator")
    parser.add_argument("-f", "--file", help="path to input file")
    parser.add_argument("-c", "--column_names", nargs='+', default=['Datums', 'EUR', 'EUR/BTC', 'BTC'])
    args = parser.parse_args()
    main(args.file, args.column_names)
