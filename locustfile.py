from locust import HttpUser, constant_pacing, task, between
import json

from userInfo import userInfo
class PretictChurn(HttpUser):
    host = "http://localhost:8000"
    wait_time = constant_pacing(1)
    

    @task
    def predict_bankChurn(self):
      # Make the request to the API
      response = self.client.post("/predict", json={"userInfo":{
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
      }})

      # Assert that the response is successful
      assert response.status_code == 200

        # Print the response content
      print(json.loads(response.content))

      wait_time = between(1, 5)