// get user input and return chatbot response
const chatLog = document.getElementById('chat-log');
const messageInput = document.getElementById('message');
const chatForm = document.getElementById('chat-form');

chatForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    if (!message) {
        return;
    }

    addMessageToLog('You', message);

    fetch('/index', {
        method: 'POST',
        body: new URLSearchParams({
            'message': message
        })
    })
    .then(response => response.json())
    .then(data => {
        const response = data.response;
        addMessageToLog('Chatbot', response);
    })
    .catch(error => {
        console.error('Error:', error);
        addMessageToLog('Chatbot', 'Sorry, an error occurred. Let me take a rest, Human.');
    });

    messageInput.value = '';
});

function addMessageToLog(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.className = 'message ' + (sender === 'Chatbot' ? 'left' : 'right');
    messageElement.innerHTML = '<strong>' + sender + ':</strong> ' + message;
    const chatWindow = document.getElementById('chat-window');
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}