# Dependencies and Setup
import numpy as np
import pandas as pd
import math
import random, json
import sys


# Flask
from flask import Flask, render_template, jsonify, redirect, request, Response, json

# Import Scikit Learn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Import Pickle
import _pickle as pickle

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
#moojson = 0
# Test Route
@app.route("/")
def home(name=None):
    return render_template('index.html', name=name)

# Route for Generate JSONs
@app.route("/generate/<userdistance>", methods=["GET"])
def practice(userdistance):

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
    Range = ((velocity**2)*(np.sin(2*angle*3.14/180))/9.8)
    Distance = userdistance

    # Creating the DataFrame
    moo = pd.DataFrame({'Angle': angle,
                        'Velocity': velocity,
                        'Horizontal Velocity': horizontal_velocity,
                        'Vertical Velocity': vertical_velocity,
                        'Free Fall Time': free_fall_time,
                        'Total Time': total_time,
                        'Maximum Height': maximum_height,
                        'Range': Range,
                        "Distance": userdistance
                        },
                        columns=['Angle','Velocity','Horizontal Velocity','Vertical Velocity','Free Fall Time','Total Time','Maximum_Height','Range', "Distance"]
                        )

    # Force a 'pattern' in the results columns
    moo['Result'] = 0 #np.where((moo['Range']>= (jsdata + 20))&(moo['Range']<=(jsdata-20)),1,0)
    moojson = json.loads(moo.to_json(orient="records"))
 
    # Return only the jsonified version
    return jsonify(moojson)

#    # Sort Values
#    moo = moo.sort_values('Result', ascending=False)

# Route for Training JSONs
@app.route("/train", methods=['GET','POST'])
def train():

    print("I WAS HIT", file=sys.stderr)

    # AJAX Route that "post" data back
    if request.method == "POST":
     
     print("Post went through", file=sys.stderr)
     jsdata = request.get_json(force=True)
     # Convert array into DataFrame
     moopretrained = pd.DataFrame(jsdata)
     # print(moopretrained.head())


    print(jsdata)
    for x in jsdata:
        # print(x)

    # print("line", jsdata)
    # return jsonify(jsdata)

        # Convert array into DataFrame
        # and append new column "Results" with Successful, Angle, Velocity, and Range
        moopretrained["Result"] = moopretrained["Result"] = np.where( ( moopretrained["Range"] < (  moopretrained["Distance"].astype(str).astype(int) + 20  ) ) & ( moopretrained["Range"] > (  moopretrained["Distance"].astype(str).astype(int) - 20  ) ), 1, 0) 
        
        # Separate "Labels" and "Data"
        labels = moopretrained["Result"].values
        data = moopretrained[["Angle","Velocity","Range"]].values

        # Create a Logistic Model
        X_train, X_test, y_train, y_test = train_test_split(data, labels, random_state=1, stratify=labels)
    
        # Model for Logistic Regression
        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)
        classifier.score(X_train, y_train)
        classifier.score(X_test, y_test)

        # Score the Model
        train_score = classifier.score(X_train, y_train)
        test_score = classifier.score(X_test, y_test)

        # "Pickle"
        pickle.dump(classifier, open("Classifier.sav", 'wb'))

        # Return the Data
        return(str(train_score))

#     moo['Result'] = np.where((moo['Range']>= (jsdata + 20))&(moo['Range']<=(jsdata-20)),1,0)
#     return jsonify(moo['Result'])

#     # classifier.predict([65, 30])
#     # classifier.predict([[12121, 23], [65,30]])
#     # newSimulation = [[12121, 23], [65,30]]
#     # success_guesses = classifier.predict([[]])
#     # newSimulation
#     # success_guesses

#     # for num in success_guesses:
#     #     if (num == 1):
#     #         print(num)
#     #         print(newSimulation[num])

#     # for x in range(len(success_guesses)):
#     #     if(success_guesses[x] == 1):
#     #         print(success_guesses[x])
#     #         print(newSimulation[x])

# Route for Filtering JSONs
@app.route("/replay", methods=["GET","POST"])
def replay():

 # Generate New Data (replayData)
 # Store as an array called replayData
    angle = [random.randint(1, 90) for k in range(1000)]
    velocity = [random.randint(0, 100) for k in range(1000)]
    velocity =  np.array(velocity)
    angle = np.array(angle)
    gravity = 9.8
    horizontal_velocity = velocity * (np.cos(angle*math.pi)/180)
    vertical_velocity = velocity * (np.sin(angle*math.pi)/180)
    free_fall_time = (vertical_velocity/9.8)
    total_time = (2*free_fall_time)
    maximum_height = (2*vertical_velocity/(2*gravity))
    Range = ((velocity**2)*(np.sin(2*angle*3.14/180))/9.8)

    #Creating the Dataframe
    mooreplay = pd.DataFrame({'Angle': angle,
                              'Velocity': velocity,
                              'Horizontal Velocity': horizontal_velocity,
                              'Vertical Velocity': vertical_velocity,
                              'Free Fall Time': free_fall_time,
                              'Total Time': total_time,
                              'Maximum Height': maximum_height,
                              'Range1': Range,
                             },
                             columns=['Angle','Velocity','Horizontal Velocity','Vertical Velocity','Free Fall Time','Total Time','Maximum Height','Range1']
                             )

    print("ANOTHER TEST", file=sys.stderr)

    # Filtered List
    filteredData = []

    # Load the classifier
    classifier = pickle.load(open("Classifier.sav", 'rb'))
       

     # Separate only necessary values
    for index, row in mooreplay.iterrows():
        # print("Angle:", row["Angle"])
        # print("Velocity:", row["Velocity"])
        # print("Range1", row["Range1"])

        print(classifier.predict([row["Angle"], row["Velocity"], row["Range1"]]))

        if(classifier.predict([row["Angle"], row["Velocity"], row["Range1"]]) == 0):
                    
            filteredData.append(row)
            print(len(mooreplay))
            print(len(filteredData))

    print(filteredData, file=sys.stderr)
    # Display only filtered Data
    return(jsonify(filteredData))

@app.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    print("ANOTHER TEST", file=sys.stderr)

    if request.method == "POST":
        # print("Post went through")
        jsdata = request.get_json(force=True)
        print(jsdata)

        # for x in jsdata:
        #     print(x)

    # print("line", jsdata)
    return jsonify(jsdata)

#################################################
# Flask Boilerplate
#################################################
if __name__ == '__main__':
    app.run(debug=True)