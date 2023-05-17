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