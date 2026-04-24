const biEye = document.createElement('i');
biEye.classList.add('bi', 'bi-eye-fill', 'text-lg', 'text-neutral-600');

const biEyeSlash = document.createElement('i');
biEyeSlash.classList.add('bi', 'bi-eye-slash-fill', 'text-lg', 'text-indigo-600');

/** @type {HTMLFormElement} */
const loginForm = document.getElementById('login');

/** @type {HTMLInputElement} */
const passwordInput = document.getElementById('password');

/** @type {HTMLButtonElement} */
const togglePassword = document.getElementById('toggle-password');

window.addEventListener('DOMContentLoaded', () => {
    passwordInput.type = 'password';
    togglePassword.replaceChildren(biEye);
});

const changePasswordVisibility = () => {
    const currentType = passwordInput.type;
    passwordInput.type = currentType === 'password' ? 'text' : 'password';
    togglePassword.replaceChildren(currentType === 'password' ? biEyeSlash : biEye);
};

togglePassword.addEventListener('click', changePasswordVisibility);


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