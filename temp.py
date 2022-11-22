import csv

# df = pd.read_excel(io="../cmpsc445_final_project/brand.xlsx", sheet_name="Sheet1")
# df1 = pd.read_excel(io="../cmpsc445_final_project/train_labels.xlsx", sheet_name="Sheet1")
# print(df.head(14))
# print(df1.head(10))

file = open("../cmpsc445_final_project/brand.csv",'r')
csv_reader = csv.reader(file)
rows = list(csv_reader)
print(str(rows[10]))
