from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate_user_info', methods=['POST'])
def validate_user_info():
    try:
        # Get form data
        age = int(request.form['age'])
        gender = request.form['gender']
        ethnicity = request.form['ethnicity']
        parent_education = request.form['parent_education']
        study_time = int(request.form['study_time'])
        absences = int(request.form['absences'])
        tutoring = request.form['tutoring']
        parental_support = request.form['parental_support']
        extracurricular = request.form['extracurricular']
        sports = request.form['sports']
        music = request.form['music']
        volunteering = request.form['volunteering']

        # Perform additional validation if needed
        if age not in [15, 16, 17, 18]:
            raise ValueError("Invalid age")

        if age <= 0 or study_time < 0 or absences < 0:
            raise ValueError("Invalid input values")

        # Return success response
        return jsonify({'valid': True, 'message': 'Form submitted successfully!'})

    except (KeyError, ValueError) as e:
        return jsonify({'valid': False, 'message': 'Error: Invalid form data.'})
    

    # def predict(input_data): 
    # '''
    #     helper function for making prediction
    # '''
    # # create input DataFrame
    # input_df=pd.DataFrame([input_data])
    # # flask returns values in forms as strings by default
    # X=input_df[cont_cols].astype('float')
    # # use OHE on categorical variables
    # X_cat=ohe.transform(input_df[cat_cols])
    # # add categorical features to input data
    # X[cat_feature_names]=X_cat
    # # scale input data
    # X_transformed=scaler.transform(X)
    # # make prediction
    # output=model.predict(X_transformed)
    # # should only return first and only element
    # return output[0]

if __name__ == '__main__':
    app.run(debug=True)
