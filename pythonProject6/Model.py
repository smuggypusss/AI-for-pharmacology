import numpy as np
import pandas as pd
import pickle
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
df=pd.read_csv('C:/Users/Asus/Untitled Folder 1/final_df_3.csv')
X=df.drop('pIC50',axis=1)
y=df['pIC50']
def remove_low_variance(input_data, threshold=0.1):
    selection = VarianceThreshold(threshold)
    selection.fit(input_data)
    return input_data[input_data.columns[selection.get_support(indices=True)]]
X=remove_low_variance(X,threshold=0.1)
X.to_csv('Slimmed Descriptors.csv',index=False)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
np.random.seed(100)
model=RandomForestRegressor(n_estimators=100)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
pickle.dump(model,open('Model.pkl','wb'))
