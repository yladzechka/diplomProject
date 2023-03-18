function showPopup() {
    var popup = document.createElement("div");
    popup.classList.add("popup");
    popup.innerHTML = "Товар добавлен в корзину!";
    document.body.appendChild(popup);

    setTimeout(function() {
        document.body.removeChild(popup);
    }, 2000);
}

