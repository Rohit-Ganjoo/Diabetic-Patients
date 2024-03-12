from django.shortcuts import render
from .ml_model import train_model, predict_diabetes

def home(request):
    return render(request, 'C:/Users/zeus/Desktop/MeriSKILL/Project 2 Diabetic Patients/diabetes_project/diabetes_app/templates/home.html')

def predict(request):
    return render(request, 'C:/Users/zeus/Desktop/MeriSKILL/Project 2 Diabetic Patients/diabetes_project/diabetes_app/templates/predict.html')

def result(request):
    model = train_model()

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    prediction = predict_diabetes(model, [val1, val2, val3, val4, val5, val6, val7, val8])

    result1 = "Positive" if prediction == 1 else "Negative"

    return render(request, template_name="predict.html", context={"result2": result1})
