import os.path
import requests
def load_secret(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        secrets: list = [line.strip() for line in f.readlines()]
        secrets_dict: dict = {key: secrets for key, secrets in zip(["client_key", "client_secret", "access_token"], secrets)}
    return secrets_dict

def download_media(url, root_path="."):
    response: requests.Response =  requests.get(url)
    file_name = os.path.basename(url).split("?")[0]
    save_dir = root_path + "/" + file_name
    with open(save_dir, "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    url = "https://storage.googleapis.com/misskey-bucket/misskey-files/webpublic-482f1295-5d04-4f94-9f32-a19a54aed2eb.png"
    download_media(url)