function expand(event){
    var target = event.target.parentElement
    if (window.getComputedStyle(target).maxHeight === "29px"){
        target.style.maxHeight = "none";
    } else {
        target.style.maxHeight = "29px";
    }
}