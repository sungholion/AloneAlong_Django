const place = document.querySelector("#map_popup");
const popup = document.getElementById("popup")

function showRocation(){
    popup.classList.remove("hidden");
}

place.addEventListener("click",showRocation)