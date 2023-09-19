        // Function to hide messages after 2 seconds
setTimeout(function() {
    console.log("Timeout function executed.");
    var messages = document.querySelectorAll('.alertbox');
    messages.forEach(function(message) {
        message.style.visibility = 'hidden';
    });
}, 2000); // 2000 milliseconds = 2 seconds