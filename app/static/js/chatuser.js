// Reference
// JavaScript library: jQuery
// Version: 3.6.0
// Source: https://code.jquery.com/jquery-3.6.0.min.js

// Reference
// JavaScript library: Socket.IO
// Version: 4.4.1
// Source: https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.4.1/socket.io.js

/**
 * Description: JavaScript code for chat room functionality using Socket.IO.
 * Dependencies: Socket.IO (4.4.1), jQuery (3.6.0)
 * Author: HuiXin Yang
*/

$(document).ready(function(){
  // Connect to the server using Socket.IO
  const socket = io.connect(window.location.origin + '/chat/');

  // Event handler for successful connection
  socket.on('connect', function() {
    // Send a 'join' event to the server to indicate the user has joined
    socket.emit('join', {});
  });

  // Event handler for receiving status messages from the server
  socket.on('status', ({ msg }) => {
    $('#chat').val(`${$('#chat').val()}<${msg}>\n`);
    $('#chat').scrollTop($('#chat')[0].scrollHeight);
  });

  // Event handler for receiving chat messages from the server
  socket.on('message', ({ msg }) => {
    $('#chat').val(`${$('#chat').val()}${msg}\n`);
    $('#chat').scrollTop($('#chat')[0].scrollHeight);
  });

  // Event handler for sending a chat message
  $('#text-form').submit((e) => {
    e.preventDefault();
    const text = $('#text').val().trim();
    if (text) {
      $('#text').val('');
      socket.emit('text', { msg: text });
    }
  });

  // Event handler for getting a random user
  $('#randomUserButton').on('click', getRandomUser);
  $('#leaveRoomButton').on('click', leaveRoom);


  // // Function to leave the chat room
  // function leaveRoom() {
  //   // Send a 'left' event to the server and disconnect
  //   socket.emit('left', () => {
  //     socket.disconnect();
  //     window.location.href = '/';
  //   });
  // }

// Function to leave the chat room
function leaveRoom() {
  // Show a confirmation dialog
  const confirmation = confirm("Are you ready to take a break from the BrewChat café? If you leave, you might miss out on your favorite blend of conversations. Are you sure you want to exit?");

  if (confirmation) {
    // Send a 'left' event to the server and disconnect
    socket.emit('left', () => {
      socket.disconnect();
      window.location.href = '/';
    });
  }
}


  // Function to get a random user
  function getRandomUser() {
    console.log('Getting random user...');
    $.ajax({
      url: '/get_random_user',
      method: 'GET',
      success: ({ random_user_name }) => {
        if (!random_user_name) {
          $('#randomUserName').text('No user available');
        }
        else {
          $('#randomUserName').text(random_user_name);
        }
      },
      error: (error) => {
        console.error('Failed to get random user:', error);
        $('#randomUserName').text('Failed to get random user');
      }
    });
  }
});

