'''
The goal of the project is and practice time complexity of algorithms while analyzing airplane accidents.
'''

# Open and read the dataset
f = open("AviationData.txt", "r")
reader = f.read()
aviation_data = reader.split("\n")

# Read each line into a list 
aviation_list = [row.split(" | ") for row in aviation_data]

# Search for the "LAX94LA336" by using different algorithms
# Long method O(n**2) iterates the 2 dimension of the list.
lax_code = []
for i in range(len(aviation_list)):
    for j in range(len(aviation_list[i])):
        if aviation_list[i][j] == 'LAX94LA336':
            lax_code.append(aviation_list[i])
                
# Linear method O(n) that searches only the row
lax_code2= []
for row in aviation_list:
    if 'LAX94LA336' in row:
        lax_code2.append(row)

# Create list of dictionaries
column_names = aviation_list[0]
aviation_dict_list = list()
for row in aviation_list[1:]:
    temp_dict = dict()
    for index, item in enumerate(row):
        temp_dict[column_names[index]] = item
    aviation_dict_list.append(temp_dict)

# Search for the "LAX94LA336" by using list of dictionaries
# Still O(n) because there is loop over each row
lax_dict = []
for dictionary in aviation_dict_list:
    if "LAX94LA336" in dictionary.values():
        lax_dict.append(dictionary) 

# Count up how many accidents occurred in each U.S. state, 
# determine which state had the most accidents overall
from collections import Counter
state_accidents_list = []
for row in aviation_dict_list:
    if 'Country' in row:
        if row['Country'] == 'United States':
                state_list = row['Location'].split(", ")
                try:
                    state = state_list[1]
                except:
                    state = ""
                if len(state) == 2:
                    state_accidents_list.append(state)
state_accidents = Counter(state_accidents_list)
state_accidents_most_5 = state_accidents.most_common(5) # Five states where most accidents happened

# Create list how many fatalities and serious injuries occurred during each month
monthly_injuries = []
for dictionary in aviation_dict_list:
    month_injuries = []
    if 'Event Date' in dictionary:
        try:
            f_injuries = int(dictionary['Total Fatal Injuries'])
        except:
            f_injuries = 0
        try:
            s_injuries = int(dictionary['Total Serious Injuries'])  
        except:
            s_injuries = 0
        try:
            month = dictionary['Event Date'].split('/')[0]
            year = dictionary['Event Date'].split('/')[2]
            date = month + '/' +  year
        except:
            date = ''    
        month_injuries.append(date)
        month_injuries.append(f_injuries)
        month_injuries.append(s_injuries)
    monthly_injuries.append(month_injuries)  

# Count fatal and serious injuries happened in each month
    f_counter = Counter()
    s_counter = Counter()    
for each in monthly_injuries:
    try:
        date = each[0]
        fatal = each[1]
        serious = each[2]
        if date != '':
            f_counter[date] += fatal
            s_counter[date] += serious
    except:
        continue       

most_fatal_monthly_5 = f_counter.most_common(5) # Five months when most fatal injuries happened
most_serious_monthly_5 = s_counter.most_common(5) # Five months when most serious injuries happened          
