function envoyer() {
    fetch("http://localhost:5005", {
        method: "POST",
        body: JSON.stringify({
            titre: document.getElementById("titre").value,
            message: document.getElementById("message").value
        })
    });
}