import pytest
from channels.routing import URLRouter
from channels.testing import WebsocketCommunicator
from..routing import websocket_urlpatterns


@pytest.mark.asyncio
class TestChatConsumer:
    async def test_connect(self, settings):
        application = URLRouter(websocket_urlpatterns)
        communicator = WebsocketCommunicator(application, "/ws/chat/lobby/")
        connected, subprotocol = await communicator.connect()
        assert connected
        await communicator.disconnect()
