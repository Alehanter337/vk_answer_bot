import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token='25553a11681b3c3d86e9653b64ea657151f4d1ae502c7a6c8dd2ae03c897ace6ad068c56389f282f769c4')

longpoll = VkBotLongPoll(vk, 197353035)


for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('New message:', event.obj.message.get('text'))
            if event.from_user:
                if event.obj.message['text'] == 'А':
                    vk.method(
                        "messages.send",
                        {"random_id": 0,
                         "user_id": event.obj.message['peer_id'],
                         "message": 'Здарова'}
                    )

            if event.from_chat:
                if event.obj.message['text'] == 'Привет':
                    vk.method(
                        "messages.send",
                        {"random_id": 0,
                         "peer_id": event.obj.message['peer_id'],
                         "message": 'Здарова'}
                    )
                if event.obj.message['text'] == 'ало':
                    vk.method(
                        "messages.send",
                        {"random_id": 0,
                         "peer_id": event.obj.message['peer_id'],
                         "message": 'ну как там с деньгами'}
                    )
                else:
                    vk.method(
                        "messages.send",
                        {"random_id": 0,
                         "peer_id": event.obj.message['peer_id'],
                         "message": 'иди нахуй'}
                    )
                print ('message from bot was sended')


