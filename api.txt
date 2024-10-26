from flask import Flask, jsonify
import json

app = Flask(__name__)

#Load json data
with open ('api-data.json', 'r') as f:
    data = json.load(f)

# GET - return a list of companies
@app.route('/companies')
def get_companies():
    return jsonify(data["companies"])

# GET - return a list of locations from one company
@app.route('/companies/<company_id>/locations')
def get_company_locations(company_id):
    if company_id not in data:
        return jsonify ({'error' : 'Company not found'}), 404

    locations = []
    for asset in data[company_id]['assets']:
        if 'locationId' in asset and asset['locationId']:
            locations.append(asset)
    return jsonify(locations)

# GET - return a list of assets from one company
@app.route('/companies/<company_id>/assets')
def get_company_assets(company_id):
    if company_id not in data:
        return jsonify({'error': 'Company not found'}), 404

    assets = []
    for asset in data[company_id]['assets']:
        assets.append(asset)
    return jsonify(assets)

if __name__ == '__main__':
    app.run(debug=True)