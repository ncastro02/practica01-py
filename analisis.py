import pandas as pd
#dataFrame=pd.DataFrame
excelData=pd.read_excel('#link')
dataFrame=pd.DataFrame(excelData)
dataFrame.head()