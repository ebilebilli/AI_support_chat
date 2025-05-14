import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from chat.tasks import generate_ai_response_task


class AIChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            await self.close() 
        
        else:
            self.room_name = 'ai_chat_room'
            self.room_group_name = f'chat_{self.room_name}'

            await self.accept()

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            user_message = text_data_json['message']
            result = await sync_to_async(generate_ai_response_task.delay)(user_message)
            ai_response = await sync_to_async(result.get)()
            
            await self.send(text_data=json.dumps({'message': ai_response}))
        except Exception as e:
            await self.send(text_data=json.dumps({f'AI error: {str(e)}'}))
