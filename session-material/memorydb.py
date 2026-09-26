from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel


app = FastAPI()

DATA_FILE = "patients.json"


# Root Endpoint
@app.get("/")
def home():
    return {"message": "Hello! This is root endpoint."}


# Util functions
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Data Validation
class Patient(BaseModel):
    name: str 
    city: str
    age: int
    gender: str
    height: float
    weight: float
    bmi: float
    verdict: str


# GET
@app.get("/view")
def view():
    return load_data()


# POST
@app.post("/add/{patient_id}")
def add(patient_id: str, patient: Patient):
    
    data = load_data()

    if patient_id in data:
        raise HTTPException(status_code=400, detail="Patient Already exists!")

    data[patient_id] = patient.model_dump()
    save_data(data)

    return "Patient Added Successfully."

# PUT: Update
@app.put("/update/{patient_id}")
def update(patient_id: str, patient: Patient):
    
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=400, detail="Patient Does Not Exist!")

    data[patient_id] = patient.model_dump()
    save_data(data)
    return "Patient Updated Successfully."


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=400, detail="The person you are looking for is on another planet.")

    del data[patient_id]
    save_data(data)
    return "Patient Removed from this Planet."