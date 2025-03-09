let messages = [];

function sendMessage() {
    let input = document.getElementById("userInput").value;
    fetch(`http://127.0.0.1:8000/chat/?user_input=${input}`)
        .then(response => response.json())
        .then(data => {
            // Mesajları güncelle
            messages.push({ sender: "You", text: input });
            messages.push({ sender: "Bot", text: data.response });

            // HTML kısmını güncelle
            document.getElementById("chatbox").innerHTML = '';
            messages.forEach(message => {
                document.getElementById("chatbox").innerHTML += `<p><b>${message.sender}:</b> ${message.text}</p>`;
            });
        });
}
