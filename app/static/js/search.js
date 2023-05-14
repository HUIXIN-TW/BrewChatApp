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
                html += '<li><strong>Result:</strong> ' + JSON.stringify(results[i]) + '</li>';
                html += '<li><strong>Body:</strong> ' + results[i].body + " " + results[i].timestamp +'</li>';
                html += '<li><strong>Response:</strong> ' + results[i].response + " " + results[i].timestamp + '</li>';
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
  