
async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const message = input.value.trim();

    if (!message) return;

    const userMessage = document.createElement("p");
    userMessage.textContent = message;
    userMessage.className = "user-message";
    chatBox.appendChild(userMessage);

    input.value = "";

    const botMessage = document.createElement("p");
    botMessage.className = "bot-message";
    botMessage.textContent = "Hayu AI deebii qopheessaa jira...";
    chatBox.appendChild(botMessage);

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        if (!response.ok) {
            throw new Error("Server hin hojjenne");
        }

        const data = await response.json();
        botMessage.textContent = data.reply;

    } catch (error) {
        botMessage.textContent =
            "Dhiifama! Server Hayu AI waliin wal qunnamuu hin dandeenye.";
    }
}
