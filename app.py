from fastapi import FastAPI
import uvicorn
import sys 
import os 
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
  return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
  try:
    os.system("python main.py")
    return Response("Success!!", status_code=200)
  except Exception as e:
    return Response(str(e), status_code=500)
  
@app.get("/predict")
async def predict(text):
  try:
    output = PredictionPipeline().predict(text)
    return Response(output, status_code=200)
  except Exception as e:
      return Response(str(e), status_code=500)
  
uvicorn.run(
  app, 
  host= "0.0.0.0",
  port=8080
)
