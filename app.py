from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import joblib

app = Flask(__name__)
app.secret_key = 'f3b9b2a7e1a6428c93b9c12c65fa46bd'  # Required for using sessions

model = joblib.load('model/model.pkl')

# 🔹 Route: Home (renders prediction if present in session)
@app.route('/')
def home():
    prediction = session.pop('prediction', None)  # Only shows once
    return render_template('index.html', prediction=prediction)

# 🔹 Route: Prediction logic + redirect
@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = [
            request.form['Pclass'],
            request.form['Sex'],
            request.form['Age'],
            request.form['Fare'],
            request.form['Embarked'],
            request.form['FamilySize'],
            request.form['IsAlone'],
            request.form['Title'],
            request.form['Deck']
        ]

        if any(val.strip() == '' for val in inputs):
            session['prediction'] = "⚠️ Please fill all fields before predicting."
            return redirect(url_for('home'))

        final_input = np.array([list(map(float, inputs))])
        result = model.predict(final_input)[0]
        session['prediction'] = int(result)  # ✅ Now it's JSON serializable

        return redirect(url_for('home'))

    except Exception as e:
        session['prediction'] = f"Error: {str(e)}"
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)