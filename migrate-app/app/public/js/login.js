const biEye = document.createElement('i');
biEye.classList.add('bi', 'bi-eye-fill', 'text-lg', 'text-neutral-600');

const biEyeSlash = document.createElement('i');
biEyeSlash.classList.add('bi', 'bi-eye-slash-fill', 'text-lg', 'text-indigo-600');

/** @type {HTMLDivElement} */
const htmlAlert = document.getElementById('alert');

/** @type {HTMLFormElement} */
const alertContent = document.getElementById('alert-content');

/** @type {HTMLButtonElement} */
const closeAlertButton = document.getElementById('close-alert');

/** @type {HTMLFormElement} */
const loginForm = document.getElementById('login');

/** @type {HTMLInputElement} */
const passwordInput = document.getElementById('password');

/** @type {HTMLButtonElement} */
const togglePassword = document.getElementById('toggle-password');

window.addEventListener('DOMContentLoaded', () => {
    htmlAlert.style.display = 'none';
    htmlAlert.style.visibility = 'visible';
    alertContent.textContent = '';
    passwordInput.type = 'password';
    togglePassword.replaceChildren(biEye);
});

const changePasswordVisibility = () => {
    const currentType = passwordInput.type;
    passwordInput.type = currentType === 'password' ? 'text' : 'password';
    togglePassword.replaceChildren(currentType === 'password' ? biEyeSlash : biEye);
};

togglePassword.addEventListener('click', changePasswordVisibility);

/** @param {string} text */
const showAlert = (text) => {
    alertContent.textContent = text;
    htmlAlert.style.display = 'flex';
};

const closeAlert = () => {
    htmlAlert.style.display = 'none';
};

closeAlertButton.addEventListener('click', closeAlert);


const sendLoginData = async () => {
    const data = new FormData(loginForm);

    const username = data.get('username');
    const password = data.get('password');

    if (!username) return showAlert('Su usuario no puede estar vacío.');
    if (!password) return showAlert('Su contraseña no puede estar vacía.');

    const payload = { username, password };
    const url = new url('api/v1/auth/login', window.location.origin);

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
}

loginForm.addEventListener('submit', (event) => {
    event.preventDefault();
    sendLoginData();
});