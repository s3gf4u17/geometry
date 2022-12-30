from fastapi import FastAPI, UploadFile
import os, json

app = FastAPI()

# connection test endpoint
@app.get("/")
async def root():
    return {"status":"ok"}

### GEOJSON
# get available layers
@app.get("/geojson/")
async def root():
    files = []
    for file,_,_ in os.walk("data.geojson"):
        files.append(file)
    return {"files":files}

### GEOJSON
#save new layer
@app.post("/geojson/")
async def root(file: UploadFile):
    with open("data.geojson/"+file.filename,"wb") as f:
        f.write(file.file.read())
    return {"status":"ok"}

### GEOJSON
# read existing layer
@app.get("/geojson/{filename}")
async def root(filename: str):
    with open("data.geojson/"+filename,"rb") as f:
        geojson = json.loads(f.read())
    return {"file":geojson}

### GEOTIFF
# get available layers
@app.get("/geotiff/")
async def root():
    files = []
    for file,_,_ in os.walk("data.geotiff"):
        files.append(file)
    return {"files":files}

### GEOTIFF
#save new layer
@app.post("/geotiff/")
async def root(file: UploadFile):
    with open("data.geotiff/"+file.filename,"wb") as f:
        f.write(file.file.read())
    return {"status":"ok"}

### GEOTIFF
# read existing layer
@app.get("/geotiff/{filename}")
async def root(filename: str):
    with open("data.geotiff/"+filename,"rb") as f:
        geotiff = json.loads(f.read())
    return {"file":geotiff}