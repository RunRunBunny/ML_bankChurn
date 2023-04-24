from fastapi.testclient import TestClient
from app import app
from userInfo import userInfo

client = TestClient(app)

def test_bankChurn():

    user_info = userInfo(
    creditscore=619,
    age=42,
    tenure=2,
    balance=0.0,
    numofproducts=1,
    estimatedsalary=101348.88,
    geography="France",
    gender_Male=False,
    hascrcard=True,
    isactivemember=True
    ) 

    #Act.
    response = client.post("/predict", json=user_info.dict())

    #Assert.
    assert response.status_code == 200
    assert response.json()['churn_prediction'] == False