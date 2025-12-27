const primaryColor = getComputedStyle(document.documentElement).getPropertyValue("--primary-color");
const sectionColor = getComputedStyle(document.documentElement).getPropertyValue("--section-color");
const triColor = getComputedStyle(document.documentElement).getPropertyValue("--tri-color");
const backgroundColor = getComputedStyle(document.documentElement).getPropertyValue("--background-color");
const textColor = getComputedStyle(document.documentElement).getPropertyValue("--text-color");
const completeButtonColor = getComputedStyle(document.documentElement).getPropertyValue("--complete-button-color");
const pure = getComputedStyle(document.documentElement).getPropertyValue("--pure");
const pureInverted = getComputedStyle(document.documentElement).getPropertyValue("--pure-inverted");

class HoverableCode extends HTMLElement {
    constructor() {
        super();
        this.originalText = '';
        this.enterText = '';
    }

    static get observedAttributes() {
        return ['enter'];
    }

    connectedCallback() {
        // Wait for the parser to create the children
        setTimeout(() => {
            if (!this.originalText) {
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
        this.style.minWidth = String(this.clientWidth-10) + 'px';
        this.style.minHeight = String(this.clientHeight-10) + 'px';
    }
}

customElements.define('hoverable-code', HoverableCode);

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
    console.log(hoverableCodes);
    for (let i = 0; i < hoverableCodes.length; i++) {
        hoverableCodes[i].style.minWidth = String(hoverableCodes[i].clientWidth - 10) + 'px';
        hoverableCodes[i].style.minHeight = String(hoverableCodes[i].clientHeight - 10) + 'px';
    }

    let tables = Array.from(document.getElementsByTagName("table"));
    tables.forEach((val, i, a) => {
        val.firstElementChild.firstElementChild.firstElementChild.style.borderTopLeftRadius = "10px";
        val.firstElementChild.firstElementChild.lastElementChild.style.borderTopRightRadius = "10px";
        val.firstElementChild.lastElementChild.firstElementChild.style.borderBottomLeftRadius = "10px";
        val.firstElementChild.lastElementChild.lastElementChild.style.borderBottomRightRadius = "10px";
    });
}