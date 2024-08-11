'''
date_time = 2024-08-08 23:59:00
take above data as example
do date, time = date_time.split(' ')
date = 2024-08-08


1. for day analysis :
analysis_date_temperatures_list = []
analysis_of_which_date = date[7:] // date_analysis-date = '08'
temp_date = analysis_of_which_date
for i in range(len(date_list)): // date_list is the list consisting of all dates in the csv file
    if date_list[i][7:] == analysis_of_which_date: // to check if the date is correct
        analysis_date_temperatures_list.append(temperature_list[i])
    else:
        break
// temperature list has been created, to get max and min values, just use max and min functions

2. for month analysis :
analysis_month_temperatures_list = []
analysis_of_which_month = date[4:7] //check the index numbers once 
temp_month = analysis_of_which_month
for i in range(len(date_list)): // date_list is the list consisting of all dates in the csv file
    if date_list[i][4:7] == analysis_of_which_month: // to check if the month is same
        analysis_month_temperatures_list.append(temperature_list[i])
    else:
        break
// temperature list has been created, to get max and min values, just use max and min functions
'''

def temperature(day_or_month_choice):
    print("You have chosen temperature")
    if day_or_month_choice==1:
        # write code for day
        pass
    else:
        # write code for month
        pass
    pass