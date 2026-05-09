document.getElementById('send-button').addEventListener('click', function() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;
    
    // Add question to chat window
    var chatWindow = document.getElementById('chat-window');
    var questionDiv = document.createElement('div');
    questionDiv.className = 'message question';
    questionDiv.textContent = userInput;
    chatWindow.appendChild(questionDiv);
    
    document.getElementById('user-input').value = '';
    
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        var answerDiv = document.createElement('div');
        answerDiv.className = 'message answer';
        answerDiv.textContent = data.answer;
        chatWindow.appendChild(answerDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    });
});
