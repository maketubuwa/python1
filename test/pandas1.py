#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-06 14:09:14
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import pandas
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
import numpy as np

titanic=pandas.read_csv("titanic.csv")

#设置成矩阵格式
titanic['Age']=titanic['Age'].fillna(titanic['Age'].median())
# print(titanic.describe())
#把str转换成能处理的数据格式
titanic.loc[titanic['Sex']=='male','Sex']=0
titanic.loc[titanic['Sex']=='female','Sex']=1

titanic.loc[titanic['Survived']==0,'Survived']=0
titanic.loc[titanic['Survived']==1,'Survived']=1
#print(titanic['Sex'].unique())
titanic['Embarked']=titanic['Embarked'].fillna('S')
titanic.loc[titanic['Embarked']=='S','Embarked']=0
titanic.loc[titanic['Embarked']=='C','Embarked']=1
titanic.loc[titanic['Embarked']=='Q','Embarked']=2
# print(titanic['Embarked'].unique())

# 线性回归
predictors = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']#
alg = LinearRegression()
#将数据分组 交叉验证
kf=KFold(titanic.shape[0],n_folds=3,random_state=1)
predictions=[]
for train,test in kf:
	train_predictors=(titanic[predictors].iloc[train,:])
	train_target=titanic["Survived"].iloc[train]
	alg.fit(train_predictors,train_target)
	test_predictions=alg.predict(titanic[predictors].iloc[test,:])
	predictions.append(test_predictions)

predictions=np.concatenate(predictions, axis=0)
# predictions[predictions>0.5]=1
# predictions[predictions<=0.5]=0
# accuracy=sum(predictions[predictions==titanic["Survived"]])/len(predictions)
# print(accuracy)
predictions_new = list(range(len(predictions)))
titanic_survived_list = list(titanic['Survived'])
summ = 0
for i in list(range(len(predictions))):
    if predictions[i] > 0.5:
        predictions_new[i] = 1
    else:
        predictions_new[i] = 0
    if predictions_new[i] == titanic_survived_list[i]:
        summ = summ+1
# print predictions_new

# print titanic['Survived']
accuracy = summ/float(len(predictions))
print(accuracy)


from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression#逻辑回归

alg=LogisticRegression(random_state=1)
scores=cross_validation.cross_val_predict(alg, titanic[predictors],titanic["Survived"],cv=3)
print(scores.mean())