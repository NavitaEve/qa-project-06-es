import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def user_token():
    token = post_new_user(data.user_body)
    data_token = token.json()
    return data_token['authToken']


def post_new_client_kit(kit_body):
    token = user_token()
    data.headers['Authorization'] = f"Bearer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.headers)


