from fastapi.testclient import TestClient
from app import app
from userInfo import userInfo

client = TestClient(app)

def test_bankChurn():

    user_info = userInfo(
    creditscore=549,
    age=25,
    tenure=5,
    balance=0.0,
    numofproducts=2,
    estimatedsalary=190857.79,
    geography="France",
    gender_Male=False,
    hascrcard=False,
    isactivemember=False
    ) 

    #Act.
    response = client.post("/predict", json=user_info.dict())

    #Assert.
    assert response.status_code == 200
    assert response.json()['churn_prediction'] == False