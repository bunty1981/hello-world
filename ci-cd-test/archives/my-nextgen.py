import requests
import json

# NextGen FHIR API base URL
fhir_base_url = "https://fhir.nextgen.com/nge/prod/fhir-api/fhir/dstu2/"

# OAuth 2.0 credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
token_url = "https://fhir.nextgen.com/nge/prod/patient-oauth/token"

# Function to obtain an access token
def get_access_token():
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(token_url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()["access_token"]

# Function to retrieve patient data
def get_patient_data(patient_id, access_token):
    url = f"{fhir_base_url}Patient/{patient_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Main function
def main():
    access_token = get_access_token()
    patient_id = "YOUR_PATIENT_ID" 

    patient_data = get_patient_data(patient_id, access_token)
    print(json.dumps(patient_data, indent=2))

if __name__ == "__main__":
    main()