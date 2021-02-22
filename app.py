#! python3.9
import eel, json, secrets, os, sys
from tinydb import TinyDB, Query
from dotenv import load_dotenv # python package for loading env file
load_dotenv()



os.path.join(os.environ["HOMEPATH"], "Desktop")
# Quick Setup -------

#if os.path.exists(os.path.join(os.environ["HOMEPATH"], "gE_Ode")) == False:
#    os.system('mkdir ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode"))
#if os.path.exists("D://gE_Ode") == False:
#    os.system('mkdir "D://gE_Ode"')
if os.path.exists(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash")) == False:
    os.system('mkdir ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash"))
if os.path.exists("D://gE_Ode/monster_mash") == False:
    os.system('mkdir "D://gE_Ode/monster_mash"')
if os.path.exists(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash")) == False:
    os.system("cd " + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash") + " && git clone https://github.com/Andyroid0/project_Monster_mash.git")
#--------------


#=====================================================================
#                           Variables
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


queryenv = []
scrumlistenv = []
caughtid = []

#----------------------------------------------------------------------


eel.init('web')

@eel.expose
def git_push_all():
    token = os.environ.get("gTokenvar") #Grabs variable from env file
    os.system('cd ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash") + ' && git add -A')
    os.system('cd ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash") + ' && git commit -m "Revision"')
    os.system("cd " + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash") + " && git push https://andyroid0:" + token + "@github.com/Andyroid0/project_Monster_mash.git --all")
    os.system('Robocopy /MIR  ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash") + ' D://gE_Ode/monster_mash/project_Monster_mash')
    eel.hide_Spinner()

@eel.expose
def git_pull():
    os.system('cd ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash") + ' && git pull')
    eel.hide_Spinner()

@eel.expose
def open_code_editor():
    os.system('cd ' + os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash") + ' && code .')







#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#-----------------------------------------------------------------------
#                   Task Object Creation and Deletion --Scrum
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def save_to_db(n):
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    #returnvalues = json.loads(n)
    #db.insert(task)
    taskobjectID = secrets.token_hex(25)
    taskstring = (n)
    tasklist = taskstring.split('..,|,..')
    tsksub = tasklist[0]
    tskdesc = tasklist[1]
    print("worked")
    scrumb.insert({"id": taskobjectID, "subject": tsksub, "description": tskdesc, "list": "tasktabletodo"})

@eel.expose
def object_pitcher():
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    envelope = []
    for item in scrumb:
        envelope.append(item['id'])
        envelope.append(item['subject'])
        envelope.append(item['list'])
    envstr = '..,|,..'.join(envelope)
    return envstr





#------------------------------------------------------------------------

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#------------------------------------------------------------------------    
#              Query Functions for Taskclick Modal - Scrum
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def taskobject_id_catcher(n):
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    thisguy = n
    query_by_id(thisguy)

def query_by_id(n):
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    if len(queryenv) > 0:
        queryenv.pop()
    query = scrumb.get(Query().id == n)
    qsub = query['subject']
    qdesc = query['description']
    qlist = query['list']
    qpack = qsub + "..,|,.." + qdesc + "..,|,.." + qlist
    queryenv.append(qpack)
    eel.query_trigger()


@eel.expose
def query_pitcher():
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    envstr = queryenv[0]
    return envstr

#------------------------------------------------------------------------

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#------------------------------------------------------------------------    
#              Taskobject dragndrop change List - Scrum
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def list_change_id_catcher(n):
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    thisguy = n
    query_list_change(thisguy)

#need id of taskobject

def query_list_change(n):
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    containera = n.split('..,|,..')
    if len(scrumlistenv) > 0:
        scrumlistenv.pop()
    if len(queryenv) > 0:
        queryenv.pop()
    query = scrumb.update({'list': containera[1]}, Query().id == containera[0])



#-------------------------------------------------------------------------

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#-------------------------------------------------------------------------


eel.start('main.html', mode='chrome',block=False)



@eel.expose # decorator that makes this python function callable in javascript
def task_button():
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb') 
    eel.form_fetch()(save_to_db) # Javascript function with python function in argument, said function grabs value returned from javascript side and saves to database


@eel.expose
def id_exchange_button():
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    eel.taskobject_id_pitcher()(taskobject_id_catcher)

@eel.expose
def list_exchange_button():
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    eel.listchange_pitcher()(list_change_id_catcher)

@eel.expose
def task_remover_trigger():
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    eel.task_remover_pitcher()(task_remover)
    

@eel.expose
def task_remover(n):
    db = TinyDB(os.path.join(os.environ["HOMEPATH"], "gE_Ode", "monster_mash", "project_Monster_mash", "Monster_mash", "scrum", "db.json"))
    scrumb = db.table('scrumb')
    scrumb.remove(Query().subject == n)



while True:
   eel.sleep(1.0)