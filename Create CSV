import csv
#sample header
header = ['Area', 'Name', 'Email', 'Passowrd']
#sample data
data = [
    ['Albania', "Alan Lane", 'AL.hotmail.com', 'ALB'],
    ['Algeria', "Danial Zafar", 'DZ.hotmail.com', 'DZA'],
    ['America', "Ally Smith", 'AS.gmail.com', 'ASM'],
    ['Pakistan', "Abdullah Zafar", 'AZ.gmail.com', 'AND'],
    ['India', "Anne Omaha", 'AO.gmail.com', 'AGO']
]
#open the file
with open("/Users/muminahkhurram/downloads/CSV_bakery.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
   #create header
    writer.writerow(header)
   #create rows
    writer.writerows(data)
