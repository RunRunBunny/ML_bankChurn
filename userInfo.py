# from pydantic import BaseModel
# Class which describes userInfo measurements
# class userInfo(BaseModel):
    # creditscore: int
    # age: int
    # tenure: int
    # balance: float
    # numofproducts: int
    # estimatedsalary: float
    # geography_Germany: int
    # geography_Spain: int
    # gender_Male: int
    # hascrcard: int
    # isactivemember: int
    # userInfo: dict

from pydantic import BaseModel, validator

class userInfo(BaseModel):
    creditscore: int
    age: int
    tenure: int
    balance: float
    numofproducts: int
    estimatedsalary: float
    geography: str
    gender_Male: bool
    hascrcard: bool
    isactivemember: bool
    
    # limit the creditscore
    @validator('creditscore')
    def check_creditscore(cls, value):
        if value < 200 or value > 800:
            raise ValueError('creditscore must be between 200 and 800')
        return value
    
    # limit positive
    @validator("age", "tenure", "balance", "numofproducts", "estimatedsalary", pre=True)
    def validate_positive(cls, value):
        if value < 0:
            raise ValueError("Value must be positive")
        return value
    
    # limit bool
    @validator('hascrcard', 'isactivemember', 'gender_Male')
    def check_booleans(cls, value):
        if not isinstance(value, bool):
            raise ValueError('must be a boolean value')
        return value
    
    # limit the geography
    @validator('geography')
    def check_geography(cls, value):
        allowed_values = ['Spain', 'Germany', 'France']
        if value not in allowed_values:
            raise ValueError(f'geography must be one of {", ".join(allowed_values)}')
        return value
