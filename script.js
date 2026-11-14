
async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const language = document.getElementById("language").value;
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
        const response = await fetch(
            "https://hayu-ai.onrender.com/chat",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message,
                    language: language
                })
            }
        );

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();
        botMessage.textContent = data.reply;

    } catch (error) {
        botMessage.textContent =
            "Dhiifama! Server waliin wal qunnamuu hin dandeenye.";
    }
}
