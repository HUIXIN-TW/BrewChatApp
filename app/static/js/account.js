// Reference
// JavaScript library: jQuery
// Version: 3.6.0
// Source: https://code.jquery.com/jquery-3.6.0.min.js

/**
 * Description: JavaScript code for 
 * 1. load a random quote from an API
 * 2. Edit and save function
 * 3. Handle validation user input of day of birth
 * Author: HuiXin Yang & YunChuan Kung
 */

// window call loadRandomQuote function
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
const textElems = document.querySelectorAll("textarea[readonly]");

// toggle read-only
editBtn.addEventListener("click", function() {
  inputElems.forEach(function(elem) {
    elem.removeAttribute("readonly");
  });
  textElems.forEach(function(elem) {
    elem.removeAttribute("readonly");
  });
});

saveBtn.addEventListener("click", function() {
  inputElems.forEach(function(elem) {
    elem.setAttribute("readonly", "");
  });
  textElems.forEach(function(elem) {
    elem.setAttribute("readonly", "");
  });
});

//User input validation( birthday)
//Verify the user input date of birth is valid (should before today)
$(document).ready(function() {
  // Declare the variable without assigning a value
  var dobInput;

  // Retrieve the Date of Birth input element when the user inputs a value
  $('#dob-input').on('input', function() {
    // Assign the element to the dobInput variable
    dobInput = this;

    // Add an event listener to the input element to check the value on change
    dobInput.addEventListener('change', function() {
      // Parse the user input value as a Date object
      var dob = new Date(this.value);

      // Get the current date
      var today = new Date();
      today.setHours(0, 0, 0, 0); // Set the time to midnight to ignore the time component

      // Compare the year, month, and day values
      if (dob.getFullYear() > today.getFullYear() ||
          (dob.getFullYear() === today.getFullYear() &&
          dob.getMonth() > today.getMonth()) ||
          (dob.getFullYear() === today.getFullYear() &&
          dob.getMonth() === today.getMonth() &&
          dob.getDate() > today.getDate())) {
        // Display an error message or take appropriate action
        alert("Invalid birth day! \u274C Please enter a date on or before today.");
        // Clear the input value
        this.value = '';
      }
    });
  });
});