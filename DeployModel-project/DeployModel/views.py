from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
import pickle
from matplotlib import scale
import pandas as pd
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request,"home.html")



@csrf_exempt
def result(request):
    #template = loader.get_template('result.html')
    pregnancies = request.POST.get('pregnancies')
    glucose = request.POST.get("glucose")
    bloodpressure = request.POST.get("bloodpressure")
    skinthickness = request.POST.get("skinthickness")
    insulin = request.POST.get("insulin")
    bmi = request.POST.get("bmi")
    DiabetesPedigreeFunction = request.POST.get("dpf")
    age = request.POST.get("age")

    diabetes_data = [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, DiabetesPedigreeFunction, age]]
    # for i in diabetes_data:
    #     print(i," ")
    diabetes_model = pickle.load(open('final_model.pkl', 'rb'))
    #diabetes_model = pd.read_pickle('r',"final_model.pkl")
    prediction = diabetes_model.predict(
        [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, DiabetesPedigreeFunction, age]])
    # outcome = prediction


    if prediction == 1:
        result = "You are Diabetic. Please visit a doctor for further assistance."
    elif prediction == 0:
        result = "HURRAY!! You are Not Diabetic"
    else:
        result = "Error!!!"


    return render(request,'result.html',{'result':result})



