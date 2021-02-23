#! python3

import os

os.system('cd ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "MonsterTools") + ' && git pull')
os.system('python ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "MonsterTools", "app.py"))

