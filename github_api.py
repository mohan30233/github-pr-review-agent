import requests

def get_pr_files(owner, repo, pr):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr}/files"

    response = requests.get(url)
    return response.json()
