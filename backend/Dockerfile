FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip3 install -r requirements.txt

ENV DATABASE_TYPE="prod"


EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]