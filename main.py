import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEY_VAULT_NAME = "kv-rlukowski-002"
KEY_VAULT_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"

def main():
    print(f" Connection with the KV")
    
    
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KEY_VAULT_URI, credential=credential)

    try:
        secret = client.get_secret("Secret-code")
        
        print(f"::add-mask::{secret.value}")

        print(f"Done")
      
        print(f"Retrieved secret")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
