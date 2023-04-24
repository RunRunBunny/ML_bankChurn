from locust import HttpUser, constant_pacing, task, between
import json

from userInfo import userInfo
class PretictChurn(HttpUser):
    host = "http://localhost:8000"
    wait_time = constant_pacing(1)
    
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

    @task
    def predict_bankChurn(self):
      # Make the request to the API
      response = self.client.post("/predict", json=user_info.dict())

      # Assert that the response is successful
      assert response.status_code == 200

      # Print the response content
      print(json.loads(response.content))

    wait_time = between(1, 5)