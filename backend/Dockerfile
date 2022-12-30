FROM python:3.10.9-alpine3.17

RUN mkdir -p data.geojson

RUN mkdir -p data.geotiff

RUN python3 -m pip install fastapi uvicorn python-multipart

WORKDIR backend

COPY . .

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]