const editBtn = document.getElementById("edit-btn");
const saveBtn = document.getElementById("save-btn");
const inputElems = document.querySelectorAll("input[readonly]");
const selectElems = document.querySelectorAll("select[readonly]");

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







