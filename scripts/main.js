const lessons = ["ispis", "varijable", "operatori", "string", "usporedjivanje", "if", "input", "liste-osnove"];

function get_lessons() {
    lessons.forEach((lesson) => {
        if (localStorage.getItem(lesson) === "da") {
            document.getElementById(lesson).checked = true;
        }
    });
}

function check_section(section) {
    if (localStorage.getItem(section) === "da") {
        localStorage.removeItem(section);
    } else {
        localStorage.setItem(section, "da");
    }
}

get_lessons();
