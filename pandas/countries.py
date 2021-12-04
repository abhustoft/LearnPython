dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
#print(brics)

# Import the cars.csv data: cars
import os
print("Read from:" + os.getcwd() + "/cars.csv")
cars = pd.read_csv(os.getcwd() + "/cars.csv")

# Print out country column as Pandas Series
#print(cars['make'])

# Print out country column as Pandas DataFrame
#print(cars[['make']])

# Print out DataFrame with country and drives_right columns
#print(cars[['make', 'year']])

#print(cars[3:5])

# Print out observation for Japan
print("iloc:")
print(cars.iloc[2])

index = cars.index

a_list = list(index)

print(a_list)

# Print out observations for Australia and Egypt
print("loc:")
#print(cars.loc[ [True, False, True, False, True]])
print(cars.loc[0])

#junior = pd.read_csv(os.getcwd() + "/pandas/" + "Junior.csv")

# Print out cars
#print(cars)
#print(junior)

