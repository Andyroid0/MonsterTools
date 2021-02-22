
//-------------------------------------------------------
//              Variables
// ------------------------------------------------------
var subjectsobj = [];
var caughtid = [];
scrumlistenv = [];
// ------------------------------------------------------


function console_test()
{
    console.log("she works friend")

}

eel.expose(show_Spinner)
function show_Spinner()
{
    var spinner_object = document.getElementById('spinner')
    spinner_object.setAttribute("class", "spinner-border text-danger buttonsmargin"); 
}

eel.expose(hide_Spinner)
function hide_Spinner()
{ 
    
    var spinner_object = document.getElementById('spinner')
    spinner_object.setAttribute("class", "spinner-border text-danger buttonsmargin visually-hidden") 
            
}




//=============================================================================
//|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
//=============================================================================

//                      Task Click and modal Expose
//-----------------------------------------------------------------------------



eel.expose(taskobject_id_pitcher) // is capable of sending data to python 
function taskobject_id_pitcher()
{
    console.log(caughtid)
    return caughtid[0]
}

eel.expose(taskobject_id_grabber)
function taskobject_id_grabber(id)
{ //works
    caughtid.pop()
    caughtid.push(id)
    console.log('durango')
    eel.id_exchange_button()
}

function query_catcher(n)
{ // Information that is collected
    querylist = n.split('..,|,..')
    console.log("We've got the stuff: " + querylist)
    qdata_insertion()
}

eel.expose(query_trigger)
function query_trigger()
{
    eel.query_pitcher()(query_catcher)
}

function qdata_insertion()
{ // Information that is injected into the modal
    var qsubnode = document.getElementById("subjectdet")
    var qdescnode = document.getElementById("descriptiondet")
    //var qlistnode = document.getElementById("listdet")
    qsubnode.innerHTML = querylist[0]
    qdescnode.innerHTML = querylist[1]
}

eel.expose(task_remover_pitcher)
function task_remover_pitcher()
{
    var subjectpitch = querylist[0]
    return subjectpitch
}
//=============================================================================
//|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
//=============================================================================

//                      Taskobject Creation
//-----------------------------------------------------------------------------



eel.expose(form_fetch)
function form_fetch()
{ 
    var taskobjsub = document.getElementById("sub1").value;
    var taskobjdesc = document.getElementById("desc1").value;
    return taskobjsub + '..,|,..' + taskobjdesc;    
}


eel.expose(object_catcher)
function object_catcher(n)
{
    objdata = (n)
    objlist = objdata.split('..,|,..')
    howmanyarrays = objlist.length / 3
    var iterarray = []
    iterarray.length = howmanyarrays
    var i = 0
    var looper = function(){
        while (i < howmanyarrays){
            var arraycontainer = objlist.splice(0, 3)
            var tasktableitem = document.createElement("div");
            tasktableitem.setAttribute("class", "card bg-secondary cardmargin")
            tasktableitem.setAttribute("onclick", "taskobject_id_grabber(this.id)")
            tasktableitem.setAttribute("data-toggle", "modal")
            tasktableitem.setAttribute("data-target", "#modaltaskobjectdetails")
            tasktableitem.setAttribute("id", arraycontainer[0])
            tasktableitem.innerHTML = '<div class="card-body">' + arraycontainer[1] +'</div>';

            //tasktableitem.innerHTML = '<li class="list-group-item"><button class="btn btn-primary btn-lg" onclick="taskobject_id_grabber(this.id)" data-toggle="modal" data-target="#modaltaskobjectdetails" id="' + arraycontainer[0] + '">'
            // + arraycontainer[1] + '</button></li>';
            //tasktableitem.setAttribute("class", "list-group-item")
            //tasktableitem.setAttribute("id", arraycontainer[0] + "line") // ID number set by python secrets module
            tasktableitem.setAttribute("draggable", "true")
            tasktableitem.setAttribute("ondragstart", "onDragStart(event)")
            tasktableitem.setAttribute("ondrop", "false")
            document.getElementById(arraycontainer[2]).appendChild(tasktableitem);
            i++
        }

    }
    looper()    
}

//=============================================================================
//|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
//=============================================================================

//                      Drag and Drop functionality
//-----------------------------------------------------------------------------

function onDragStart(event)
{
    event
        .dataTransfer
        .setData('text/plain', event.target.id)
}


function onDragover(ever)
{
    event.preventDefault()
}


function onDrop(event, el)
{
    const id = event
        .dataTransfer
        .getData('text');

    const draggableElement = document.getElementById(id)
    const dropzone = event.target
    var idrev = id.split('line')
    caughtid.pop()
    caughtid.push(idrev[0])
    el.appendChild(draggableElement)
    event
        .dataTransfer
        .clearData()
}


function column_identifier(id)
{
    scrumlistenv.pop()
    scrumlistenv.push(id)
    eel.list_exchange_button()
}

eel.expose(listchange_pitcher) // is capable of sending data to python 
function listchange_pitcher()
{
    var infopacket = caughtid[0] + "..,|,.." + scrumlistenv
    return infopacket
}