
function reval(){
  // var z = document.getElementsByClassName("trialsel")
  // return z[0][z[0].selectedIndex].value
  var v = document.getElementById("selectid");
  return v.options[v.options.selectedIndex].value
}

function resrc(filename){
  var img_element = document.getElementById("imgid");
  var loc = window.location.pathname;
  var dir = loc.substring(0, loc.lastIndexOf('/'));
  img_element.setAttribute("src",(dir+filename))
}

function newwin(url_new){
  window.open(url_new);
}

// document.getElementById("seattle").addEventListener("click", function(){ window.open("{% url 'appHome:myseattle' %}"); });

// vs window.location.assign
/*$(document).ready(function(){
  $('.dropTab').hover(function(){
    $(this).children('.dropBox').slideToggle();
  });
});*/
