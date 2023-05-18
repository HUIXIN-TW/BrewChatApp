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
            html += '<ul>';
            for (var i = 0; i < results.length; i++) {
              //Original code, keep temporary, need to delete after finalisation
              //html += '<li><strong>Result:</strong> ' + JSON.stringify(results[i]) + '</li>';
              //html += '<li><strong>Body:</strong>' + results[i].body + " " + results[i].timestamp +'</li>';
              //html += '<li><strong>Response:</strong>' + results[i].response + " " + results[i].timestamp + '</li>';
              html += '<li><div class="message right">' + results[i].body + '</li>';
              html += '<li><div class="message left"> ' + results[i].response + '</li>';
              }
            html += '</ul>';
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
  