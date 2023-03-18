'use strict';

const submitButton = document.getElementById('sign-up');

submitButton.addEventListener('click', (event) => {
    event.preventDefault();
    window.location.href = '/';
});

// const button2 = document.querySelector("#prompt-2");

// function handleClick2(event) {
//   alert(`${document.querySelector('#alert-text').value}`);
//   // console.log(the_alert);
//   event.preventDefault();

// }

// button2.addEventListener('click', handleClick2);