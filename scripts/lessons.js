const primaryColor = getComputedStyle(document.documentElement).getPropertyValue("--primary-color");
const sectionColor = getComputedStyle(document.documentElement).getPropertyValue("--section-color");
const triColor = getComputedStyle(document.documentElement).getPropertyValue("--tri-color");
const backgroundColor = getComputedStyle(document.documentElement).getPropertyValue("--background-color");
const textColor = getComputedStyle(document.documentElement).getPropertyValue("--text-color");
const completeButtonColor = getComputedStyle(document.documentElement).getPropertyValue("--complete-button-color");
const pure = getComputedStyle(document.documentElement).getPropertyValue("--pure");
const pureInverted = getComputedStyle(document.documentElement).getPropertyValue("--pure-inverted");
const secondaryColor = getComputedStyle(document.documentElement).getPropertyValue("--secondary-color");

class HoverableCode extends HTMLElement {
    constructor() {
        super();
        this.originalText = '';
        this.enterText = '';
        this.color = '';
    }

    static get observedAttributes() {
        return ['enter', 'color'];
    }

    connectedCallback() {
        // Wait for the parser to create the children
        setTimeout(() => {
            if (!this.originalText) {
                this.style.color = this.color;
                this.style.borderColor = this.color;
                this.originalText = this.innerHTML;
                this.render();
                this.addEventListeners();
            }
        });
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (name === 'enter' && oldValue !== newValue) {
            this.enterText = newValue;
        }
        if (name === 'color' && oldValue !== newValue) {
            this.color = newValue;
        }
    }

    addEventListeners() {
        this.addEventListener('mouseover', () => {
            this.innerHTML = this.enterText || this.originalText;
        });

        this.addEventListener('mouseleave', () => {
            this.innerHTML = this.originalText;
        });
    }

    render() {
        this.classList.add('hoverable-code');
        // Ensure content is set (though it should be already if we read it from innerHTML)
        if (this.innerHTML !== this.originalText) {
            this.innerHTML = this.originalText;
        }
        this.style.minWidth = String(this.clientWidth - 10) + 'px';
        this.style.minHeight = String(this.clientHeight - 10) + 'px';
    }
}

class Explainer extends HTMLElement {
    constructor() {
        super();
        this.target;
        this.infos;
    }

    setCallbacks(element) {
        element.addEventListener('mouseover', () => {
            let siblings = element.parentNode.children;
            for (let i = 0; i < siblings.length; i++) {
                if (siblings[i] == element) {
                    continue;
                }
                siblings[i].style.color = 'transparent';
                siblings[i].style.backgroundColor = 'transparent';
            }
            let c = document.createElement('div');
            c.innerText = element.content;
            c.id = 'info-content';
            c.style.color = element.color;
            c.style.paddingLeft = '10px';
            element.after(c);
        });
        element.addEventListener('mouseleave', () => {
            let siblings = element.parentNode.children;
            let infoI = 0;
            for (let i = 0; i < siblings.length; i++) {
                if (siblings[i] == element) {
                    infoI++;
                    continue;
                }
                if (siblings[i].className != 'info') {
                    continue;
                }
                let color = this.infos[infoI].color;
                if (color == '') {
                    color = primaryColor;
                }
                siblings[i].style.color = color;
                siblings[i].style.backgroundColor = color;
                infoI++;
            }
            document.getElementById('info-content').remove();
        });
    }

    connectedCallback() {
        setTimeout(() => {
            this.target = this.previousElementSibling;
            while (this.target) {
                if (this.target.tagName.toLowerCase() == 'pre') {
                    break;
                }
                this.target = this.target.previousElementSibling;
            }
            this.render();
        });
    }

    render() {
        this.className = 'explainer-cont';
        let infos = Array.from(this.getElementsByTagName('explainer-info'));
        infos.forEach((info) => {
            info.content = info.innerHTML;
        });
        infos.sort((a, b) => {
            return a.pos - b.pos;
        });
        this.infos = infos;

        this.innerHTML = '';


        if (infos.length == 0) {
            return;
        }

        let prevInfo = infos[0];
        let margin = document.createElement('div');
        margin.className = 'margin';
        margin.innerText = this.target.innerText.split("\n").findLast((e) => e.length > 0).slice(0, Number(prevInfo.pos));
        this.appendChild(margin);
        let code = document.createElement('div');
        code.className = 'info'
        if (prevInfo.color == "") {
            prevInfo.color = primaryColor;
        }
        code.style.color = prevInfo.color;
        code.style.backgroundColor = prevInfo.color;
        code.innerText = this.target.innerText.split("\n").findLast((e) => e.length > 0).slice(Number(prevInfo.pos), Number(prevInfo.pos) + Number(prevInfo.size));
        code.content = prevInfo.content;
        code.color = prevInfo.color;
        code.style.marginLeft = String(prevInfo.additionalPadding) + 'px';
        this.appendChild(code);
        this.setCallbacks(code);
        for (let i = 1; i < infos.length; i++) {
            let info = infos[i];
            let margin = document.createElement('div');
            margin.className = 'margin';
            margin.innerText = this.target.innerText.split("\n").findLast((e) => e.length > 0).slice(Number(prevInfo.pos) + Number(prevInfo.size), Number(info.pos));
            this.appendChild(margin);
            let code = document.createElement('div');
            code.className = 'info';
            if (info.color == "") {
                info.color = primaryColor;
            }
            code.style.color = info.color;
            code.style.backgroundColor = info.color;
            code.innerText = this.target.innerText.split("\n").findLast((e) => e.length > 0).slice(Number(info.pos), Number(info.pos) + Number(info.size));
            code.content = info.content;
            code.color = info.color;
            code.style.marginLeft = String(info.additionalPadding) + 'px';
            this.appendChild(code);
            this.setCallbacks(code);
            prevInfo = info;
        }
    }
}

class ExplainerInfo extends HTMLElement {
    constructor() {
        super();
        this.color = '';
        this.pos = 0;
        this.size = 0;
        this.content = '';
        this.additionalPadding = 0;
    }

    static get observedAttributes() {
        return ['color', 'pos', 'size', 'hc-paddings'];
    }

    connectedCallback() {
        // Wait for the parser to create the children
        setTimeout(() => {
            this.content = this.innerHTML;
        });
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (name === 'color' && oldValue !== newValue) {
            this.color = newValue;
        }
        if (name === 'pos' && oldValue !== newValue) {
            this.pos = newValue;
        }
        if (name === 'size' && oldValue !== newValue) {
            this.size = newValue;
        }
        if (name === 'hc-paddings' && oldValue !== newValue) {
            this.additionalPadding = Number(newValue) * 6.67;
        }
    }
}

customElements.define('hoverable-code', HoverableCode);
customElements.define('explainer-cont', Explainer);
customElements.define('explainer-info', ExplainerInfo);

function completeLesson(lesson) {
    localStorage.setItem(lesson, "da");
    location.href = "../../index.html";
}

function main() {
    let invis = document.getElementsByClassName("invis");
    for (let i = 0; i < invis.length; i++) {
        invis[i].onclick = (e) => {
            if (e.target.seen) {
                e.target.style.color = pure;
                e.target.seen = false;
            }
            else {
                e.target.style.color = textColor;
                e.target.seen = true;
            }
        };
    }

    let hoverableCodes = document.getElementsByClassName("hoverable-code");
    for (let i = 0; i < hoverableCodes.length; i++) {
        hoverableCodes[i].style.minWidth = String(hoverableCodes[i].clientWidth - 10) + 'px';
        hoverableCodes[i].style.minHeight = String(hoverableCodes[i].clientHeight - 10) + 'px';
    }

    let tables = Array.from(document.getElementsByTagName("table"));
    tables.forEach((val, i, a) => {
        val.firstElementChild.firstElementChild.firstElementChild.style.borderTopLeftRadius = "10px";
        val.firstElementChild.firstElementChild.lastElementChild.style.borderTopRightRadius = "10px";
        val.lastElementChild.lastElementChild.firstElementChild.style.borderBottomLeftRadius = "10px";
        val.lastElementChild.lastElementChild.lastElementChild.style.borderBottomRightRadius = "10px";
    });

    let stare_gluposti = Array.from(document.querySelectorAll("p"));
    stare_gluposti.forEach((val, i, a) => {
        if (val.style.whiteSpace == 'pre-wrap') {
            val.style.fontFamily = "Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace";
            val.style.fontSize = "1.5em";
            val.style.paddingLeft = "2px";
            for (let line of val.innerText.split("\n")) {
                let newLine = "  " + line;
                val.innerText = val.innerText.replace(line, newLine);
            }
        }
    });
}