# for init plaid client
import plaid, os
from plaid.api import plaid_api
from dotenv import load_dotenv
# load additional plaid components for link token / init requests
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

startPlaid(){
    # load the env file for keys
    load_dotenv()

    # load secrets as passed env variables
    PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
    #print(f"PLAID_CLIENT_ID: {PLAID_CLIENT_ID}")
    PLAID_SECRET = os.getenv("PLAID_SECRET")
    #print(f"PLAID_SECRET: {PLAID_SECRET}")
    PLAID_ENV = os.getenv("PLAID_ENV")

    # config object to init plaid
    configuration = plaid.Configuration(
        host = plaid.Environment.Sandbox,
        api_key={
            'clientId' : PLAID_CLIENT_ID,
            'secret' : PLAID_SECRET,
        }
    )

    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)
    return client
}

# create link token with plaid api
generateLinkToken(){
    request_data = {
        'user':{
            'client_user_id' : 
        }
    }
}

