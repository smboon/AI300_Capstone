from flask import Flask, request, render_template
from model import Model
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        form_input = request.form

        # Extract and preprocess form data
        tenure_months = int(form_input['tenure_months'])
        contract_type = int(form_input['contract_type'])
        total_monthly_fee = float(form_input['total_monthly_fee'])
        total_charges_quarter = float(form_input['total_charges_quarter'])
        age = int(form_input['age'])
        has_internet_service = form_input['has_internet_service'] == 'true'
        has_phone_service = form_input['has_phone_service'] == 'true'
        has_premium_tech_support = form_input['has_premium_tech_support'] == 'true'
        has_online_security = form_input['has_online_security'] == 'true'
        paperless_billing = form_input['paperless_billing'] == 'true'

        # Convert boolean values to integers (1 or 0)
        has_internet_service = 1 if has_internet_service else 0
        has_phone_service = 1 if has_phone_service else 0
        has_premium_tech_support = 1 if has_premium_tech_support else 0
        has_online_security = 1 if has_online_security else 0
        paperless_billing = 1 if paperless_billing else 0

        model_inputs = [tenure_months, total_monthly_fee, age, contract_type, total_charges_quarter, 
                        has_phone_service, has_internet_service, has_premium_tech_support,
                        has_online_security, paperless_billing]

        # Debug print statements
        print("Form input:", form_input)
        print("Model inputs:", model_inputs)


        # Ensure the model prediction returns a single value
        # prediction = model.predict([model_inputs])[0]
        prediction = Model().predict(model_inputs) 

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
