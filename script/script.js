document.addEventListener("DOMContentLoaded", function () {
    const speakerForm = document.getElementById("speakerForm");
    const meetingForm = document.getElementById("meetingForm");

    if (speakerForm) {
        speakerForm.addEventListener("submit", addspeaker);
    }
    if (meetingForm) {
        meetingForm.addEventListener("submit", addmeeting);
    }
});

function loadTemplate(templatePath, replacements) {
    return fetch(templatePath)
        .then(response => response.text())
        .then(template => {
            Object.keys(replacements).forEach(key => {
                template = template.replace(`[${key}]`, replacements[key]);
            });
            return template;
        });
}

function saveFile(filename, content) {
    const blob = new Blob([content], { type: "text/html" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function createspeakerpage(name, bio, agendaFile) {
    const filename = `speaker/${name.replace(" ", "_").toLowerCase()}.html`;
    const replacements = {
        "speaker Name": name,
        "Background": bio,
        "speaker_name_agenda": `agendas/${agendaFile}`
    };

    loadTemplate("speaker/speaker_template.html", replacements)
        .then(content => saveFile(filename, content));

    updatespeakerList(name);
}

function createMeetingPage(date, speakerName, agendaFile) {
    const filename = `meeting/meeting_${date.replace("-", "_")}.html`;
    const replacements = {
        "Month Year": date,
        "speaker Name": speakerName,
        "speaker_name_agenda": `agendas/${agendaFile}`
    };

    loadTemplate("meeting/meeting_template.html", replacements)
        .then(content => saveFile(filename, content));

    updateMeetingList(date, speakerName);
}

function updatespeakerList(name) {
    const speakerList = document.getElementById("speakerList");
    if (speakerList) {
        const newEntry = document.createElement("li");
        newEntry.innerHTML = `<a href="speakers/${name.replace(" ", "_").toLowerCase()}.html">${name}</a>`;
        speakerList.appendChild(newEntry);
    }
}

function updatemeetingList(date, speakerName) {
    const meetingList = document.getElementById("meetingList");
    if (meetingList) {
        const newEntry = document.createElement("li");
        newEntry.innerHTML = `meeting Date ${date}: <a href="meeting/meeting_${date.replace("-", "_")}.html">${speakerName}'s Summary</a>`;
        meetingList.appendChild(newEntry);
    }
}

function saveFile(filename, content) {
    const blob = new Blob([content], { type: "text/html" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}