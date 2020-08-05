import pytest
from channels.testing import WebsocketCommunicator
from ..consumers import ChatConsumer

TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# WIP
@pytest.mark.asyncio
class TestChatConsumer:
    async def test_connect(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        communicator = WebsocketCommunicator(ChatConsumer, "/ws/chat/lobby/")
        # Not working because scope needs to be overridden 
        connected, subprotocol = await communicator.connect()
        assert connected
