import numpy as np
import pandas as pd


#convert the index of a series into a column od a dataframe (question no 1)
# s1=pd.DataFrame(np.random.rand(20,5),index=np.arange(1,21))
# df=s1.reset_index()
# print(df)

# __________________________________________________________________________________________________________________________________________________

#combine 2 or more series to form  a dataframe(question no 2)

# s2=pd.Series(data=[10,20,30], index=['a','b','c'])
# s3=pd.Series(data=[40,50,60], index=['a','b','c'])
# df=pd.concat([s2,s3],axis=1)
# print(df)

#_______________________________________________________________________________________________________________________________________________

#assign the name of the series (question no 3)

# s4=pd.Series(data=[10,20,30], index=['a','b','c'])
# s4.name='s4series'
# print(s4)

#____________________________________________________________________________________________________________________________________________

#convert a numpy array to a dataframe of agiven shape(question no : 4)

# s5=np.array([[1,2,3],[4,6,7]])
# print(s5)

# shape=(3,2)
# s6=pd.DataFrame(data=s5.reshape(shape))
# print(s6)

#__________________________________________________________________________________________________________________________________________

# Form a DataFrame with 2D list (question no : 5)

# s7=np.array([["JETHALAL","Sodi","Iyer","Babita"],["37","40","53","10"]])
# s8=pd.DataFrame(s7)

# print(s8)

#--------------------------------------------------------------------------------------------------------------------------------------------

#Change the index from 0 to 1 in your dataframe(quetion no 6)

# s9 = pd.DataFrame(np.random.rand(20,5), index=np.arange(0,20))
# print(s9)
# s9 = pd.DataFrame(np.random.rand(20,5), index=np.arange(1,21))
# print(s9)


#__________________________________________________________________________________________________________________________________________

#Reverse the rows of a data frame(question no 7)

# df1=pd.DataFrame(np.random.rand(20,5),index=np.arange(1,21))
# print(df1)

# df2=df1.iloc[::-1]
# print(df2)

#---------------------------------------------------------------------------------------------------------------------------------------------

#concatenate two data frames that are crates(question no 11)

# df1 = pd.DataFrame({'id': ['Hi', 'Hello', 'Haha', 'Hehe'],
#                     'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
  
# df3 = pd.DataFrame({'City': ['Sanjoy', 'Rajesh', 'Ram', 'Raghu'],
#                     'Age': ['12', '13', '14', '12']})
  
  
# result = pd.concat([df1, df3], axis=1, join='inner')
# print(result)


#___________________________________________________________________________________________________________________________________________

#(Question no 10 )

# Df2={
#     "Days":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
#     "Computer":["Acer","Asus","Dell","Lenovo","HP","Apple","Samsung"],
#     "Mouse":["HP","Lenonvo","ASUS","Corsair","Acer","Intex","Logitech"],
#     "Speaker":["Zebronics","Corsair","Bose","Samsung","JBL","Boat","Realtek"]
# }
# k=pd.DataFrame(Df2)
# o=k.set_index("Days")
# print(o)

#_________________________________________________________________________________________________________________________________________


#Q8. Use loc function to print values of a row or a column that should be less than 0.11 in Python
# df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'], index=['R1', 'R2', 'R3', 'R4', 'R5'])
# print(df)
# col_A = df.loc[df['A'] < 0.11, 'A']
# print(col_A)
# row_R2 = df.loc['R2', df.loc['R2'] < 0.11]
# print(row_R2)

#---------------------------------------------------------------------------------------------------------------------------------------------


# #Q9. Take a dataframe of many columns and print 3 columns that are not side by side in Python\
    
    
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18]})
# cols = [0, 2, 4]
# df_3cols = df.iloc[:, cols]
# print(df_3cols)

#_________________________________________________________________________________________________________________________________________