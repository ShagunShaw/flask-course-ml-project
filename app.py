import pandas as pd
import joblib
from flask import Flask, url_for, render_template
from forms import InputForm

app= Flask(__name__, template_folder= "HTML Templates")
app.config['SECRET_KEY']= "This_is_your_CSRF_Token_Code"        # Generating our CSRF token here by giving it a random value
                          # because here we are woking with WTF forms and it won't work without passing the csrf token to it.
                          # Don't change the word 'SECRET_KEY' here.

model= joblib.load("E:/Development Docs/Web Development (Using Flask)/Flask Tutorial/Part 8 (ML Project)/model.joblib")                          

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title= "Home")

@app.route("/predict", methods= ["GET", "POST"])
def predict():
    predict_form= InputForm()
    if predict_form.validate_on_submit():    # Under this part, after the user clicks on predict and if all of the required
        # conditions for the inputs are satisfied, then we will perform some operation on the data we got and then send it
        # to our model for prediction.
        
        x_new= pd.DataFrame(dict(   # Converting all our inputs to pandas dataframe (as our model expects a pd dataframe for making predictions)
                airline= [predict_form.airline.data],       # Getting the data given by the user

                date_of_journey= [predict_form.date_of_journey.data.strftime("%Y-%m-%d")],  
                # For this date part, we used the datetime object
                # of wtforms so our 'date_of_journey' would be of datetime object. But one thing to be noticed is that in 
                # the dataset that we are using, the 'date_of_journey' was an object (string datatype) before it was sent 
                # for pre-preocessing and then it was converted to data-time object using the pipeline. For our model 
                # prediction also we are using the same pipeline and so it requires the 'date_of_journey' to be initially of
                # object type and not date-time type. So we need to handle that too, that's why we are using "strftime()"

                source= [predict_form.source.data],
                destination= [predict_form.destination.data],
                dep_time= [predict_form.dep_time.data.strftime("%H:%M:%S")],    # Same logic here also
                arrival_time= [predict_form.arrival_time.data.strftime("%H:%M:%S")],        # Same logic here also
                duration= [predict_form.duration.data],
                total_stops= [predict_form.total_stops.data],
                additional_info= [predict_form.additional_info.data]
        ))  

        prediction= model.predict(x_new)[0]     # '[0]' is an important step to note down, because 'predict' method returns a numpy array
        message= f"The predicted price for your flight is {prediction: ,.0f} INR"   # Understand the '{prediction:, .0f}' part from chatGPT
    
    else:
        message= "Please provide valid input details!"

    return render_template("predict.html", title= "Predict", form= predict_form, output= message)

if __name__== "__main__":
    app.run(debug= True)