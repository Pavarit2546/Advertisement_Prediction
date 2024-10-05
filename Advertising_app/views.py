from django.shortcuts import render
import pickle
import numpy 
import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load
import sklearn
from sklearn.preprocessing import PolynomialFeatures


#Load your model here
model_poly = load('model_Poly.pickle')
model_muti = load('model_Multi.pickle')

# Create your views here.
def Polynomial(request):

    if request.method == 'POST':
        try:
            Tv = float(request.POST['Tv'])
            Radio = float(request.POST['Radio'])
            Newspaper = float(request.POST['Newspaper'])
            
            data = {
                'TV': [Tv],
                'Radio': [Radio],
                'Newspaper': [Newspaper],
            }
            df_input = pd.DataFrame(data)
            df = pd.read_csv('advertising_Cleaned.csv')

            X = df[['TV', 'Radio', 'Newspaper']]
            y = df['Sales']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=346)
            
            #test_df = pd.concat([X_test, y_test], axis=1)
            train_df = pd.concat([X_train, y_train], axis=1)
            poly = PolynomialFeatures(degree=2)
            poly.fit_transform(X_train)
            df_trans = poly.transform(df_input)
            prediction = model_poly.predict(df_trans)
            #test_df.to_csv('Test_data.csv', index=False)
            train_df.to_csv('Train_data.csv', index=False)
            context = {
                'result': f"Predicted sales: {prediction[0]:.2f} thousands"
            }
            return render(request, "Poly_index.html", context)
        
        except (ValueError, KeyError) as e:
            context = {
                'result': "An error has occurred: " + str(e)
            }
            return render(request, "Poly_index.html", context)
 
    return render(request, "Poly_index.html")

def Multiple_Linear(request):

    if request.method == 'POST':
        try:
            Tv = float(request.POST['Tv'])
            Radio = float(request.POST['Radio'])
            Newspaper = float(request.POST['Newspaper'])
            
            data = {
                'TV': [Tv],
                'Radio': [Radio],
                'Newspaper': [Newspaper],
            }
            df_input = pd.DataFrame(data)
            
            prediction = model_muti.predict(df_input)

            context = {
                'result': f"Predicted sales: {prediction[0]:.2f} thousands"
            }
            return render(request, "Multi_index.html", context)
        
        except (ValueError, KeyError) as e:
            context = {
                'result': "An error has occurred: " + str(e)
            }
            return render(request, "Multi_index.html", context)
 
    return render(request, "Multi_index.html")

def homepage(request):
    return render(request, 'home.html')