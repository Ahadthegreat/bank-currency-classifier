# UTF-8 coding
# authentication downloaded dataset from Dataset Link: https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data 
from pydantic import BaseModel

class BankNote(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float
