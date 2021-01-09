from mastodon import StreamListener
from atlatl.lib.lib import download_media
import os
class Listener(StreamListener):
    def __init__(self, root_dir=".") -> None:
        super().__init__()
        self.root_dir = root_dir

    def on_update(self, status):
        user_name = status["account"]["username"]
        save_root_dir = self.root_dir + "/" + user_name

        for media in status["media_attachments"]:
            if not os.path.exists(save_root_dir):
                os.mkdir(save_root_dir)
            remote_url = media["url"]
            download_media(remote_url, save_root_dir)
                

