from flask import Flask, jsonify
from flasgger import Swagger
import json

app = Flask(__name__)
swagger = Swagger(app)

# Load JSON data
with open('api-data.json', 'r') as f:
    data = json.load(f)

# GET - return a list of companies
@app.route('/companies', methods=['GET'])
def get_companies():
    """
    Retrieve a list of companies
    ---
    responses:
      200:
        description: A list of companies
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: The ID of the company
              name:
                type: string
                description: The name of the company
    """
    return jsonify(data["companies"])

# GET - return a list of locations from one company
@app.route('/companies/<company_id>/locations', methods=['GET'])
def get_company_locations(company_id):
    """
    Retrieve a list of locations for a specific company
    ---
    parameters:
      - name: company_id
        in: path
        type: string
        required: true
        description: The ID of the company
    responses:
      200:
        description: A list of locations for the specified company
        schema:
          type: array
          items:
            type: object
            properties:
              locationId:
                type: string
                description: The ID of the location
              name:
                type: string
                description: The name of the location
      404:
        description: Company not found
    """
    if company_id not in data:
        return jsonify({'error': 'Company not found'}), 404

    locations = []
    for asset in data.get(company_id, {}).get('assets', []):
        if 'locationId' in asset and asset['locationId']:
            locations.append(asset)
    return jsonify(locations)

# GET - return a list of assets from one company
@app.route('/companies/<company_id>/assets', methods=['GET'])
def get_company_assets(company_id):
    """
    Retrieve a list of assets for a specific company
    ---
    parameters:
      - name: company_id
        in: path
        type: string
        required: true
        description: The ID of the company
    responses:
      200:
        description: A list of assets for the specified company
        schema:
          type: array
          items:
            type: object
            properties:
              assetId:
                type: string
                description: The ID of the asset
              name:
                type: string
                description: The name of the asset
      404:
        description: Company not found
    """
    if company_id not in data:
        return jsonify({'error': 'Company not found'}), 404

    assets = data.get(company_id, {}).get('assets', [])
    return jsonify(assets)

if __name__ == '__main__':
    app.run(debug=True)