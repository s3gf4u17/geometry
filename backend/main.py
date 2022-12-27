from fastapi import FastAPI
import subprocess as sub

sub.run(["mkdir","-p","data.geotiff"])
sub.run(["mkdir","-p","data.geojson"])

app = FastAPI()

@app.get("/")
async def root():
    content = None
    with open("data.geojson/test.txt","w") as f:
        f.write("test")
    with open("data.geojson/test.txt","r") as f:
        content = f.read()
    return {"status":content}