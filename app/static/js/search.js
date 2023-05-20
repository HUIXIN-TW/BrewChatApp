// Reference
// JavaScript library: jQuery
// Version: 3.6.0
// Source: https://code.jquery.com/jquery-3.6.0.min.js

/**
 * Description: JavaScript code for handling search form submission and marking keywords in messages.
 * File: search.js
 * Author: HuiXin Yang & YunChuan Kung
 */

// handle the search form submission
$('#search-form').submit(function(event) {
    event.preventDefault();
    var query = $('#search-form input[name="query"]').val();
    $.ajax({
      type: 'POST',
      url: '/memory',
      data: {query: query},
      success: function(response) {
        if ('error' in response) {
          $('#search-results').html('<p>' + response.error + '</p>');
        } else {
          var results = response.results;
          var html = '';
          if (results.length > 0) {
            html += '<p>';
            for (var i = 0; i < results.length; i++) {
              html += '<div class="message right">' + results[i].body +'</div>';
              html += '<div class="message left"> ' + results[i].response + '</div>';
              }
            html += '</p>';
            $('#search-results').html(html);
          }
        }
      },
      error: function() {
        alert('An error occurred while searching.');
      }
    });
  });

// mark the keyword in the message
function mark() {
  let keyWord = document.getElementById("keyword").value.trim();
  if (keyWord !== "") {
    let textList = document.querySelectorAll(".message.left, .message.right");
    for (let i = 0; i < textList.length; i++) {
      let text = textList[i].innerHTML;
      let re = new RegExp(keyWord, "gi"); // create a regex, g=global match, i=case insensitive
      let newText = text.replace(re, "<span class='searchHighlight'>$&</span>"); // replace the text
      textList[i].innerHTML = newText;
    }

    // Toggle button text and click event
    let button = document.getElementById("mark-button");
    button.innerHTML = "Clear";
    button.onclick = clearMark;
  }
}
// clear the all marks
function clearMark() {
  let highlights = document.getElementsByClassName("searchHighlight");
  while (highlights.length) {
    highlights[0].outerHTML = highlights[0].innerHTML;
  }

  // Clear the input message
  document.getElementById("keyword").value = "";
    
  // Toggle button text and click event
  let button = document.getElementById("mark-button");
  button.innerHTML = "Mark";
  button.onclick = mark;
}
  