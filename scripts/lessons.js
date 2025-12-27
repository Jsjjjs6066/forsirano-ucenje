function completeLesson(lesson) {
    localStorage.setItem(lesson, "da");
    location.href = "../../index.html";
}

function table() {
    let arr = Array.from(document.getElementsByTagName("table"));
    arr.forEach((val, i, a) => {
        val.firstElementChild.firstElementChild.firstElementChild.style.borderTopLeftRadius = "10px";
        val.firstElementChild.firstElementChild.lastElementChild.style.borderTopRightRadius = "10px";
        val.firstElementChild.lastElementChild.firstElementChild.style.borderBottomLeftRadius = "10px";
        val.firstElementChild.lastElementChild.lastElementChild.style.borderBottomRightRadius = "10px";
    });
}