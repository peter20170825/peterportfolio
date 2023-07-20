

var pop1 = document.querySelector('#myimage1');

pop1.addEventListener('mouseover',function(){
  document.getElementById('demo').innerHTML = 'Minimize widow after clicking Guess Number App'
  document.getElementById('demo').style.fontSize = '40px'
  document.getElementById('demo').style.color = 'red'
})

pop1.addEventListener('mouseleave',function(){
  document.getElementById('demo').innerHTML = '';
})


var pop2 = document.querySelector('#myimage2');

pop2.addEventListener('mouseover',function(){
  document.getElementById('demo').innerHTML = 'Minimize widow after clicking Student GUI App'
  document.getElementById('demo').style.fontSize = '40px'
  document.getElementById('demo').style.color = 'green'
})

pop2.addEventListener('mouseleave',function(){
  document.getElementById('demo').innerHTML = '';
})




let popup = document.getElementById('popup');

function openPopup(){
    popup.classList.add('open-popup');
}

function closePopup(){
     popup.classList.remove('open-popup');
}
