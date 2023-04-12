from pydantic import BaseModel
# Class which describes userInfo measurements
class userInfo(BaseModel):
    creditscore: int
    age: int
    tenure: int
    balance: float
    numofproducts: int
    estimatedsalary: float
    geography_Germany: int
    geography_Spain: int
    gender_Male: int
    hascrcard: int
    isactivemember: int