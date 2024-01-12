from settingsDB import conn

class Settings ():
    def __init__(self):
        self.path = conn['MY_PATH']

    def DATABASE_URL(self):
        return f'sqlite:///{self.path}.db'

settings = Settings()
print(settings.DATABASE_URL())