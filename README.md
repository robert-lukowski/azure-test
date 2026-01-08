# Azure Key Vault Integration Demo

This repository demonstrates how to securely retrieve secrets from Azure Key Vault using Python and GitHub Actions.

## Technical Workflow
1. Authentication: The GitHub Action authenticates to Azure using a Service Principal via the azure/login action.
2. Execution: The pipeline sets up the environment and installs Python dependencies (azure-identity, azure-keyvault-secrets).
3. Retrieval: The script connects to the Key Vault instance and retrieves the secret programmatically.

## Project Structure
* main.py: Python script that connects to Azure using DefaultAzureCredential.
* .github/workflows/demo.yml: CI/CD pipeline definition for GitHub Actions.

## Configuration
To run this workflow, the repository requires the following GitHub Secret:
* AZURE_CREDENTIALS: JSON output from the Azure Service Principal creation command.

## Usage
1. Navigate to the Actions tab.
2. Select "Test Pipeline" from the workflows list.
3. Click the "Run workflow" button to trigger the execution manually.
