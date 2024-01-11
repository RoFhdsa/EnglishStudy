import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

#from qures.orm import SyncORM
#from Menu.orm_menu import MenuORM
#MenuORM.create_tables()
#MenuORM.insert_menu()
from Menu.MenuTGbot import MenuTGbot, CreateMenu

#MenuTGbot = MenuTGbot()
CreateMenu(isCreate=True)



"""SyncORM.create_tables()
SyncORM.insert_tables()
SyncORM.select_tables()
SyncORM.update_tables()
SyncORM.insert_tables_ResumeOrm()
sdsd
"""