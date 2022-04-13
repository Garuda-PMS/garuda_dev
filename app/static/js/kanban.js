function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.currentTarget.appendChild(document.getElementById(data));
}

function createTask(){
    var space1 = document.getElementById("done");
    var space2 = document.getElementById("testing");
    var space3 = document.getElementById("closed");
    var objective_block = document.getElementById("create-new-objective-block");
    if (space1.style.display === "none") {
        space1.style.display = "block";
        space2.style.display = "block";
        space3.style.display = "block";
        objective_block.style.display = "none";
    } else {
        space1.style.display = "none";
        space2.style.display = "none";
        space3.style.display = "none";
        objective_block.style.display = "flex";
    }
}

function saveTask(user_id){

    const xmlhttp = new XMLHttpRequest();
    const saveTaskURL = "/task/create";
    const objectiveName = document.getElementById("objective-name");
    const objectiveStatus = document.getElementById("objective-status");
    const objectiveDescription = document.getElementById('objective-description');
    let task_params = {
        'assignee_id': user_id,
        'title': objectiveName.value, 
        'status': objectiveStatus.value, 
        'description': objectiveDescription.value
    };

    document.getElementById(objectiveStatus.value).innerHTML += `
    <div class="objective" id="${objectiveName.value.toLowerCase().split(" ").join("")}" draggable="true" ondragstart="drag(event)" ondrop="dropObjective(event)">
        <span>${objectiveName.value}</span>
    </div>
    `;

    xmlhttp.open('POST', saveTaskURL);
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(JSON.stringify(task_params));
}

function editTask(){
    var saveButton = document.getElementById("save-button");
    var editButton = document.getElementById("edit-button");
    if (saveButton.style.display === "none") {
        saveButton.style.display = "block";
        editButton.style.display = "none";
    } else{
        saveButton.style.display = "none";
        editButton.style.display = "block";
    }
}
