window.addEventListener('DOMContentLoaded', function() {
    loadRandomQuote();
  });

// load a random quote from an API
function loadRandomQuote() {
  var xhttp = new XMLHttpRequest();
  const method = "GET";
  const url = "https://api.quotable.io/random";
  xhttp.open(method, url, true);

  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var apiQuotes = JSON.parse(this.responseText);
      var randomQuoteContent = apiQuotes.content;
      var randomQuoteAuthor = apiQuotes.author || "- Anonymous";
      var randomQuoteText =
        '<span><i class="ion-quote"></i></span> &nbsp; ' + randomQuoteContent;
      document.getElementById("quote").innerHTML = randomQuoteText;
      document.getElementById("author").innerHTML = "- " + randomQuoteAuthor;
    }
  };
  xhttp.send();
}

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

//Account information get edit and save btn
const editBtn = document.getElementById("edit-btn");
const saveBtn = document.getElementById("save-btn");
const inputElems = document.querySelectorAll("input[readonly]");
const selectElems = document.querySelectorAll("select[readonly]");

// toggle read-only
editBtn.addEventListener("click", function() {
  inputElems.forEach(function(elem) {
    elem.removeAttribute("readonly");
  });
  selectElems.forEach(function(elem) {
    elem.removeAttribute("readonly");
  });
});

saveBtn.addEventListener("click", function() {
  inputElems.forEach(function(elem) {
    elem.setAttribute("readonly", "");
  });
  selectElems.forEach(function(elem) {
    elem.setAttribute("readonly", "");
  });
});
