import pandas as pd  
import numpy as np 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv('BankNote_Authentication.csv')

# print(df.head(101))

#Independent features like y=m1x1^n+m2x2^u+m3x3^o
#Independent features are x1 x2 and x3
#Dependent feature are y

X=df.iloc[:,:-1]
y=df.iloc[:,-1]

# print(X)

# print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)


y_pred=classifier.predict(X_test)
score=accuracy_score(y_test,y_pred)
print(score)


pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()


print(classifier.predict([[-2,-3,-4,-1]]))