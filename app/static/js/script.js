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

function type_effect_setting() {
  // create a typing effect
  var count = 0;
  var speed = 100;
  var idName = "type-effect";
  var word = document.getElementById(idName).innerHTML;
  typingEffect(word, idName, count, speed);
}

// creates a typing effect by gradually printing out the characters of a given word
function typingEffect(word, idName, count, speed) {
  // checks if the element exists in the DOM. If not, it returns.
  const element = document.getElementById(idName);
  if (!element) return;
  // gets the substring of the word from the first character to the current count
  const text = word.substring(0, count);
  element.innerHTML = text;

  // if the current count is less than the length of the word, it calls the function again
  if (count < word.length) {
    setTimeout(() => {
      typingEffect(word, idName, count + 1, speed);
    }, speed);
  }
}

// using js and DOM to change the appearance of page
function toggleMode() {
  var icon = document.getElementById("mode-icon");
  var currentClass = icon.className;

  // if the current class is sunny, change it to moon and vice versa
  if (currentClass === "ion-ios-sunny-outline") {
    icon.className = "ion-ios-moon-outline";
    document.body.classList.add("dark-mode");
    document.querySelector("footer").classList.add("dark-mode");
    document.querySelectorAll("nav li a").forEach(function (icon) {
      icon.classList.add("dark-mode");
    });
  } else {
    icon.className = "ion-ios-sunny-outline";
    document.body.classList.remove("dark-mode");
    document.querySelector("footer").classList.remove("dark-mode");
    document.querySelectorAll("nav li a").forEach(function (icon) {
      icon.classList.remove("dark-mode");
    });
  }
}
