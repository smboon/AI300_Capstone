import joblib
import numpy as np
import pandas as pd 

class Model:
    def __init__(self):
        self.model = joblib.load('model/GBC_model.pkl')

    def predict(self, input_features):
        return self.model.predict([input_features])[0]

'''
    def predict(self, input_features):
        input_df = pd.DataFrame(input_features, columns=['tenure_months', 'total_monthly_fee',
                'age', 'contract_type',
                'total_charges_quarter', 'has_phone_service',
                'has_internet_service', 'has_premium_tech_support',
                'has_online_security', 'paperless_billing'])
        return self.model.predict(input_df) 
'''
    
# Add in this code chunk temporarily (delete it after this run)
"""
beneficiary_example = {
    "tenure_months": 5,
    "has_internet_service": 1,
    "has_phone_service": 0,
    "has_premium_tech_support": 0,
    "has_online_security": 0,
    "contract_type": 0,
    "paperless_billing": 0,
    "total_monthly_fee": 28.45,
    "total_charges_quarter": 131.05,
    "age": 77
}


beneficiary_example = {
"tenure_months":5, 
"contract_type":0
}



model_inputs = list(beneficiary_example.values())

print(model_inputs)                  
model_instance = Model()
prediction = model_instance.predict(beneficiary_example) 
print("Prediction:", prediction)

"""