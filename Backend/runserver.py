from fastapi import FastAPI
import uvicorn
from db.database import engine, Base
from dotenv import load_dotenv
from controller.prediction import predict_phenotype

app = FastAPI()

app.title = "Biotecnología API"
app.description = "API para predecir características fenotípicas a partir de ADN"
app.version = "0.1.0"

origins =[
    "*"
]

# Creación de la base de datos
Base.metadata.create_all(bind=engine)


@app.get("/status")
async def read_root():
    return {"message": "Backend Is Running"}    

@app.post("/predict")
async def predict_dna_sequence(sequence: str):
    prediction = predict_phenotype(sequence)
    return {"sequence": sequence, "prediction": prediction}

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
