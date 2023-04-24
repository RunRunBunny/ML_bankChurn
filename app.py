# 1. Library imports
import uvicorn
from fastapi import FastAPI
from userInfo import userInfo
from churnPred import churnPred
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
#    JSON data and return the predicted Bank Churn with the confidence
@app.post('/predict', response_model= churnPred)
def predict_bankChurn(data:userInfo):
    data = data.dict()
    # data = data.userInfo
    data['NewAGT'] = data['age'] - data['tenure']
    data['geography_Germany'] = (data['geography'] == "Germany")
    data['geography_Spain'] = (data['geography'] == "Spain")
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

    probability = model.predict_proba(X)[:, 1]
    
    if(probability > 0.5):
        return churnPred(churn_prediction=True, churn_probability=probability, explanation="High risk of churn.")
    else:
        return churnPred(churn_prediction=False, churn_probability=probability, explanation="Low risk of churn.")

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload