from fastapi.testclient import TestClient
from app import app, predict_bankChurn
import userInfo

client = TestClient(app)

def test_bankChurn():
    #Arrange. 
    request_body = {"userInfo": {
        "creditscore": 0,
        "age": 20,
        "tenure": 0,
        "balance": 0.0,
        "numofproducts": 0,
        "estimatedsalary": 0.0,
        "geography_Germany": 0,
        "geography_Spain": 0,
        "gender_Male": 0,
        "hascrcard": 0,
        "isactivemember": 0
    }}

    #Act.
    response = client.post("/predict", json=request_body)

    #Assert.
    assert response.status_code == 200
    assert response.json() == {
        'prediction': 'Not Churn'
    }