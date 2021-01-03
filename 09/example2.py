import requests
import os 
import json

def list_repos(host, access_token):
    '''Lists repositories that the authenticated user has explicit permission,
    (:read, :write, or :admin) to access.

    :param str host: URL GitHub.
    :param str access_token: GitHub access token.
    '''

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {access_token}"
    }

    path = "/user/repos"
    r = requests.get(host+path, headers=headers)
    data_json = json.loads(r.content)

    repos = [repo["name"] for repo in data_json]
    
    return repos

if __name__ == "__main__":
    
    
    host = "https://api.github.com" #host GitHub

    #get access token from environment variable
    access_token = os.environ["TOKEN_GITHUB"]

    print("listing repos...")
    #call function list_repos
    list_repos = list_repos(host, access_token)

    print("repos:\n")
    for repo in list_repos:
        print(f"repo_name: {repo}") 
