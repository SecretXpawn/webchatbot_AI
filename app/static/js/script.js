document.addEventListener('DOMContentLoaded', function() {
    var messageInput = document.getElementById('message-input');
    var chatBox = document.getElementById('chat-box');
    var messageForm = document.getElementById('message-form');
    messageForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
        var message = messageInput.value.trim();
        messageInput.value = '';
        displayMessage('user', message);
    });
    function displayMessage(role, content) {
        var messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.classList.add(role);
        messageElement.textContent = content;
        chatBox.appendChild(messageElement);
    }
});
