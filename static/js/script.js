// get all close buttons under flash messages
var closeButtons = document.querySelectorAll(".flash-message .close");

// add click event listener to each close button
closeButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // get the parent element (i.e., the message box) and remove it
    var parent = this.parentNode;
    parent.parentNode.removeChild(parent);
  });
});

// get edit and save btn
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
