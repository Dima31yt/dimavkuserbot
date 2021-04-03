## -*- coding: utf-8 -*-
import vk_api, random, time, wikipedia, requests, os
from vk_api.longpoll import VkLongPoll, VkEventType
from bs4 import BeautifulSoup
from vk_api import VkUpload

tokend = "ce2dbe2afa1d0e75534d3db448a19b70d1dfaf6970d38ed569539cc59fa4bf56750ab422a11e2eacd03c7"

vk_session = vk_api.VkApi(token=tokend)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
	vk.messages.send(user_id=id, message=text, random_id=0)

def sender1(id, text):
	vk.messages.send(peer_id=id, message=text, random_id=0)

answ1 = "нет"
answ2 = "qiest2"
answ3 = "qiest3"
answ4 = "qiest4"
answ5 = "qiest5"
answ6 = "qiest6"
answ7 = "qiest7"
answ8 = "qiest8"

send1 = "Никиты Хрущева ответ"
send2 = "get2"
send3 = "get3"
send4 = "get4"
send5 = "get5"
send6 = "get6"
send7 = "get7"
send8 = "get8"

answ_m = "нет"
send_m = "Никиты Хрущева ответ"

wikipedia.set_lang("RU")

sender(400484262, "Бот запущен")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        try:
            if event.from_chat:
                msg = event.text.lower()
                id = event.peer_id
                user = event.user_id
                msgl = event.text

                if msg in ["дима"]:
                    sender1(id, "На месте")

                if msg in ["отклик"]:
                    otk = time.time()
                    sender1(id, str(otk) + ' мс')
                
                if "вики" in event.text.lower():
                    qies3t_wiki = msg.split(" ", 1)
                    try:
                        wiki_redsult = str(wikipedia.summary(qies3t_wiki[1]))
                        sender1(id, wiki_redsult)
                        sender1(id, 'Ответ выдан')
                    except:
                        sender1(id, 'По вашему запросу ничего не найдено')

                if "бинд" in event.text.lower():
                    if user == 400484262:
                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "1":
                                answ1 = str(msg.split(' ', 2)[2].split('|')[0])
                                send1 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ1) + "<br>Ответ: " + str(send1))

                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "2":
                                answ2 = str(msg.split(' ', 2)[2].split('|')[0])
                                send2 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ2) + "<br>Ответ: " + str(send2))
                        
                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "3":
                                answ3 = str(msg.split(' ', 2)[2].split('|')[0])
                                send3 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ3) + "<br>Ответ: " + str(send3))

                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "4":
                                answ4 = str(msg.split(' ', 2)[2].split('|')[0])
                                send4 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ4) + "<br>Ответ: " + str(send4))
                                
                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "5":
                                answ5 = str(msg.split(' ', 2)[2].split('|')[0])
                                send5 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ5) + "<br>Ответ: " + str(send5))
                                
                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "6":
                                answ6 = str(msg.split(' ', 2)[2].split('|')[0])
                                send6 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ6) + "<br>Ответ: " + str(send6))
                                
                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "7":
                                answ7 = str(msg.split(' ', 2)[2].split('|')[0])
                                send7 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ7) + "<br>Ответ: " + str(send7))
                                
                        if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                            if str(msg.split(' ')[1]) == "8":
                                answ8 = str(msg.split(' ', 2)[2].split('|')[0])
                                send8 = str(msgl.split(' ', 2)[2].split('|')[1])
                                sender1(id, "Готово!<br>Вопрос: " + str(answ8) + "<br>Ответ: " + str(send8))
                

                if msg in [answ1]:
                    sender1(id, send1)
                
                if msg in [answ2]:
                    sender1(id, send2)
                
                if msg in [answ3]:
                    sender1(id, send3)
                
                if msg in [answ4]:
                    sender1(id, send4)
                
                if msg in [answ5]:
                    sender1(id, send5)
                
                if msg in [answ6]:
                    sender1(id, send6)
                
                if msg in [answ7]:
                    sender1(id, send7)
                
                if msg in [answ8]:
                    sender1(id, send8)

                if msg in ["онлайн", "кто онлайн"]:
                    f = vk.messages.getConversationMembers(peer_id=id, fields="online")
                    al = -1
                    sw_all = ""
                    try:
                        while True:
                            al = al + 1
                            sw1 = f["profiles"][al]["first_name"]
                            sw2 = f["profiles"][al]["last_name"]
                            sw3 = f["profiles"][al]["id"]
                            sw4 = f["profiles"][al]["online"]
                            if sw4 == 1:
                                sw_al = "[id" + str(sw3) + "|" + sw1 + " " + sw2 + "]"
                                sw_all += "<br>" + sw_al
                    except:
                        sender1(id, 'Пользователи онлайн:' + sw_all)

                if "поцеловать" in event.text.lower():
                    if user == 400484262:
                        kiss_r_u = vk.users.get(user_ids='400484262', name_case='nom')
                        kiss_r_n_1 = kiss_r_u[0]["first_name"]
                        kiss_r_n_2 = kiss_r_u[0]["last_name"]
                        kiss_r_n_f = kiss_r_n_1 + ' ' + kiss_r_n_2
                        kiss_n_f_n = '[id' + str(400484262) + '|' + kiss_r_n_f + ']'

                        kiss_sex_s = ' поцеловал '

                        kiss1 = msg.split(' ')[1]
                        kiss_w_n = kiss1.split("|")[0].replace("[id", "")

                        kiss_r_u1 = vk.users.get(user_ids=kiss_w_n, name_case='acc')
                        kiss_r_n_11 = kiss_r_u1[0]["first_name"]
                        kiss_r_n_21 = kiss_r_u1[0]["last_name"]
                        kiss_r_n_f1 = kiss_r_n_11 + ' ' + kiss_r_n_21
                        kiss_n_f_n1 = '[id' + str(kiss_w_n) + '|' + kiss_r_n_f1 + ']'

                        sender1(id, kiss_n_f_n + kiss_sex_s + kiss_n_f_n1 + ' 😍❤')

                if "обнять" in event.text.lower():
                    if user == 400484262:
                        user = event.user_id
                        kiss_r_u = vk.users.get(user_ids='400484262', name_case='nom')
                        kiss_r_n_1 = kiss_r_u[0]["first_name"]
                        kiss_r_n_2 = kiss_r_u[0]["last_name"]
                        kiss_r_n_f = kiss_r_n_1 + ' ' + kiss_r_n_2
                        kiss_n_f_n = '[id' + str(400484262) + '|' + kiss_r_n_f + ']'

                        kiss_sex_s = ' обнял '

                        kiss1 = msg.split(' ')[1]
                        kiss_w_n = kiss1.split("|")[0].replace("[id", "")

                        kiss_r_u1 = vk.users.get(user_ids=kiss_w_n, name_case='acc')
                        kiss_r_n_11 = kiss_r_u1[0]["first_name"]
                        kiss_r_n_21 = kiss_r_u1[0]["last_name"]
                        kiss_r_n_f1 = kiss_r_n_11 + ' ' + kiss_r_n_21
                        kiss_n_f_n1 = '[id' + str(kiss_w_n) + '|' + kiss_r_n_f1 + ']'

                        sender1(id, kiss_n_f_n + kiss_sex_s + kiss_n_f_n1 + ' 💕😘')
                
            if event.from_me:
                msg = event.text.lower()
                id = event.user_id
                msgl = event.text
                msg_id = event.message_id

                if msg in ['ня']:
                    vk.messages.edit(peer_id=id, message='❤❤❤<br>💚💚💚<br>💚💚💚<br>💚💚💚', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='💚💚💚<br>❤❤❤<br>💚💚💚<br>💚💚💚', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='💚💚💚<br>💚💚💚<br>❤❤❤<br>💚💚💚', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='💚💚💚<br>💚💚💚<br>💚💚💚<br>❤❤❤', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='💚💚💚<br>💚💚💚<br>❤❤❤<br>❤❤❤', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='💚💚💚<br>❤❤❤<br>❤❤❤<br>❤❤❤', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='❤❤❤<br>❤❤❤<br>❤❤❤<br>❤❤❤', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='Я', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='Тебя', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='Люблю', message_id=msg_id)
                    time.sleep(1)
                    vk.messages.edit(peer_id=id, message='❤❤❤', message_id=msg_id)
                    vk.messages.delete(message_ids=msg_id, delete_for_all=1)

                if msg in ["отклик"]:
                    otk = time.time()
                    sender(id, str(otk) + ' мс')

                if "вики" in event.text.lower():
                    qies3t_wiki = msg.split(" ", 1)
                    try:
                        wiki_redsult = str(wikipedia.summary(qies3t_wiki[1]))
                        sender(id, wiki_redsult)
                        sender(id, 'Ответ выдан')
                    except:
                        sender(id, 'По вашему запросу ничего не найдено')

                if msg in ['поцеловать']:
                    kiss_r_u = vk.users.get(user_ids='400484262', name_case='nom', fields='sex')
                    kiss_r_n_1 = kiss_r_u[0]["first_name"]
                    kiss_r_n_2 = kiss_r_u[0]["last_name"]
                    kiss_sex = kiss_r_u[0]["sex"]
                    kiss_r_n_f = kiss_r_n_1 + ' ' + kiss_r_n_2
                    kiss_n_f_n = '[id' + str(400484262) + '|' + kiss_r_n_f + ']'

                    kiss_sex_s = '0'

                    if int(kiss_sex) == 1:
                        kiss_sex_s = ' поцеловала '
                    if int(kiss_sex) == 2:
                        kiss_sex_s = ' поцеловал '

                    kiss_r_u1 = vk.users.get(user_ids=id, name_case='acc')
                    kiss_r_n_11 = kiss_r_u1[0]["first_name"]
                    kiss_r_n_21 = kiss_r_u1[0]["last_name"]
                    kiss_r_n_f1 = kiss_r_n_11 + ' ' + kiss_r_n_21
                    kiss_n_f_n1 = '[id' + str(id) + '|' + kiss_r_n_f1 + ']'

                    sender(id, kiss_n_f_n + kiss_sex_s + kiss_n_f_n1 + ' 😍❤')

                if msg in ['обнять']:
                    kiss_r_u = vk.users.get(user_ids='400484262', name_case='nom', fields='sex')
                    kiss_r_n_1 = kiss_r_u[0]["first_name"]
                    kiss_r_n_2 = kiss_r_u[0]["last_name"]
                    kiss_sex = kiss_r_u[0]["sex"]
                    kiss_r_n_f = kiss_r_n_1 + ' ' + kiss_r_n_2
                    kiss_n_f_n = '[id' + str(400484262) + '|' + kiss_r_n_f + ']'

                    kiss_sex_s = '0'

                    if int(kiss_sex) == 1:
                        kiss_sex_s = ' обняла '
                    if int(kiss_sex) == 2:
                        kiss_sex_s = ' обнял '

                    kiss_r_u1 = vk.users.get(user_ids=id, name_case='acc')
                    kiss_r_n_11 = kiss_r_u1[0]["first_name"]
                    kiss_r_n_21 = kiss_r_u1[0]["last_name"]
                    kiss_r_n_f1 = kiss_r_n_11 + ' ' + kiss_r_n_21
                    kiss_n_f_n1 = '[id' + str(id) + '|' + kiss_r_n_f1 + ']'

                    sender(id, kiss_n_f_n + kiss_sex_s + kiss_n_f_n1 + ' 💕😘')

                if msg in ['wall']:
                    sender(id, 'Ожидайте')
                    try:
                        while True:
                            ran1 = ['Я люблю тебя', 'Пошли в личку', 'Ответь уже']
                            ran = random.choice(ran1)
                            vk.wall.post(message=ran, owner_id=str(id))
                    except Exception as e:
                        print(e)
                        time.sleep(2)
                        sender(id, e)

                if "бинд" in event.text.lower():
                    if (len(msg) > 4) and msg.split(' ')[0] == "бинд":
                        if str(msg.split(' ')[1]) == "m":
                            answ_m = str(msg.split(' ', 2)[2].split('|')[0])
                            send_m = str(msgl.split(' ', 2)[2].split('|')[1])
                            sender(id, "Готово!<br>Вопрос: " + str(answ_m) + "<br>Ответ: " + str(send_m))

                if msg in [answ_m]:
                    sender(id, send_m)

                if msg in ['тест таблица']:
                    url = 'https://docs.google.com/document/d/1VqkRfCDz89vUQ_jKN1BBzM7D6C7XGA7XWfxBc0fVE0w'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('meta', property="og:image")
                    a = str(quotes[0]).split('"')[1]

                    filename = "\\app\\files\\" + os.path.basename(a).split('?')[0] + ".jpg"
                    if(os.path.isfile(filename)): os.remove(filename)
                    r = requests.get(a)
                    with open(filename, 'wb') as f:
                        f.write(r.content)

                    upload = VkUpload(vk_session)
                    ph = [filename]
                    photo_list = upload.photo(photos=ph, album_id=278675304, group_id=201980948)

                    vk.messages.send(user_id=id, message="Таблица тест", random_id=0, attachment="photo" + str(photo_list[0]["owner_id"]) + "_" + str(photo_list[0]["id"]))

                if msg in ['квест таблица']:
                    url = 'https://docs.google.com/document/d/1PZA58N21QW3W1cdjV2TLNVa0352lYtf_M9zNksLknms'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('meta', property="og:image")
                    a = str(quotes[0]).split('"')[1]

                    filename = "\\app\\files\\" + os.path.basename(a).split('?')[0] + ".jpg"
                    if(os.path.isfile(filename)): os.remove(filename)
                    r = requests.get(a)
                    with open(filename, 'wb') as f:
                        f.write(r.content)

                    upload = VkUpload(vk_session)
                    ph = [filename]
                    photo_list = upload.photo(photos=ph, album_id=278675304, group_id=201980948)

                    vk.messages.send(user_id=id, message="Таблица продвижения команд", random_id=0, attachment="photo" + str(photo_list[0]["owner_id"]) + "_" + str(photo_list[0]["id"]))

                if msg in ['чс+']:
                    chs_r_u = vk.users.get(user_ids=id, name_case='nom', fields='sex')
                    chs_r_n_1 = chs_r_u[0]["first_name"]
                    chs_r_n_2 = chs_r_u[0]["last_name"]
                    chs_sex = chs_r_u[0]["sex"]
                    chs_r_n_f = chs_r_n_1 + ' ' + chs_r_n_2
                    chs_n_f_n = '[id' + str(id) + '|' + chs_r_n_f + ']'
                    if int(chs_sex) == 1:
                        chs_sex_s = ' добавлена '
                    if int(chs_sex) == 2:
                        chs_sex_s = ' добавлен '
                    sender(id, chs_n_f_n + chs_sex_s + 'в чёрный список')
                    vk.account.ban(owner_id=id)

            if event.to_me:
                msg = event.text.lower()
                id = event.user_id

                if msg in [answ_m]:
                    sender(id, send_m)

        except Exception as e:
            sender(400484262, str(e))
            print(e)
