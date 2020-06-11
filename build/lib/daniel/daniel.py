import os
import slack


class Daniel:
    def __init__(self, emoticon=' :dollar: ', token=os.environ["slack_token"], channel='automatic-reporting'):
        """Create the Daniel."""
        self.job_name = None
        self.ender = emoticon
        self.starter = emoticon
        self.channel = channel
        self.client = slack.WebClient(token=token)

    def say(self, msg, channel=None, enders=True):
        if channel is None:
            channel=self.channel
        if enders:
            self.client.chat_postMessage(
                    channel=channel,
                    text=self.starter + msg + self.ender)
        else:
            self.client.chat_postMessage(
                channel=channel,
                text=msg)

    def upload_file(self, title, filename, channel=None):
        if channel is None:
            channel = self.channel
        file = open(filename, 'rb')
        self.client.files_upload(channels=channel, filename=filename, file=file, title=title)
        file.close()

