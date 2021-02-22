#! python3

import os

os.system('cd ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "MonsterTools") + ' && git pull')
os.system(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "MonsterTools", "output", "app", "app.exe"))


