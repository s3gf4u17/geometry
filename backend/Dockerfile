FROM python:3.10.9-alpine3.17

WORKDIR /backend

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload"]