from mastodon import StreamListener
class Listener(StreamListener):
    def __init__(self) -> None:
        super().__init__()

    def on_update(self, status):
        user_name = status["account"]["username"]

        for media in status["media_attachments"]:
            remote_url = media["remote_url"]
                pass

