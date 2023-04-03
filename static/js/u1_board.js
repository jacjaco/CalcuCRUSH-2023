'use strict';

const cell = document.querySelector('.cell');
const marker = document.querySelector('.marker');

cell.addEventListener('click', (event) => {
    marker.style.display='block';
    marker.style.top = event.clientY - cell.offsetTop + 'px';
    marker.style.left = event.clientX - cell.offsetLeft + 'px';
});