'use strict';

const inputField = document.getElementById('equationInput');
const outputDiv = document.getElementById('outputDiv');

inputField.addEventListener('input', () => {
  const inputText = inputField.value;
  outputDiv.textContent = inputText;
  katex.render(inputText, outputDiv);
});