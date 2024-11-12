from flask_wtf import FlaskForm
import pandas as pd
from wtforms import SelectField, DateField, TimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired


# Getting the data
train= pd.read_csv("E:/Development Docs/Web Development (Using Flask)/Flask Tutorial/Part 8 (ML Project)/Data/training_data.csv")
val= pd.read_csv("E:/Development Docs/Web Development (Using Flask)/Flask Tutorial/Part 8 (ML Project)/Data/validation_data.csv")
x_data= pd.concat([train, val], axis=0)
x_data= x_data.drop(['Price'], axis=1)


class InputForm(FlaskForm):
    airline= SelectField(
        label= "Airline",
        choices= x_data['Airline'].unique().tolist(),        # 'x_data['Airline'].unique()' will return
                        # a numpy array and by doing '.tolist()' we are converting it to a python list
        validators= [DataRequired()]                
    )

    date_of_journey= DateField(
        label= "Date of Journey",
        validators= [DataRequired()]
    )

    source= SelectField(
        label= "Source",
        choices= x_data['Source'].unique().tolist(),
        validators= [DataRequired()]
    )

    destination= SelectField(
        label= "Destination",
        choices= x_data['Destination'].unique().tolist(),
        validators= [DataRequired()]
    )

    dep_time= TimeField(
        label= "Departure Time",
        validators= [DataRequired()]
    )

    arrival_time= TimeField(
        label= "Arrival Time",
        validators= [DataRequired()]
    )

    duration= IntegerField(
        label= "Duration of Flight (in minutes)",
        validators= [DataRequired()]
    )

    total_stops= IntegerField(
        label= "Total Number of Stops",
        validators= [DataRequired()]
    )

    additional_info= SelectField(
        label= "Additional Information",
        choices= x_data['Additional_Info'].unique().tolist(),
        validators= [DataRequired()]
    )

    predict= SubmitField(label= "Predict")