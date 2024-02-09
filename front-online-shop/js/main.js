function menu() {
  var menu = document.getElementById("nav");
  if (menu.className === "nav") {
    menu.className += " responsive";
  } else {
    menu.className = "nav";
  }
}
