var windows = 0;
var saved = false;
var mapUrl = "";
var map = L.map('map',{minZoom:2,maxZoom:18,"zoomControl":false,"attributionControl":false}).setView([51.9189046,19.1343786],5);
var maplayer = null;
// L.control.scale({"position":"bottomleft"}).addTo(map);
// L.control.zoom({"position":"bottomright"}).addTo(map);
var serverUrl = "";
var httpSecurity = "http";

function setMapUrl(url){
    try{map.removeLayer(maplayer);}catch(error){}
    mapUrl = url;
    maplayer = L.tileLayer(mapUrl);
    maplayer.addTo(map);
}

function changeServerUrl(){
  serverUrl = document.getElementById('set1').value;
  document.getElementById('set1').style.borderColor = "red";
    fetch(httpSecurity+"://"+serverUrl+"/test").then((response) => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('Something went wrong');;
    })
    .then(() => {
      document.getElementById('set1').style.borderColor = "green";
    })
    .catch((error) => {
      console.log(error)
    });
}

function swapSecurity(){
  if (httpSecurity == "http") {httpSecurity = "https"}
  else {httpSecurity = "http"}
  document.getElementById('set1').style.borderColor = "red";
    fetch(httpSecurity+"://"+serverUrl+"/test").then((response) => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('Something went wrong');;
    })
    .then(() => {
      document.getElementById('set1').style.borderColor = "green";
    })
    .catch((error) => {
      console.log(error)
    });
}

async function createWindow(name,title){
    if (name=="server") {
      resp={
        content:"Ustawienie połączenia z serwerem FastAPI backendu GisPortalu:",
        form:"<input type='text' id='set1' placeholder='Adres IP/DNS serwera' onchange='changeServerUrl()'/><input type='checkbox' id='set1' name='settings' onclick='swapSecurity()'/><label for='set1'>Serwer Https</label></br>"
      }
    } else {
      resp = await fetch(httpSecurity+"://"+serverUrl+"/"+name).then((response)=>response.json()).then((data)=>{return data;});
    }
    // window
    const win = document.createElement("div");
    win.classList.add("window");
    win.id = "win"+windows;
    document.body.appendChild(win);

    // header
    const header = document.createElement("div");
    header.classList.add("window-header");
    header.id = "win"+windows+"header";
    win.appendChild(header);

    // close button
    const close = document.createElement("div");
    close.classList.add("main-bar-button");
    close.innerHTML = "<i class='fa-solid fa-circle-xmark'></i> Zamknij";
    close.addEventListener("click",function(){win.remove()})
    header.appendChild(close);

    // window title
    const ttl = document.createElement("div");
    ttl.classList.add("window-title");
    ttl.innerHTML = title;
    header.appendChild(ttl);

    // window content
    const content = document.createElement("div");
    content.classList.add("window-content");
    content.id = "win"+windows+"content";
    content.innerHTML = resp.content;
    win.appendChild(content);

    // window form
    const form = document.createElement("div");
    form.classList.add("window-form");
    form.innerHTML = resp.form;
    content.appendChild(form);

    // make window draggable
    dragElement(win);
    windows++;
}

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
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

function closeWindow(){
    document.getElementById("window").remove();
}