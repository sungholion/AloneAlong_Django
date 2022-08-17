
// heart btn 

const countHeart = document.querySelector("#heartBtn")


let count = 0;
let result = countHeart.innerText;
function counter() {
    if(count %2 == 0) {
        countHeart.classList.add("btn_clicked");
        result = parseInt(result)+1;
        console.log(result)
    } else {
        countHeart.classList.remove("btn_clicked");
        result = parseInt(result)-1;
    }
    count+=1;
   
}

countHeart.addEventListener("click",counter);