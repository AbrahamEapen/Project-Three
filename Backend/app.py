# Dependencies and Setup
import sqlite3
import datetime as dt
import numpy as np
import pandas as pd
import math

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify, redirect

# Import Scikit Learn
from sklearn.linear_model import LogisticRegression

# Import Pickle
import _pickle as pickle


#################################################
# Database Setup
#################################################
 engine = create_engine("sqlite:///titanic.sqlite")

 # reflect an existing database into a new model
 Base = automap_base()
 # reflect the tables
 Base.prepare(engine, reflect=True)

 # Save reference to the table
 Passenger = Base.classes.passenger

 # Create our session (link) from Python to the DB
 session = Session(engine)

#################################################
# Flask Setup
#################################################
# app = Flask(__name__)
#################################################
# Flask Routes
#################################################

# Test Route
@app.route("/")
def home(): 
    return ("Hi!")

# Route for Receiving JSONs
@app.route("/practice", methods=["GET", "POST"])
def practice():

    # Initial Data 
    angle = [random.randint(1, 90) for k in range(1000)]
    velocity = [random.randint(0, 100) for k in range(1000)]
    velocity = np.array(velocity)
    angle = np.array(angle)
    gravity = 9.8
    horizontal_velocity = velocity * (np.cos(angle*math.pi)/180)
    vertical_velocity = velocity * (np.sin(angle*math.pi)/180)
    free_fall_time = (vertical_velocity/9.8)
    total_time = (2*free_fall_time)
    maximum_height = (2*vertical_velocity/(2*gravity))
    Range = (horizontal_velocity*total_time)

    Range = ((velocity**2)*(np.sin(2*angle/180))/9.8)
    print(Range)

    Range = ((velocity**2)*(np.sin(2*angle*3.14/180))/9.8)
    print(Range)

    # Creating the DataFrame
    moo = pd.DataFrame({'Angle': angle,
                        'Velocity': velocity,
                        'Horizontal Velocity': horizontal_velocity,
                        'Vertical Velocity': vertical_velocity,
                        'Free Fall Time': free_fall_time,
                        'Total Time': total_time,
                        'Maximum_Height': maximum_height,
                        'Range': Range
                        },
                        columns=['Angle','Velocity','Free Fall Time',]
                        )
    
    #Force a 'pattern' in the results columns
    moo['Result'] = np.where((moo['Range']>= 300] & (moo['Range']<=310)1,0))
    moo.to_json('json.json', orient='records')

    # Sort Values
    moo = moo.sort_values('Result', ascending=False)
    


    # Separate "Labels" and "Data"
    labels = practiceDF["Success_Failure"].values
    data = practiceDF[["Angle", "Velocity"]].values

    # Create a Logistic Model 
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data, labels, #random_state=1, stratify=labels)

    # Model for LogistiRegression
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    classifier.score(X_train, y_train)
    classifier.score(X_test, y_test)

    classifier.predict([65, 30])
    classifier.predict([[12121, 23], [65,30]])
    newSimulation = [[12121, 23], [65,30]]
    success_guesses = classifier.predict([[]])
    newSimulation
    success_guesses
    for num n success_guesses:
       if (num == 1):
           print(num)
           print(newSimulation[num])

    for x in range(len(success_guesses)):
       if(success_guesses[x] == 1):
           print(success_guesses[x])
           print(newSimulation[x])

    # Score the Model
    train_score = classifier.score(X_train, y_train)
    test_score = classifier.score(X_test, y_test)

    # Pickle 
    pickle.dump(classifier, open("Classifier.sav", 'wb'))

    # Return the Data
    return(str(train_score))


# Route for Filtering JSONs
@app.route("/replay", methods=["GET", "POST"])
def replay(): 

    # Replay Data

    # Filtered List 
    filteredData = []

    # Reload the classifier
    classifier = pickle.load(open("Classifier.sav", 'rb'))

    # Filter it down using the Classifier
    for x in range(len(replayData)):

        print(replayData[x])
        if(classifier.predict([replayData[x]["Angle"], replayData[x]["Velocity"]]) == 1):
            filteredData.append(replayData[x])

    print(len(replayData))
    print(len(filteredData))

    # Display only filtered Data
    return(jsonify(filteredData))

#################################################
# Flask Boilerplate
#################################################
if __name__ == '__main__':
    app.run(debug=True)