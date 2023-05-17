window.addEventListener('DOMContentLoaded', function() {
    loadRandomQuote();
  });

function likeQuote() {
// Prepare the data to send to the backend
var quoteData = {
    quote: document.getElementById('quote').innerText,
    author: document.getElementById('author').innerText
};
// Send the data to the backend
fetch('/like_quote', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify(quoteData)
})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data && data.success) {
            // Liked quote successfully stored
            alert('Quote liked and stored in the database!');
            // Update the input value with the liked quote
            document.getElementById('myquote').value = quoteData.quote;
        } else {
            // Failed to store the liked quote
            alert('Failed to store the liked quote.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
