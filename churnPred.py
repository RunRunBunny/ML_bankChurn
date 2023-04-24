from pydantic import BaseModel, validator

class churnPred(BaseModel):
    churn_prediction: bool
    churn_probability: float
    explanation: str

    # limit the prediction
    @validator('churn_probability')
    def check_churn_probability(cls, value):
        if value < 0 or value > 1:
            raise ValueError('probability must be between 0 and 1')
        return value
    
    # limit bool
    @validator('churn_prediction')
    def check_booleans(cls, value):
        if not isinstance(value, bool):
            raise ValueError('must be a boolean value')
        return value