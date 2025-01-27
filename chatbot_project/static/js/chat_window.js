// DOM Elements

const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const academicCalendarBtn = document.getElementById('academic-calendar-btn');


// Function to append messages to the chat window
// Function to append messages to the chat window
function appendMessage(content, className) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = content;  // Ensure you're using textContent to avoid rendering HTML
    messageDiv.classList.add('message', className);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}
function sendMessageToBackendMongo(userMessage) {
    let url = `/query_bus/?message=${encodeURIComponent(userMessage)}`;
    console.log("Requesting URL:", url);  // Log the request URL
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log("Success:", data);
            let resultHTML = '';
            if (data.status === 'success') {
                resultHTML = `${data.data.message}`;
            } else {
                resultHTML = `${data.message}`;
            }
            appendMessage(resultHTML, 'bot-message');
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('Error occurred. Please try again later.', 'bot-message');
        });
}


/*
/earlier correct code
// Function to handle sending user input to the backend and displaying the response
function sendMessageToBackendMongo(userMessage) {
    // Build the query URL for the backend
    let url = `/query_bus/?message=${encodeURIComponent(userMessage)}`;

    console.log("Requesting URL:", url);  // Log the request URL to check what is being sent

    // Send the query to the backend using Fetch API
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log("Success:", data);

            // Handle the response
            let resultHTML = '';
            if (data.status === 'success') {
                // If there's a relevant message in the response
                if (data.data && data.data.message) {
                    resultHTML = `${data.data.message}`;
                }
            } else {
                // If there was an error (e.g., no bus found or no fee found)
                resultHTML = `${data.message}`;
            }
            // Display the result in the chat window
            appendMessage(resultHTML, 'bot-message');
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('Error occurred. Please try again later.', 'bot-message');
        });
}
        */
// Handle user message submission
function handleSendMessage() {
    const userMessage = messageInput.value.trim();
    console.log('The user message is', userMessage);

    if (userMessage) {
        appendMessage(userMessage, 'user-message');
        sendMessageToBackendMongo(userMessage);  // Send message to backend
        messageInput.value = '';  // Clear input
    }
}
  // Open Academic Calendar
  academicCalendarBtn.addEventListener('click', () => {
    window.open('assets/academic_calender.pdf', '_blank');
});


// Event Listeners
sendButton.addEventListener('click', handleSendMessage);
messageInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        handleSendMessage();
    }
});





