console.log('working');
if(localStorage.getItem('cart')==null){
                var cart ={};
            }
else{
                cart = JSON.parse(localStorage.getItem('cart'))
            }
$('.cart').click(function(){
console.log('clicked');
            });