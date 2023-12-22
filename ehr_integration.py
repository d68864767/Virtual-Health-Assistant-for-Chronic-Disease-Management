# Importing necessary libraries
import requests
import pandas as pd
from fhirclient import client

# Define the FHIR compliant server
settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhir.test.com/baseDstu3'
}

# Create a client instance
smart = client.FHIRClient(settings=settings)

def get_patient_data(patient_id):
    """
    Function to get patient data from the EHR using the patient's ID.
    This involves making a GET request to the EHR API and returning the patient's data.
    """
    # Make a GET request to the EHR API
    response = requests.get(f"{settings['api_base']}/Patient/{patient_id}")

    # Convert the response to JSON
    data = response.json()

    return data

def get_patient_observations(patient_id):
    """
    Function to get patient observations from the EHR using the patient's ID.
    This involves making a GET request to the EHR API and returning the patient's observations.
    """
    # Make a GET request to the EHR API
    response = requests.get(f"{settings['api_base']}/Observation?subject=Patient/{patient_id}")

    # Convert the response to JSON
    data = response.json()

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data['entry'])

    return df

def update_patient_data(patient_id, data):
    """
    Function to update patient data in the EHR using the patient's ID and new data.
    This involves making a PUT request to the EHR API.
    """
    # Make a PUT request to the EHR API
    response = requests.put(f"{settings['api_base']}/Patient/{patient_id}", json=data)

    return response.status_code

def delete_patient_data(patient_id):
    """
    Function to delete patient data from the EHR using the patient's ID.
    This involves making a DELETE request to the EHR API.
    """
    # Make a DELETE request to the EHR API
    response = requests.delete(f"{settings['api_base']}/Patient/{patient_id}")

    return response.status_code
