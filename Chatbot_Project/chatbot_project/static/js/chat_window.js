// DOM Elements
/*const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

// Append message to chat
function appendMessage(content, className) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = content;
    messageDiv.classList.add('message', className);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}

// Handle user message submission
function handleSendMessage() {
    const userMessage = messageInput.value.trim();
    if (userMessage) {
        appendMessage(userMessage, 'user-message');
        setTimeout(() => {
            appendMessage(userMessage, 'bot-message');
        }, 500); // Simulate bot response delay
        messageInput.value = ''; // Clear input
    }
}

// Event Listeners
sendButton.addEventListener('click', handleSendMessage);
messageInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        handleSendMessage();
    }
});*/


// DOM Elements
const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

// Append message to chat
function appendMessage(content, className) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = content;
    messageDiv.classList.add('message', className);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}

// Send user message to Django backend for processing
function sendMessageToBackend(message) {
    console.log(`Sending message to backend: ${message}`);  // Debug: Log the message being sent
    // fetch is built-in JavaScript function that makes HTTP requests. Here its ends POST request to /get-semester
    fetch('/get-semester/', {  // Endpoint for processing the question.  In this case /get-semester it's assumed to be the backend API that processes the question related to the "semester"
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,  // CSRF Token for security
        },
        body: JSON.stringify({ question: message })
    })
    .then(response => response.json())
    .then(data => {
        // Process the bot response
        console.log(`Received reply from backend: ${data.reply}`);  // Debug: Log the reply from the backend
        if (data.reply) {
            appendMessage(data.reply, 'bot-message');
        } else {
            appendMessage('Sorry, I could not understand the question.', 'bot-message');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('Sorry, there was an error processing your request.', 'bot-message');
    });
}

// Handle user message submission
function handleSendMessage() {
    const userMessage = messageInput.value.trim();
    if (userMessage) {
        appendMessage(userMessage, 'user-message');
        sendMessageToBackend(userMessage);  // Send message to backend
        messageInput.value = '';  // Clear input
    }
}

// Event Listeners
sendButton.addEventListener('click', handleSendMessage);
messageInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        handleSendMessage();
    }
});
