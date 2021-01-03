from mastodon import Mastodon
import os.path

clientcred_file = ".clientcred.secret"


def init_app(app_name, url, email, password):
    if os.path.exists(clientcred_file) is False:
        Mastodon.create_app(app_name, api_base_url=url, to_file=".clientcred.secret")
    app = Mastodon(client_id=".clientcred.secret", api_base_url=url)
    app.log_in(email, password, to_file=".usercred.secret")
