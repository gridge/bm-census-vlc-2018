import pandas as pd
import csv

years = range (2017, 2019)
modified = pd.DataFrame()

for y in years: #go through the files, add them to a dataframe
    path = '/Users/red/Desktop/bmdata/'#make sure to change the path
    fileName = path + str(y) + '.csv'
    #print("Loading %s" % fileName)
    data_frame = pd.read_csv(fileName)
    data_frame['year'] = y
    modified = modified.append(data_frame)

#print(modified.groupby('year').size())
#print(list(modified .iloc[1:,]))

#reduce the number of columns
best_descr_df = pd.DataFrame()
best_descr_df[['Respondent ID',
               'Best Description – Degree of Involvement',
               'Best Description – Playa Only',
               'Best Description – New volunteer',
               'Best Description – Veteran',
               'Best Description – In remission',
               'Best Description – Historal',
               'year']] = modified[['Respondent ID',
               'Best Description – Degree of Involvement',
               'Best Description – Playa Only',
               'Best Description – New volunteer',
               'Best Description – Veteran',
               'Best Description – In remission',
               'Best Description – Historal',
               'year']]
#count each category
print(best_descr_df.count())

