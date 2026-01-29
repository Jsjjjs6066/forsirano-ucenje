const lessons = ["ispis", "varijable", "operatori", "string", "usporedjivanje", "if", "input", "liste-osnove", "liste-elementi", "liste-dodavanje", "for-osnove", "for-napredno", "liste-zadatak"];
const version = "1-liste";
let last_version = version;

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

function update_version() {
    if (localStorage.getItem("version") !== version) {
        last_version = localStorage.getItem("version");
        localStorage.setItem("version", version);
    }
}

update_version();
get_lessons();
