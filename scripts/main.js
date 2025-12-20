const lessons = ["ispis"];

function get_lessons() {
    lessons.forEach((lesson) => {
        if (Cookies.get(lesson) === "da") {
            document.getElementById(lesson).checked = true;
        }
    });
}

function check_section(section) {
    if (Cookies.get(section) === "da") {
        Cookies.remove(section);
    } else {
        Cookies.set(section, "da");
    }
}

get_lessons();
