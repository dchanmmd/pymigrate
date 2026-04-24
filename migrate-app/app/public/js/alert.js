/** @type {HTMLDivElement} */
const htmlAlert = document.getElementById('alert');

/** @type {HTMLFormElement} */
const alertContent = document.getElementById('alert-content');

/** @type {HTMLButtonElement} */
const closeAlertButton = document.getElementById('close-alert');

window.addEventListener('DOMContentLoaded', () => {
    alertContent.textContent = '';
    htmlAlert.classList.remove('flex', 'visible');
    htmlAlert.classList.add('hidden', 'invisble');
})

/** @param {string} text */
const showAlert = (text) => {
    alertContent.textContent = text;
    htmlAlert.classList.remove('hidden', 'invisible');
    htmlAlert.classList.add('flex', 'visible');
};

const closeAlert = () => {
    htmlAlert.classList.remove('flex', 'visible');
    htmlAlert.classList.add('hidden', 'invisible');
};

closeAlertButton.addEventListener('click', closeAlert);