const socket = io();

socket.on('message', function(msg) {
    const chat = document.getElementById('chat');
    const messageElement = document.createElement('div');
    messageElement.innerText = msg;
    chat.appendChild(messageElement);
});

function sendMessage() {
    const messageInput = document.getElementById('message');
    const message = messageInput.value;
    socket.send(message);
    messageInput.value = '';
}
