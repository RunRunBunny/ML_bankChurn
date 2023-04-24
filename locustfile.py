import json
from locust import HttpUser, task, between
from userInfo import userInfo

class PredictChurn(HttpUser):
    host = "http://localhost:8000"

    @task
    def predict_bankChurn(self):
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

        # Make the request to the API
        response = self.client.post("/predict", json=user_info.dict())

        # Print the response content
        print(response.content)
  
        # Assert that the response is successful
        assert response.status_code == 200

    wait_time = between(1, 5)
