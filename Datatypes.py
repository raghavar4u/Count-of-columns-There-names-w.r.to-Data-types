dataframe_train.dtypes.value_counts()


Num_cols = Tdata.select_dtypes(include=['float64','int64']).columns.tolist()
Cat_cols = Tdata.select_dtypes(include=['object']).columns.tolist()
print("Number columns : ",Num_cols , "Catogarical columns :" ,Cat_cols,sep="\n")


