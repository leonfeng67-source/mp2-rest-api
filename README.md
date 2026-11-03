# MP2: REST API for Data Processing

This project is a FastAPI application for uploading, inspecting, and cleaning CSV datasets. It provides a health check endpoint, a CSV upload endpoint that stores datasets in memory and returns their metadata, a retrieval endpoint that returns stored rows with an optional limit, and a processing endpoint that validates and cleans a stored dataset using my MP1 data pipeline modules. Processing is controlled by a JSON configuration for required and numeric columns, duplicate removal, missing-value handling, and outlier removal, and it returns a cleaning report. A middleware logs every request with a unique request ID, status code, and duration, and adds the ID to the response headers. The API is tested with pytest and FastAPI's TestClient.

## Run

    python -m uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs.

## Test

    python -m pytest tests -v
