from channels.generic.websocket import AsyncJsonWebsocketConsumer



class ExchangeConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        print(text_data)
        if text_data == 'PING':
            await self.send('PONG')

    async def disconnect(self, close_code):
        self.event_close = True
