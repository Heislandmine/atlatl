from requests import post
import json


def create_app(
    url,
    client_name,
    redirect_uris="urn:ietf:wg:oauth:2.0:oob ",
    scopes=None,
    website=None,
    to_file=None,
    **kwargs,
):

    params = {
        "client_name": client_name,
        "redirect_uris": redirect_uris,
        "scopes": scopes,
        "website": website,
    }

    if "test" in kwargs:
        post_stab = kwargs["stab"]
        response = post_stab()
        response_dict = response
    else:
        response = post(url + "/api/v1/apps", data=params)
        response_dict = json.loads(response.text)

    if to_file:
        with open(
            to_file,
            "w",
        ) as f:
            f.writelines(response_dict["client_id"] + "\n")
            f.write(response_dict["client_secret"] + "\n")
            f.write(response_dict["vapid_key"] + "\n")
            f.write(url)
    else:
        print(response_dict["client_id"])
        print(response_dict["client_secret"])
        print(response_dict["vapid_key"])
        print(url)
