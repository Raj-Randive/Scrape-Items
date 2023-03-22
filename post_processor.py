import pandas as pd

datafr = pd.read_csv("D:\pushistov\Scrape-Items\CSVS\datcsvtho2.csv")

for index, row in datafr.iterrows():
    pinpin = row['Pin Code'].removeprefix("Pin : ")
    pinpin = row['Pin Code'].removeprefix(" ")
    if int(pinpin[0]) > 47 and int(pinpin[0]) < 58 : 
        datafr.loc[datafr[index] == index] = [[row['Name of NGOs'], row['Address'].removeprefix("Add : "), row['City'], pinpin, row['State'], row['Mobile No(s).'], row['Email'], row['Website'], row['Name of Contact Person'], row['Purpose'], row['About']]]
    else :
        datafr.loc[datafr[index] == index] = [[row['Name of NGOs'], row['Address'].removeprefix("Add : "), row['City'], row['State'], pinpin, row['Mobile No(s).'], row['Email'], row['Website'], row['Name of Contact Person'], row['Purpose'], row['About']]]
    row['Address'] = row['Address'].removeprefix("Add : ")
    print(row["Address"])

datafr.to_csv("D:/pushistov/Scrape-Items/CSVS/datcsvtho3.csv")