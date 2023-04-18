from fastapi.testclient import TestClient

from app import app, predict_bankChurn
from userInfo import userInfo

client = TestClient(app)

def test_input_data(mocker):
    data = {
        "creditscore": 0,
        "age": 0,
        "tenure": 0,
        "balance": 0.0,
        "numofproducts": 0,
        "estimatedsalary": 0.0,
        "geography_Germany": 0,
        "geography_Spain": 0,
        "gender_Male": 0,
        "hascrcard": 0,
        "isactivemember": 0
    }

    response = client.post("/predict", json = data)

    # assert response.status_code == 200
    # assert isinstance(response.json(), dict)
