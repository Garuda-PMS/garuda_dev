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

function toggleInputOutputLabels(input_display, output_display) {
    let input_objective_name = document.getElementById('input-objective-name');
    let input_objective_description = document.getElementById('input-objective-description');
    let input_objective_status = document.getElementById('input-objective-status');
    let input_objective_type = document.getElementById('input-objective-type');
    let input_objective_deadline = document.getElementById('input-objective-deadline');

    let output_objective_name = document.getElementById('output-objective-name');
    let output_objective_description = document.getElementById('output-objective-description');
    let output_objective_status = document.getElementById('output-objective-status');
    let output_objective_deadline = document.getElementById('output-objective-deadline');
    let output_objective_assignee_id = document.getElementById('output-objective-assignee');
    let output_objective_type = document.getElementById('output-objective-type');

    input_objective_name.style.display = input_display;
    input_objective_description.style.display = input_display;
    input_objective_type.style.display = input_display;
    input_objective_status.style.display = input_display;
    input_objective_deadline.style.display = input_display;

    output_objective_name.style.display = output_display;
    output_objective_description.style.display = output_display;
    output_objective_type.style.display = output_display;
    output_objective_status.style.display = output_display;
    output_objective_deadline.style.display = output_display;
    output_objective_assignee_id.style.display = output_display;
    document.getElementById('label-assignee').style.display = output_display;
    document.getElementById('save-button').style.display = input_display;
    //document.getElementById('edit-button').style.display = output_display;
}

function setOutputContents(title, description, type, status, deadline, assignee_id) {

    let output_objective_name = document.getElementById('output-objective-name');
    let output_objective_description = document.getElementById('output-objective-description');
    let output_objective_deadline = document.getElementById('output-objective-deadline');
    let output_objective_status = document.getElementById('output-objective-status');
    let output_objective_assignee_id = document.getElementById('output-objective-assignee');
    let output_objective_type = document.getElementById('output-objective-type');

    output_objective_name.innerHTML = "<p>" + title + "</p>";
    output_objective_description.innerHTML = "<p>" + description + "</p>";
    output_objective_type.innerHTML = "<p>" + type + "</p>";
    output_objective_status.innerHTML = "<p>" + status + "</p>";
    output_objective_deadline.innerHTML = "<p>" + deadline + "</p>";
    output_objective_assignee_id.innerHTML = "<p>" + assignee_id + "</p>";
}

function renderTask(){
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

function createTask() {
    renderTask();
    toggleInputOutputLabels('inherit', 'none');
}

function viewTask(title, description, type, status, deadline, assignee_id) {
    renderTask();
    toggleInputOutputLabels('none', 'inherit');
    setOutputContents(title, description, type, status, deadline, assignee_id);
}

function saveTask(user_id){

    var saveTaskURL = "/task/create";
    const xmlhttp = new XMLHttpRequest();
    const objectiveName = document.getElementById("input-objective-name");
    const objectiveType = document.getElementById('input-objective-type');
    const objectiveStatus = document.getElementById("input-objective-status");
    const objectiveDescription = document.getElementById('input-objective-description');
    const objectiveDeadline = document.getElementById('input-objective-deadline');

    type = objectiveType.value;

    let task_params = {
        'title': objectiveName.value, 
        'status': objectiveStatus.value, 
        'description': objectiveDescription.value
    };

    switch(type) {
        case 'task': task_params['assignee_id'] = user_id; 
                     task_params['deadline'] = deadline;
                     break;
        case 'story': saveTaskURL = "/story/create"; break;
        case 'epic': saveTaskURL = "/epic/create"; break;
    }

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
