import requests
import os 
import json

def create_repo(host, access_token, repo_name):

    '''Creates a new repository in GitHub.
    :param str host: URL GitHub.
    :param str access_token: GitHub access token.
    :param str repo_name: Name of the repository.
    '''

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {access_token}"
    }

    data = {
        "name":f"{repo}"
    }
    path = f"{host}/user/repos"

    #using method POST
    r = requests.post(path, headers=headers, data=json.dumps(data))

    data_json = json.loads(r.content)

    if r.status_code == 201:
        print("successfully created repository - code: {r.status_code}")
    else:
        print(f"repository not created - code: {r.status_code}")
    
    return data_json

if __name__ == "__main__":
    #host GitHub
    host = "https://api.github.com"
    #get access token from environment variable
    access_token = os.environ["TOKEN_GITHUB"]
    #owner
    owner = "alissonit"
    #repo
    repo = "create_from_pythontrap"
    #create a new repo
    new_repo = create_repo(host, access_token, repo)

