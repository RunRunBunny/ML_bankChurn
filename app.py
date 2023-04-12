# 1. Library imports
import uvicorn
from fastapi import FastAPI
from userInfo import userInfo
import numpy as np
import joblib
import pandas as pd
# 2. Create the app object
app = FastAPI()
model = joblib.load("./bankChurn.model")
scaler = joblib.load('scaler.bin')

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To BankChurn Prediction System': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:userInfo):
    data = data.dict()
    data['NewAGT'] = data['age'] - data['tenure']
    # data['CreditsScore'] = pd.qcut(data['creditscore'], 10, labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # data['AgeScore'] = pd.qcut(data['age'], 8, labels = [1, 2, 3, 4, 5, 6, 7, 8])
    # data['BalanceScore'] = pd.qcut(data['balance'].rank(method="first"), 10, labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # data['EstSalaryScore'] = pd.qcut(data['estimatedsalary'], 10, labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # data["NewEstimatedSalary"] = data['estimatedsalary'] / 12 
    cat_variables = ["geography_Germany", "geography_Spain", "gender_Male", "hascrcard","isactivemember"]
    con_variables = ['creditscore', 'age', 'tenure', 'balance', 'numofproducts', 'estimatedsalary',	'NewAGT']
    cat_dict = {}
    con_dict = {}
    for i in cat_variables:
        cat_dict[i] = data[i]
    for i in con_variables:
        con_dict[i] = data[i]
    con_df = scaler.transform(pd.DataFrame(con_dict, index = [1], columns= con_variables))
    con_df = pd.DataFrame(con_df, columns = con_variables, index = [1])
    cat_df = pd.DataFrame(cat_dict, index = [1])
    X = pd.concat([con_df,cat_df], axis = 1)

    prediction = model.predict(X)
    
    if(prediction == 1):
        prediction = 'Churn'
    else:
        prediction = 'Not Churn'
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload