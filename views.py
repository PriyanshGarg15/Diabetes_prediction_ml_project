import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from django.shortcuts import render
def home(request):
  return render(request,"home.html")

def predict(request):
  return render(request,"predict.html")

def result(request):
  data = pd.read_csv('./diabetes.csv')
  X = data.drop("Outcome" , axis=1)
  Y = data["Outcome"]

  X_train ,X_test, Y_train , Y_test = train_test_split(X,Y, test_size =0.2)
  model = LogisticRegression()
  model.fit(X_train,Y_train)
  val1=float(request.GET('pregnancies'))
  val2=float(request.GET('Glucose'))
  val3=float(request.GET('Blood-Pressure'))
  val4=float(request.GET('Skin-Thickness'))
  val5=float(request.GET('Insulin'))
  val6=float(request.GET('BMI'))
  val7=float(request.GET('Diabetes-Pedigree-Function'))
  val8=float(request.GET('Age'))
  result=""
  predictions = model.predict([val1,val2,val3,val4,val5,val6,val7,val8])
  if(predictions==1):
    result="Positive"
  else:
    result="Negative"
  print(result)
  return render(request,"home.html",{"result1":result})
