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

function saveTask(){

    var objectiveName = document.getElementById("objective-name").value;
    var objectiveStatus = document.getElementById("objective-status");
    document.getElementById(objectiveStatus.value).innerHTML += `
    <div class="objective" id="${objectiveName.toLowerCase().split(" ").join("")}" draggable="true" ondragstart="drag(event)" ondrop="dropObjective(event)">
        <span>${objectiveName}</span>
    </div>
    `
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
