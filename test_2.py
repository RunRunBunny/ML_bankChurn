from fastapi.testclient import TestClient
from app import app
from userInfo import userInfo

client = TestClient(app)

def test_bankChurn():

    user_info = userInfo(
    creditscore=600,
    age=35,
    tenure=5,
    balance=10000.0,
    numofproducts=2,
    estimatedsalary=50000.0,
    geography="Spain",
    gender_Male=True,
    hascrcard=True,
    isactivemember=False
    ) 

    #Act.
    response = client.post("/predict", json=user_info.dict())

    #Assert.
    assert response.status_code == 200
    # assert response.json() == {
    #     'prediction': 'Churn'
    # }