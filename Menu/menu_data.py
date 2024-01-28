menu_parents = [{"tittlenamemenu": "Прочие запросы", "labale": "B", "parent": "G",
                 "description": "Данный раздел в проработке", "iswork":False},
                {"tittlenamemenu": "🏆 Выбор тренировки", "labale": "A", "parent": "G",
                 "description": "Выбирте один из видов тренировки используя меню", "iswork":True},
                {"tittlenamemenu": "🌍 Перевод", "labale": "A1", "parent": "A",
                 "description": "Выбирте тип тренировки используя меню", "iswork":True},
                {"tittlenamemenu": "🇬🇧🔄🇷🇺 Перевод с Английского на Русский", "labale": "A1A", "parent": "A1",
                 "description": "Необходимо ", "iswork":True},
                {"tittlenamemenu": "🇷🇺🔄🇬🇧 Перевод c Русского на Английский", "labale": "A1B", "parent": "A1",
                 "description": "", "iswork":True},
                {"tittlenamemenu": "Неправильные глаголы", "labale": "A2", "parent": "A",
                 "description": "", "iswork":False},
                {"tittlenamemenu": "🖼️🇷🇺🔄🇬🇧 Перевод картинки", "labale": "A3", "parent": "A",
                 "description": "", "iswork":False},
                {"tittlenamemenu": "🇷🇺🔄🇬🇧📝 Глагол в инфинитиве", "labale": "A2A", "parent": "A2",
                 "description": "", "iswork":False},
                {"tittlenamemenu": "🇷🇺🔄🇬🇧4️⃣📝 Глагол 4 формы", "labale": "A2B", "parent": "A2",
                 "description": "", "iswork":False},
                {"tittlenamemenu": "🌐📷✍️🇬🇧 Картинка из интернета", "labale": "A3A", "parent": "A3",
                 "description": "", "iswork":False}]


"""
<body>
    <h2>Данный раздел {tittlenamemenu} находится в проработке.</h2>

    <q>Можете воспользоваться другими функциями бота</q>

    <ul>
        <li><strong>Раздел {tittlenamemenu}:</strong> {description} </li>
    </ul>
    
</body>
"""