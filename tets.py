from mastodon import Mastodon
from atlatl.streaming import Listener

base_url = "http://heislandmine.work"
mastodon = Mastodon(api_base_url=base_url, access_token="secret")

mastodon.stream_user(Listener())