"""
pip install pytest
pip install -U chaipy
"""
from chai_py.auth import set_auth

set_auth('ptJ****', 'yGLDf******Q')

from chai_py import ChaiBot, Update

class EchoBot(ChaiBot):
    """ A simple example bot. """

    def setup(self):
        self.name = 'Echo'

    async def on_message(self, update: Update):
        return f"{self.name}: {update.latest_message.text}"


# Create an instance of the EchoBot
EchoBot()

