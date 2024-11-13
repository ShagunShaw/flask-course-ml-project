'''NOTE:  From line 33 to 51, when retrieving our data from the website that the user has entered, make sure the variable
in which you are assigning the values for each parameter should be same as the column name in your dataset. For example,
in line number 34, the value of 1st parameter is airline which we are getting from our website. Now in the dataset, the 
parameter name is "Airline" and not "airline", so the variable in which we are assigning the value should be "Airline" only
and not anything else. In the "forms.py" page it doesn't matter whether you mentioned "Airline" or "airline" , but for the
"app.py" page, it should be same as the column name i.e. "Airline" '''


import pandas as pd
import joblib
from flask import Flask, url_for, render_template, redirect
from forms import InputForm

app= Flask(__name__, template_folder= "HTML Templates")
app.config['SECRET_KEY']= "This_is_your_CSRF_Token_Code"        # Generating our CSRF token here by giving it a random value
                          # because here we are woking with WTF forms and it won't work without passing the csrf token to it.
                          # Don't change the word 'SECRET_KEY' here.

model= joblib.load("model.joblib")                          

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
                Airline= [predict_form.airline.data],       # Getting the data given by the user

                Date_of_Journey= [predict_form.date_of_journey.data.strftime("%Y-%m-%d")],  
                # For this date part, we used the datetime object
                # of wtforms so our 'date_of_journey' would be of datetime object. But one thing to be noticed is that in 
                # the dataset that we are using, the 'date_of_journey' was an object (string datatype) before it was sent 
                # for pre-preocessing and then it was converted to data-time object using the pipeline. For our model 
                # prediction also we are using the same pipeline and so it requires the 'date_of_journey' to be initially of
                # object type and not date-time type. So we need to handle that too, that's why we are using "strftime()"

                Source= [predict_form.source.data],
                Destination= [predict_form.destination.data],
                Dep_Time= [predict_form.dep_time.data.strftime("%H:%M:%S")],    # Same logic here also
                Arrival_Time= [predict_form.arrival_time.data.strftime("%H:%M:%S")],        # Same logic here also
                Duration= [predict_form.duration.data],
                Total_Stops= [predict_form.total_stops.data],
                Additional_Info= [predict_form.additional_info.data]
        ))  
        print(x_new, type(x_new))
        prediction= model.predict(x_new)[0]     # '[0]' is an important step to note down, because 'predict' method returns a numpy array
        p_message= f"The predicted price for your flight is {prediction: ,.0f} INR"   # Understand the '{prediction:, .0f}' part from chatGPT

        return redirect(url_for('output', output_message= p_message))

    else:
        e_message= "Please provide valid input details!"

    return render_template("predict.html", title= "Predict", form= predict_form, output= e_message)

@app.route("/Predicted/<output_message>")
def output(output_message):
    return render_template("output.html", output= output_message)

if __name__== "__main__":
    app.run(debug= True)
