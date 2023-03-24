import os

from dotenv import load_dotenv

import vk_api

load_dotenv()


vk_session = vk_api.VkApi(token=os.environ.get('VK_TOKEN'))
vk = vk_session.get_api()

query = {'city': '2', 'sex': '1', 'first_name': 'В'}
result = vk.users.search(**query)


print('Количество женщин из Санкт-Петербурга с именем, начинающимся на букву В:', result['count'])
