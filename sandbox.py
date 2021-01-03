"""from requests import get
from json import loads

base_url = "https://heislandmine.work/"

response = get(base_url + "api/v1/timelines/public?limit=2").text

print(loads(response))
"""

from atlatl.lib.auth import create_app

base_url = "https://heislandmine.work/"

create_app(base_url, "atlatl", to_file=".clientcred.secret")