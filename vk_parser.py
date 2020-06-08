import vk_api
import time
import codecs

if __name__ == '__main__':
    vk_session = vk_api.VkApi('login', 'password')
    vk_session.auth()
    vk = vk_session.get_api()

    # Возраст от и до
    age = 18
    age_max = 50

    # Номер города
    s_num = 1
    # Номер страны
    country_number = 3

    # По необходимости - 1 - девушки, 2 - парни
    # gender = 2

    for city_number in s_num:
        ff = codecs.open('{}_result.txt'.format(city_number), 'a', encoding='utf8')
        while age <= age_max:
            month = 1
            while month <= 12:
                # Пауза для API
                time.sleep(4)
                print('City' + str(city_number) + "Download ID: " + str(age) + ' age, born in ' + str(month))
                z = vk.users.search(count=1000,
                                    fields='id, photo_max_orig, has_photo, '
                                           'first_name, last_name',
                                    city=city_number,
                                    country=country_number,
                                    # sex=gender,
                                    age_from=age,
                                    age_to=age,
                                    birth_month=month)
                month = month + 1
                print('Peoples count: ' + str(z['count']))
                for x in z['items']:
                    if x['has_photo'] == 1:
                        s = str(x['id']) + '|' + str(x['photo_max_orig']) + '|' + str(
                            x['first_name']) + ' ' + str(x['last_name']) + '\n'
                        ff.write(s)
            age = age + 1
        ff.close()
        age = 1
        month = 1
        print('Done!')
