from atlatl.auth import init_app
import sys

app_name = sys.argv[1]
url = sys.argv[2]
email = sys.argv[3]
password = sys.argv[4]
print(email)
print(password)
init_app(app_name, url, email, password)
