import telebot
from telebot import types
import time
import schedule

BOT_TOKEN = "6910054215:AAHEUpxHVOcVInq-EUoqo231cnrc9cpC9_s"

bot = telebot.TeleBot(BOT_TOKEN)
markup = types.InlineKeyboardMarkup(row_width=2)
itembtn1 = types.InlineKeyboardButton('О нас', callback_data='about_dunie')
itembtn2 = types.InlineKeyboardButton('Принципы и ценности', callback_data='core_values')
itembtn3 = types.InlineKeyboardButton('Наши инструменты', callback_data='our_tools')
itembtn5 = types.InlineKeyboardButton('Будущее Дуние', callback_data='future_of_dunie')
itembtn6 = types.InlineKeyboardButton('Контактные данные', callback_data='contact_info')


@bot.message_handler(commands=['start'])
def handle_start(message):
    global user_id
    user_id = message.chat.id
    # Приветственное сообщение
    text_hello = "<b>Привет!</b>\nВас приветствует команда <b>Международной группы компаний Адам Адал Жол и МБК Дуние</b>\n\nЗдесь вы сможете ознакомиться с продуктами, идеями и ценностями, которые транслирует и предоставляет наша группа компаний!"
    photo_path_hello = "images/hello_photo.jpg"
    with open(photo_path_hello, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text_hello, parse_mode='HTML')
    time.sleep(5)
        
    text_about = "<b>Первое позитивное планетарное движение</b>\n\nМБК «ДУНИЕ» является международной некоммерческой, членской, благотворительной организацией, созданной на добровольном объединении граждан, физических и/или юридических лиц на ОСНОВЕ чистоты, равенства, сохранности и защиты все вся всех всего, живых и не живых, всего человечества, животного мира, экологического оздоровления жизни и планеты, Благо-творения, Благо-человечности, Благо-человеческой семьи, Благо-живым и не живым, Благо-справедливости и всеобщего мира, Благо-созидательности, содействия и осуществления взаимодействия человечества, граждан, народов, населения, нации, всех государств и не государств, республик и не республик, монархии и не монархии, религиозных и не религиозных, конфессий и не конфессий, государственных и не государственных, сообществ, членств, организаций."
    photo_path_about = "images/about_dunie.jpg"
    with open(photo_path_about, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text_about, parse_mode='HTML')

    time.sleep(8)
    text_principles = '''<b>Солидарность</b>\n\nМы верим в солидарность и взаимопомощь, в общую ответственность перед будущим поколением и нашей планетой.\n\n<b>Справедливость</b>\n\nМы стремимся к созданию справедливого общества, где люди не будут ограничены неравенством, дискриминацией и эксплуатацией.\n\n<b>Инновации</b>\n\nМы ищем новые идеи и решения, чтобы преобразовать системы и процессы в более прорывные ноосферные, природоподобные, экологически устойчивые.\n\n<b>Исключим из жизни</b> \n\nБоль, страх, искажения. Имеем решения как прекратить войны, болезни, снять все долговое бремя кредитов по планете, как с государств, так и с человека.'''
    photo_path_principles = 'images/principles.jpg'
    
    with open(photo_path_principles, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text_principles, parse_mode='HTML')

    time.sleep(8)
    text_tools = "<b>CVB</b>\n\n🚀«Converted Virtual Balance» или «Конвертируемый Виртуальный Баланс»"
    bot.send_message(message.chat.id, text_tools, parse_mode="HTML")
    time.sleep(3)
    text_tools = "Что такое CVB и что он дает для всех всё вся всего, народа, человечества, государства, бизнеса и Вас самих?"
    bot.send_message(message.chat.id, text_tools, parse_mode="HTML")
    time.sleep(3)
    text_tools2 = "«Converted Virtual Balance» -«Конвертируемый  виртуальный баланс» CVB - это программное обеспечение для персонального компьютера и мобильное приложение для любого гаджета, которое дает возможность: \n\n• конвертировать любую валюту мира без\n\nпривязки к любой бирже, любому кросс курсу ;\n\n• отправлять деньги в любую точку мира засекунды и получать их;\n\n• осуществлять куплю-продажу любыхтоваров и услуг по всему миру;\n\n• хранить свои сбережения, зарплату,пенсию без каких-либо финансовых потерь из-за обменных курсов."
    markup_tools = types.InlineKeyboardMarkup(row_width=2)
    tools_btn1 = types.InlineKeyboardButton("Преимущества", callback_data="cvb_advantages")
    tools_btn2 = types.InlineKeyboardButton("Польза", callback_data="cvb_benefits")
    tools_btn3 = types.InlineKeyboardButton("Узнать подробнее про CVB", url="https://telegra.ph/CHto-takoe-Konvertiruemyj-virtualnyj-balans--CVB-03-09")
    # tools_btn4 = types.InlineKeyboardButton("Назад ◀️", url="")
    markup_tools.add(tools_btn1, tools_btn2, tools_btn3)
    bot.send_message(message.chat.id, text_tools2, reply_markup=markup_tools)

@bot.message_handler(commands=['about'])
@bot.callback_query_handler(func=lambda call: call.data == 'about_dunie')

def handle_about(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    
    text = "<b>Первое позитивное планетарное движение</b>\n\nМБК «ДУНИЕ» является международной некоммерческой, членской, благотворительной организацией, созданной на добровольном объединении граждан, физических и/или юридических лиц на ОСНОВЕ чистоты, равенства, сохранности и защиты все вся всех всего, живых и не живых, всего человечества, животного мира, экологического оздоровления жизни и планеты, Благо-творения, Благо-человечности, Благо-человеческой семьи, Благо-живым и не живым, Благо-справедливости и всеобщего мира, Благо-созидательности, содействия и осуществления взаимодействия человечества, граждан, народов, населения, нации, всех государств и не государств, республик и не республик, монархии и не монархии, религиозных и не религиозных, конфессий и не конфессий, государственных и не государственных, сообществ, членств, организаций."
    photo_path = "images/about_dunie.jpg"

    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=text, parse_mode='HTML')



    file_path = "files/dunie.pdf"
    with open(file_path, 'rb') as photo:
        bot.send_document(chat_id, photo, caption="Презентация Дуние")


# Обработчик для кнопки "Ключевые принципы и ценности"
@bot.message_handler(commands=['values'])
@bot.callback_query_handler(func=lambda call: call.data == 'core_values')
def handle_principles(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    
    text = '''<b>Солидарность</b>\n\nМы верим в солидарность и взаимопомощь, в общую ответственность перед будущим поколением и нашей планетой.\n\n<b>Справедливость</b>\n\nМы стремимся к созданию справедливого общества, где люди не будут ограничены неравенством, дискриминацией и эксплуатацией.\n\n<b>Инновации</b>\n\nМы ищем новые идеи и решения, чтобы преобразовать системы и процессы в более прорывные ноосферные, природоподобные, экологически устойчивые.\n\n<b>Исключим из жизни</b> \n\nБоль, страх, искажения. Имеем решения как прекратить войны, болезни, снять все долговое бремя кредитов по планете, как с государств, так и с человека.'''
    photo_path = 'images/principles.jpg'
    
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=text, parse_mode='HTML')


# Обработчик для кнопки "Наши инструменты"
@bot.message_handler(commands=['tools'])
@bot.callback_query_handler(func=lambda call: call.data == 'our_tools')
def handle_tools(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    text = "<b>CVB</b>\n\n<b>«Converted Virtual Balance» или «Конвертируемый Виртуальный Баланс»</b>\n\nЧто такое CVB и что он дает для всех всё вся всего, народа, человечества, государства, бизнеса и Вас самих?\n\nВо-первых, это программное обеспечение, которое дает возможность конвертировать любую валюту мира без привязки к любой бирже, без привязки к любому кросс курсу, без финансовых потерь.\n\nВо-вторых, это решение для всех секторов экономики и в жизни человека, в том числе по любым транзакциям.\n\n<b>Что даст CVB:</b>\n\nЭто снижение финансовой зависимости от внешних регуляторов, постепенный уход от внешних финансовых влияний, выход из разных долговых ям и обязательств, как и у самого государства, так и у человечества.\n\nИ еще - возможность иметь низкие устойчивые цены на все товары и услуги посредством оплаты через систему CVB.\n\n<b>Девиз продукта: Нет больше финансовых границ!</b>"
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)
    
# Обработчик для кнопки "Перспективы"
@bot.message_handler(commands=['perspectives'])
@bot.callback_query_handler(func=lambda call: call.data == 'perspectives')
def perspectives(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    text = "<b>Перспективы</b>\n\nВсе доходы от работы платформы идут в строительство уникальных инновационных городов, где мир , спокойствие , справедливость , любовь , труд по предназначению и оплата благами по труду, доступ всем ко всем знаниям, теглубокое образование с малых лет без нагрузки, требований, искажений и тп.\n\nТакже доходы от работы платформы идут в создание в промышленных масштабах для всего населения мира самых современных, экологичных, прорывных и футуристических вещей бытового назначения,  медицины и питания - вот абсолютно все иное,  работающее во благо человека и его организма. Что приведет к включению механизмов регенерации и самовосстановления; омоложения и баланса внутри<b></b>"
    photo_path = 'images/perspectives.jpg'
    
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=text, parse_mode='HTML')


# Обработчик для кнопки "Будущее позитивного планетарного движения"
@bot.message_handler(commands=['future'])
@bot.callback_query_handler(func=lambda call: call.data == 'future_of_dunie')
def handle_tools(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    text = "<b>Будущее Планетарного движения</b>\n\nСегодняшнее и будущее дома нашего, общего корабля - планета Земля - зависит лишь от всех нас, те от Человека и Человечества!\n\n<b>Какой у нас Образ будущего?</b>\n\nПозитивное планетарное движение в рамках ЖИВОЙ дорожной карты дает решения для абсолютно всех вопросов , ситуаций на планете Земля , как бы это фантастично не звучало, но это именно так.\n\nЗаявление пресс службы всегда принимается ко вниманию. А мы трудимся по своему желанию и решению с душой - для все вся всех всего и согласно только нашего Устава, зарегистрированного единым текстом по всем государствам планеты.\n\n<b></b>"
    photo_path = "images/future.jpg"
    
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=text, parse_mode='HTML')
    time.sleep(3)
    bot.send_message(chat_id, "<b>Думай только сам! Спроси сам! Узнай сам! Реши сам! Как ты хочешь тут жить.</b>", parse_mode="HTML")


# Обработчик для кнопки "Контактные данные"
@bot.message_handler(commands=['contact'])
@bot.callback_query_handler(func=lambda call: call.data == 'contact_info')
def handle_tools(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    text = "<b>Контактные данные</b>\n\nТелефон: +7 909 888 82 09\n<a href='https://t.me/conso27'>Telegram</a>\n<a href='https://vk.com/dunie'>ВК</a>\n<a href='https://dunie.press'>Сайт Дуние</a>\n<a href='https://www.youtube.com/@Dunie-2024'>Youtube</a>\nEmail: 7928117@mail.ru"
    bot.send_message(chat_id, text, parse_mode="HTML")
    time.sleep(3)



@bot.callback_query_handler(func=lambda call: call.data == 'cvb_advantages')
def handle_tools(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    text = "<b>Преимущества</b>\n\nБез привязки к бирже CVB работает без привязки к кросс курсам, без привязки к мировым биржам\n\nСвобода от валютного контроля\n Беспрепятственные операции в любую точку мира, не подвергаясь валютному контролю\n\nВысокая скорость\nПрактически моментальное движение средств через CVB без блокировок и заморозок\n\nБез комиссий за транзакции\nCVB не взимает комиссии за транзакции и оплату за конвертацию\n\nCVB будет размещено только на государственных серверах, которое предоставляет техподдержку на территории этой страны"
    bot.send_message(chat_id, text, parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data == 'cvb_benefits')
def handle_tools(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    text = "<b>Польза:</b>\n\nCVB для народа и для человека\n\nЭто низкие цены на всё необходимое для жизни:\nпродукты питания, жилье, автомобили, одежду, коммунальные и другие услуги. В любом секторе, где человек будет использовать для оплаты CVB цена снизится от 50 до 80%\n\nCVB для государства\nИмея высокий оборот местной валюты, экономика будет расти, государство будет иметь большую привлекательность, как для инвесторов, так и для всех фондов мира и финансовых институтов.\n\n• CVB для бизнеса и финансовых институтов\nЧерез CVB бизнес может осуществлять любые сделки, заключать любые контракты с кем угодно в рамках закона\n\nЛюбое перечисление и перевод средств через CVB, будет проходить и поступать клиенту, также быстро и безболезненно, как смс через любой мессенджер или чат \n\n📣Девиз продукта: Нет больше финансовых границ!"
    bot.send_message(chat_id, text, parse_mode="HTML")

messages_to_send = [
    "Сообщение 1",
    "Сообщение 2",
    "Сообщение 3"
]
user_id = None

def send_message_to_user():
    global user_id
    if messages_to_send:
        message_text = messages_to_send.pop(0)  # Извлекаем первое сообщение из списка
        bot.send_message(user_id, message_text)
    else:
        # Если список пуст, то снова наполняем его
        messages_to_send.extend([
            "Сообщение 1",
            "Сообщение 2",
            "Сообщение 3"
        ])
        
schedule.every().minute.do(send_message_to_user)  

# Функция для запуска расписания
# def run_schedule():
#     while True:
#         schedule.run_pending()
#         time.sleep(5)

# # Запуск расписания в отдельном потоке
# import threading
# threading.Thread(target=run_schedule).start()



# Обработчик для кнопки "Юридический Каркас"
@bot.message_handler(commands=['legal'])
@bot.callback_query_handler(func=lambda call: call.data == 'legal_framework')
def handle_tools(message_or_query):
    if isinstance(message_or_query, telebot.types.Message):
        chat_id = message_or_query.chat.id
    elif isinstance(message_or_query, telebot.types.CallbackQuery):
        chat_id = message_or_query.message.chat.id
    text = "<b>Юридический каркас</b>\n\nДвижение и дорожная карта проявлены юридическими лицами с единым уставом в рамках которого ведется вся деятельность по всей планете.\nНаши компании: МБК Дуние и ООО Адам Адал Жол представлены в Российской Федерации, Кыргызстане, Казахстане, Канаде, Индии, Турции. На данный момент идет процесс регистрации и выстраивания отношений в более чем 90 стран мира и в течении полугода наша группа компаний проявится во всех 251 странах.\nНаша группа компаний трудится во благо человечества, в том числе мы занимаемся образовательной, воспитательной и медицинской деятельностью F 0, социальными и строительными программами.\nГруппа компаний является заказчиком разнообразных программных продуктов. В том числе СѴВ выходит на рынок; платформа платформ на очереди. Затем будут и другие программные Продукты"
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)






    
bot.polling(none_stop=True, timeout=120)
