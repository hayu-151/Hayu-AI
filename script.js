function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    let userMessage = document.createElement("p");
    userMessage.textContent = message;
    userMessage.className = "user-message";

    chatBox.appendChild(userMessage);

    input.value = "";
}