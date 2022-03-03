// const card = document.querySelector('.search__btn_card'),
//       burger = document.querySelector('.burger-content')
// card.addEventListener('click', (e) => {
//     burger.classList.toggle('.burger_card_active')
// });

const card = document.querySelector('.search__btn_card'),
  burger = document.querySelector('.burger-content');
card.addEventListener('click', (e) => {
  burger.classList.remove('burger-content')
  burger.classList.add('burger_card_active')
});
const rem = document.querySelector('.burger-menu_up');
rem.addEventListener('click', () => {
  burger.classList.add('burger-content')
  burger.classList.remove('burger_card_active')
});

const icons = document.querySelectorAll('.post-date span'),
  icon = document.querySelectorAll('.post-date'),
  cartAdd = document.querySelectorAll('.cart-add');

function addToCart(arr) {
  if (arr.length) {
    arr.forEach(element => {
      if (element) {
        element.addEventListener("click", (e) => {
          const target = e.target;
          if (target && target === element) {
            if(element.classList.contains('fa-cart-plus')) {
              element.classList.remove("fa-cart-plus");
              element.classList.add("fa-check");
            } else {
              element.classList.add("fa-cart-plus");
              element.classList.remove("fa-check");
            } 
          }
        })
      }
    });
  }
}


addToCart(cartAdd);

























