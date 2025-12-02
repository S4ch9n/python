import pandas as pd
from narwhals import String

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