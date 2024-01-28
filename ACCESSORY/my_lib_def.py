import telebot

def retern_dict_use_data (message):
    NameTable = str(message.from_user.first_name) + str(message.from_user.id)
    user_id = str (message.from_user.id)
    user_name = message.from_user.first_name
    tittlenamemenu_choised = message.text
    user_data = {
        'user_id':user_id,
        'user_name':user_name,
        'user_name_id': user_name  + user_id,
        'tittlenamemenu_choised': tittlenamemenu_choised
    }
    return user_data