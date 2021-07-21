from get_model import LoadModel
from flask import Flask, render_template, flash, request
from get_model import *

# Flask web.
 
#initializing the model
MODEL_PATH = "../models/logistic_reg.sav"
model = LoadModel(MODEL_PATH)

# 'pregnant','glucose','bp','insulin','pedigree','age'

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#Define home route
@app.route("/")
def index():
    return render_template("index.html")

#Define diagnosis route
@app.route("/diagnosis", methods=['POST'])
def diagnosis():
    pregnant = request.form['pregnant']
    glucose = request.form['glucose']
    bp = request.form['bp']
    name = request.form['name']
    age = request.form['age']
    insulin = request.form['insulin']
    pedigree = request.form['pedigree']
 
    #Predict on the given parameters
    prediction = model.predict_class(pregnant,glucose,bp,insulin,pedigree,age)
    print(prediction)
    #Route for result
    if prediction[0] == '1':
        return render_template("positive.html", result="true")
    elif prediction[0] == '0':
        return render_template("negetive.html", result="true")
        
if __name__ == "__main__":
    app.run()