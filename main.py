from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import subprocess as sub
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sub.run(["sudo","mkdir","-p","/var/www/html/data.geojson"])
sub.run(["sudo","mkdir","-p","/var/www/html/data.geotiff"])

@app.get("/geotiff/")
async def root():
    for _,_,files in os.walk("/var/www/html/data.geotiff/"):
        return {"layers":files}

@app.get("/geojson/")
async def root():
    for _,_,files in os.walk("/var/www/html/data.geojson/"):
        return {"layers":files}

@app.post("/geojson/")
async def root(file: UploadFile):
    filepath = f'/var/www/html/data.geojson/{file.filename}'
    filecontent = f'{file.file.read().decode()}'
    with open("temp.txt","w") as f: f.write(filecontent)
    sub.run(["sudo","mv","temp.txt",filepath])
    sub.run(["sudo","rm","-rf","temp.txt"])
    return {"status":"success"}

@app.post("/geotiff/")
async def root(file: UploadFile):
    filepath = f'/var/www/html/data.geotiff/{file.filename}'
    filecontent = file.file.read()
    with open("temp.txt","wb") as f: f.write(filecontent)
    sub.run(["sudo","mv","temp.txt",filepath])
    sub.run(["sudo","rm","-rf","temp.txt"])
    return {"status":"success"}