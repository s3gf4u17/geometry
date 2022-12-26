export class MyWindow{
    constructor(title,contents){
        try{
            document.getElementById("window").remove();
        }catch(e){}
        const win = document.createElement("div");
        win.classList.add("window");
        win.id = "window";
        document.body.appendChild(win);

        const head = document.createElement("div");
        head.classList.add("window-header")
        win.appendChild(head);
        head.id = "window-header";

        const headTitle = document.createElement("div");
        headTitle.classList.add("window-title");
        headTitle.innerHTML = title;
        head.appendChild(headTitle);
        headTitle.addEventListener("click",()=>{win.remove()})
        
        win.appendChild(contents);
        this.dragElement(win);
    }
    dragElement(elmnt) {
        var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
        if (document.getElementById("window-header")) {
          // if present, the header is where you move the DIV from:
          document.getElementById("window-header").onmousedown = dragMouseDown;
        } else {
          // otherwise, move the DIV from anywhere inside the DIV:
          elmnt.onmousedown = dragMouseDown;
        }
      
        function dragMouseDown(e) {
          e = e || window.event;
          e.preventDefault();
          // get the mouse cursor position at startup:
          pos3 = e.clientX;
          pos4 = e.clientY;
          document.onmouseup = closeDragElement;
          // call a function whenever the cursor moves:
          document.onmousemove = elementDrag;
        }
      
        function elementDrag(e) {
          e = e || window.event;
          e.preventDefault();
          // calculate the new cursor position:
          pos1 = pos3 - e.clientX;
          pos2 = pos4 - e.clientY;
          pos3 = e.clientX;
          pos4 = e.clientY;
          // set the element's new position:
          elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
          elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
        }
      
        function closeDragElement() {
          // stop moving when mouse button is released:
          document.onmouseup = null;
          document.onmousemove = null;
        }
      }
}