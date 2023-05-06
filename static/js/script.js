// get all close buttons under flash messages
var closeButtons = document.querySelectorAll('.flash-message .close');

// add click event listener to each close button
closeButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    // get the parent element (i.e., the message box) and remove it
    var parent = this.parentNode;
    parent.parentNode.removeChild(parent);
  });
});
