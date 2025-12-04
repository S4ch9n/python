import pandas as pd
from narwhals import String
from streamlit import dataframe

data = {
    "apple":  [0, 3, 4, 2],
    "orange": [2, 1, 3, 4]
}
#pd.DataFrame() is used to create table like structure (rows -columns) in pandas.
#its full signature is pd.DataFrame(data=None, index=None, columns=None, dtype=None)


# Creating the DataFrame (default index 0,1,2,3)
# df = pd.DataFrame(data)
#creating the Dataframe (with given index "A" , "B" , "C" , "D"
df = pd.DataFrame(data , index = ["A" , "B" , "C" , "D"])
print(df)


data2 = {
    1 : ["Nick" , "John"],
    2 : ["Alex" , "Bella"]
}
df2 = pd.DataFrame(data2 , index = ["x" , "y"] , columns = ["Name" , "Name"] , dtype = String)
print(df2)



#data analysis  - > data cleaning : handling missing values , invalid data , noisy data.
import pandas as pd

data3 = {
    "Name": ["John", "Anna", None, "Mark"],
    "Age": [25, None, 30, "40"],
    "City": ["NY", "LA", "NY", "LA"],
    "Salary": ["50000", "60000", None, "70000"]
}

df3 = pd.DataFrame(data3)
#Check basic info


