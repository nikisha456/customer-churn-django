
# Create your views here.
from django.shortcuts import render
import joblib

# Load model (correct path)
model = joblib.load('../model.pkl')

def home(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        purchase = float(request.POST['purchase'])
        manager = int(request.POST['manager'])
        years = float(request.POST['years'])
        sites = int(request.POST['sites'])

        prediction = model.predict([[age, purchase, manager, years, sites]])

        if prediction[0] == 1:
            result = "Customer will CHURN ❌"
        else:
            result = "Customer will STAY ✅"

        return render(request, 'index.html', {'result': result})

    return render(request, 'index.html')
