document.addEventListener('DOMContentLoaded', function() {
    // Reference to the message input field
    var messageInput = document.getElementById('message-input');
    
    // Reference to the chat box
    var chatBox = document.getElementById('chat-box');

    // Reference to the message form
    var messageForm = document.getElementById('message-form');

    // Event listener for form submission
    messageForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        
        // Get the user's message from the input field
        var message = messageInput.value.trim();
        
        // Clear the input field
        messageInput.value = '';
        
        // Display the user's message in the chat box
        displayMessage('user', message);
    });

    // Function to display messages in the chat box
    function displayMessage(role, content) {
        var messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.classList.add(role);
        messageElement.textContent = content;
        chatBox.appendChild(messageElement);
    }
});
