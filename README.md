# Tractian Challenge API - Asset Management

This API is part of the Tractian Challenge, designed to manage assets, locations, and companies. It provides endpoints for retrieving information about companies, locations within companies, and assets related to these companies. The API uses Swagger for automatic documentation, making it easy to understand and interact with the available endpoints.

---

## Features

- **Retrieve Companies**: Get a list of all companies.
- **Retrieve Locations**: Access location data associated with a specific company.
- **Retrieve Assets**: Get assets for a particular company, organized by hierarchy.

## Technology Stack

- **Flask**: Lightweight framework for building API endpoints.
- **Flasgger**: Library for integrating Swagger with Flask to automatically generate API documentation.
- **Python**: Core programming language used for API development.

## Installation and Setup

To run the API locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LS-MyProjects/tractian_challenge_api.git
   cd tractian_challenge_api
   ```
2. **Install Dependencies:** Make sure flask, flasgger, and other dependencies are installed. Run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the API:** Start the Flask server by running:
   ```bash
   python api.py
   ```
- The API will be available at `http://127.0.0.1:5000`.
4. **Access Swagger Documentation:** Navigate to `http://127.0.0.1:5000/apidocs/` to view the Swagger UI and interact with the endpoints directly.

## API Documentation

- The API documentation is automatically generated using Swagger and can be accessed by visiting `http://127.0.0.1:5000/apidocs/`. Swagger provides a user-friendly interface to interact with and understand the available endpoints.
 
    ### API Documentation
    1. **Retrieve Companies**:
        - **Endpoint:** /companies
        - **Method:** GET
        - **Description:** Retrieves a list of all companies in the system.
        - **Response:**
            - **200 OK:** Returns an array of company objects 
             ```json
             [
                {
                    "id": "1",
                    "name": "Company A"
                },
                {
                    "id": "2",
                    "name": "Company B"
                },
             ]
             ```
    2. **Retrieve Locations for a Specific Company**:
        - **Endpoint:** /companies/<company_id>/locations
        - **Method:** GET
        - **Description:** Retrieves the locations associated with a specific company.
        - **Response:**
            - **200 OK:** Returns an array of company objects 
             ```json
             [
                {
                    "locationId": "101",
                    "name": "Location X"
                },
                {
                    "locationId": "102",
                    "name": "Location Y"
                },
             ]
             ```
            - **404 Not Found:** If the specified company_id does not exist.

    3. **Retrieve Assets for a Specific Company**:
        - **Endpoint:** /companies/<company_id>/assets
        - **Method:** GET
        - **Description:** Retrieves the assets associated with a specific company.
        - **Path Parameters:**
            - `company_id` **(string):** The ID of the company whose assets are being retrieved.
        - **Response:**
            - **200 OK:** Returns an array of company objects 
             ```json
             [
                {
                   "assetId": "201",
                    "name": "Asset A",
                    "locationId": "101",
                    "sensorType": "Energy",
                    "status": "Active"
                },
                {
                    "assetId": "202",
                    "name": "Asset B",
                    "locationId": "102",
                    "sensorType": "Vibration",
                    "status": "alert"
                },
             ]
             ```
            - **404 Not Found:** If the specified company_id does not exist.
## Example Usage

- Use the following curl commands to interact with the API:
1. **Get All Companies:**
    ```bash
    curl -X GET http://127.0.0.1:5000/companies
    ```
2. **Get All Companies:**
    ```bash
    curl -X GET http://127.0.0.1:5000/companies/1/locations
    ```
3. **Get All Companies:**
    ```bash
    curl -X GET http://127.0.0.1:5000/companies/1/assets
    ```

## Troubleshooting

- **API Not Accessible:** Ensure the server is running by checking the terminal output.
- **Dependency Issues:** Run `pip install -r requirements.txt` to install missing dependencies.
- **Swagger Documentation Not Visible:** Confirm that `flasgger` is installed and that you’ve started the Flask app.
