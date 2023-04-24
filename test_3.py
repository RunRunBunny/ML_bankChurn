from fastapi.testclient import TestClient
from app import app
from userInfo import userInfo

client = TestClient(app)

def test_bankChurn():

    user_info = userInfo(
    creditscore=376,
    age=29,
    tenure=4,
    balance=115046.74,
    numofproducts=4,
    estimatedsalary=119346.88,
    geography="Germany",
    gender_Male=False,
    hascrcard=True,
    isactivemember=False
    ) 

    #Act.
    response = client.post("/predict", json=user_info.dict())
    print(response.json()['churn_prediction'])

    #Assert.
    assert response.status_code == 200
    assert response.json()['churn_prediction'] == True