function getRandomUser() {
    fetch('/get_random_user')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        if (data.random_user_name) {
          // Update the random user name element
          document.getElementById('randomUserName').innerText = data.random_user_name;
        } else {
          // Handle the case when no random user is available
          document.getElementById('randomUserName').innerText = 'No random user available';
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  