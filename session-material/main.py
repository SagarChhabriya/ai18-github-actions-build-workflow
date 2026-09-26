from fastapi import FastAPI
import pickle
import sklearn
from pydantic import BaseModel, Field


app = FastAPI()

# Load Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


class SalaryRequest(BaseModel):
    experience_years: float = Field(ge=0, le=10)

@app.get("/")
def home():
    return {"message": "Hello from ML APP root endpoint!"}



@app.post("/predict")
def predict(request: SalaryRequest):

    prediction = model.predict([[request.experience_years]])

    return {"predicted_salary": prediction[0]}