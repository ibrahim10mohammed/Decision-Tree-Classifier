import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

train_set = pd.read_csv('train.csv')
test_set = pd.read_csv('test.csv')

train_set['Sex'] = train_set['Sex'].map( {'female': 1, 'male': 0} ).astype(int)
test_set['Sex'] = test_set['Sex'].map( {'female': 1, 'male': 0} ).astype(int)

guess_ages = np.zeros((2,3))
for i in range(0, 2):
    for j in range(0, 3):
        guess_df = train_set[(train_set['Sex'] == i) &(train_set
                                ['Pclass']== j+1)]['Age'].dropna()         
        age_guess = guess_df.median()
        
        guess_ages[i,j] = float (age_guess)

for i in range(0, 2):
    for j in range(0, 3):
        train_set.loc[ (train_set.Age.isnull()) & (train_set
                         .Sex == i) & (train_set.Pclass == j+1),'Age'] = guess_ages[i,j]

train_set.loc[train_set['Age'] <= 10,'Age' ] =1
train_set.loc[(train_set['Age'] <= 20 )& (train_set['Age'] > 10),'Age' ] =2       
train_set.loc[(train_set['Age'] <= 30 )& (train_set['Age'] > 20),'Age' ] =3 
train_set.loc[(train_set['Age'] <= 40 )& (train_set['Age'] > 30),'Age' ] =4 
train_set.loc[(train_set['Age'] <= 50 )& (train_set['Age'] > 40),'Age' ] =5 
train_set.loc[(train_set['Age'] <= 60 )& (train_set['Age'] > 50),'Age' ] =6 
train_set.loc[(train_set['Age'] <= 70 )& (train_set['Age'] > 60),'Age' ] =7
train_set.loc[(train_set['Age'] <= 80 )& (train_set['Age'] > 70),'Age' ] =8
guess_ages = np.zeros((2,3))
for i in range(0, 2):
    for j in range(0, 3):
        guess_df = test_set[(test_set['Sex'] == i) &(test_set
                                ['Pclass']== j+1)]['Age'].dropna()         
        age_guess = guess_df.median()
        
        guess_ages[i,j] = float (age_guess)
for i in range(0, 2):
    for j in range(0, 3):
        test_set.loc[ (test_set.Age.isnull()) & (test_set
                         .Sex == i) & (test_set.Pclass == j+1),'Age'] = guess_ages[i,j]
test_set.loc[test_set['Age'] <= 10 ,'Age' ] =1
test_set.loc[ (test_set['Age'] <= 20)& (test_set['Age'] > 10) ,'Age' ] =2
test_set.loc[ (test_set['Age'] <= 30 )& (test_set['Age'] > 20),'Age' ] =3
test_set.loc[ (test_set['Age'] <= 40 )& (test_set['Age'] > 30),'Age' ] =4
test_set.loc[ (test_set['Age'] <= 50 )& (test_set['Age'] > 40),'Age' ] =5
test_set.loc[ (test_set['Age'] <= 60 )& (test_set['Age'] > 50),'Age' ] =6
test_set.loc[ (test_set['Age'] <= 70 )& (test_set['Age'] > 60),'Age' ] =7
test_set.loc[ (test_set['Age'] <= 80 )& (test_set['Age'] > 70),'Age' ] =8    


guess_fares = np.zeros((2,3))
for i in range(0, 2):
    for j in range(0, 3):
        guess_df = train_set[(train_set['Sex'] == i) &(train_set
                                ['Pclass']== j+1)]['Fare'].dropna()         
        Fares_guess = guess_df.median()
        
        guess_fares[i,j] = float (Fares_guess)

for i in range(0, 2):
    for j in range(0, 3):
        train_set.loc[ (train_set.Fare.isnull()) & (train_set
                         .Sex == i) & (train_set.Pclass == j+1),'Fare'] = guess_fares[i,j]

train_set.loc[train_set['Fare'] <= 50 ,'Fare'] = 1   
train_set.loc[ (train_set['Fare'] > 50)& (train_set['Fare'] <= 100) ,'Fare' ] =2
train_set.loc[ (train_set['Fare'] > 100)& (train_set['Fare'] <= 150) ,'Fare' ] =3
train_set.loc[ (train_set['Fare'] > 150)& (train_set['Fare'] <= 200) ,'Fare' ] =4    
train_set.loc[ (train_set['Fare'] > 200)& (train_set['Fare'] <= 250) ,'Fare' ] =5
train_set.loc[ (train_set['Fare'] > 250)& (train_set['Fare'] <= 300) ,'Fare' ] =6
train_set.loc[ (train_set['Fare'] > 300)& (train_set['Fare'] <= 350) ,'Fare' ] =7
train_set.loc[ (train_set['Fare'] > 350)& (train_set['Fare'] <= 400) ,'Fare' ] =8
train_set.loc[ (train_set['Fare'] > 400)& (train_set['Fare'] <= 450) ,'Fare' ] =9
train_set.loc[ (train_set['Fare'] > 450)& (train_set['Fare'] <= 513) ,'Fare' ] =10    
guess_fares = np.zeros((2,3))
for i in range(0, 2):
    for j in range(0, 3):
        guess_df = test_set[(test_set['Sex'] == i) &(test_set
                                ['Pclass']== j+1)]['Fare'].dropna()         
        Fares_guess = guess_df.median()
        
        guess_fares[i,j] = float (Fares_guess)

for i in range(0, 2):
    for j in range(0, 3):
        test_set.loc[ (test_set.Fare.isnull()) & (test_set
                         .Sex == i) & (test_set.Pclass == j+1),'Fare'] = guess_fares[i,j]

test_set.loc[test_set['Fare'] <= 50 ,'Fare'] = 1   
test_set.loc[ (test_set['Fare'] > 50)& (test_set['Fare'] <= 100) ,'Fare' ] =2
test_set.loc[ (test_set['Fare'] > 100)& (test_set['Fare'] <= 150) ,'Fare' ] =3
test_set.loc[ (test_set['Fare'] > 150)& (test_set['Fare'] <= 200) ,'Fare' ] =4    
test_set.loc[ (test_set['Fare'] > 200)& (test_set['Fare'] <= 250) ,'Fare' ] =5
test_set.loc[ (test_set['Fare'] > 250)& (test_set['Fare'] <= 300) ,'Fare' ] =6
test_set.loc[ (test_set['Fare'] > 300)& (test_set['Fare'] <= 350) ,'Fare' ] =7
test_set.loc[ (test_set['Fare'] > 350)& (test_set['Fare'] <= 400) ,'Fare' ] =8
test_set.loc[ (test_set['Fare'] > 400)& (test_set['Fare'] <= 450) ,'Fare' ] =9
test_set.loc[ (test_set['Fare'] > 450)& (test_set['Fare'] <= 513) ,'Fare' ] =10    
freq_Embarked=train_set.Embarked.dropna().mode()
train_set['Embarked'] = train_set['Embarked'].fillna(freq_Embarked[0])
train_set['Embarked'] = train_set['Embarked'].map( {'S': 1, 'C': 2, 'Q': 3}).astype(int)

freq_Embarked=test_set.Embarked.dropna().mode()
test_set['Embarked'] = test_set['Embarked'].fillna(freq_Embarked[0])
test_set['Embarked'] = test_set['Embarked'].map( {'S': 1, 'C': 2, 'Q': 3}).astype(int)

train_x = train_set.drop(['PassengerId','Survived','Cabin','Name','Ticket'],axis=1)
train_y= train_set['Survived']

test_x = test_set.drop(['PassengerId','Cabin','Name','Ticket'],axis=1)
estimator = DecisionTreeClassifier(max_leaf_nodes=7, random_state=0)
estimator.fit(train_x, train_y)
y_pred = estimator.predict(test_x)