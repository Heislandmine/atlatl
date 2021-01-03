def load_secret(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        secrets: list = [line.strip() for line in f.readlines()]
        secrets_dict: dict = {key: secrets for key, secrets in zip(["client_key", "client_secret", "access_token"], secrets)}
    return secrets_dict
