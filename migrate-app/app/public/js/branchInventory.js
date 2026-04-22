/** @type {Set<string>} */
const rowIds = new Set();

/** @type {HTMLInputElement} */
const searchBar = document.getElementById('search-bar');

/** @type {HTMLButtonELement} */
const clearSearchButton = document.getElementById('clear-search');

/**  @type {HTMLButtonElement} */
const refreshButton = document.getElementById('refresh-results');

/** @type {HTMLButtonElement} */
const submitTransferButton = document.getElementById('submit-transfer');

/** @type {HTMLElement} */
const tableBody = document.getElementById('tbody');

/** @type {HTMLButtonElement} */
const previousPageButton = document.getElementById('previous-btn');

/** @type {HTMLButtonElement} */
const nextPageButton = document.getElementById('next-btn');

/** @type {HTMLDialogElement} */
const dialog = document.getElementById('row-details');

/** @type {HTMLButtonELement} */
const closeDialogButton = document.getElementById('close-dialog-btn');

/** @type {HTMLDivElement} */
const dialogContent = document.getElementById('dialog-content');

/** @type {HTMLFormElement} */
const transferForm = document.getElementById('transfer-form');

/** @type {HTMLInputElement} */
const selectAll = document.getElementById('select-all');



let page = null;
let query = null;

const updateSearchParams = () => {
    const params = new URLSearchParams(window.location.search);
    page = parseInt(params.get('page') ?? 0);
    query = params.get('query');
};

// Set page's initial state
window.addEventListener('DOMContentLoaded', () => {
    // Transfer button is disabled if no rows are selected
    submitTransferButton.disabled = !rowIds.size;
});

// Text clear implementation
const clearSearch = () => {
    searchBar.value = '';
};

// Clear search bar on 'X' button click
clearSearchButton.addEventListener('click', clearSearch);

// Text search implementation
const searchText = async () => {
    const query = encodeURIComponent(searchBar.value);
    const params = { query };
    if (page) params['page'] = page;
    const rows = await getTableUpdate(params);
    if (tableBody) tableBody.innerHTML = rows;
};

// Begin text search on Enter
/** @param {KeyboardEvent} event */
searchBar.addEventListener('keydown', (event) => {
    if (event.key.toLowerCase() === 'enter') {
        searchText();
    }
});

// Table refresh implementation
const refreshTable = async () => {
    const rows = await getTableUpdate({ page, query });
    if (tableBody) tableBody.innerHTML = rows;
}

// Refresh table on Enter
refreshButton.addEventListener('click', () => {
    refreshButton.disabled = true;
    refreshButton.classList.add('spin');
    refreshTable().finally(() => setTimeout(() => {
        refreshButton.classList.remove('spin');
        refreshButton.disabled = false;
    }, 500));
});


// Show modal dialog implementation
/** @param {HTMLButtonElement} button */
const openDetails = async (button) => {
    const itemId = button.dataset["id"];
    const details = await getItemDetails(itemId);
    if (dialog && dialogContent) {
        dialogContent.innerHTML = details;
        dialog.showModal();
    }
}

// Close dialog on 'X' button click
closeDialogButton.addEventListener('click', () => dialog.close());


// Send transfer request implementation
const sendTransferRequest = async () => {
    const payload = { rowIds: Array.from(rowIds) };
    const branchId = window.location.pathname.split('/').filter(Boolean)[1];
    const url = new URL(`/api/v1/inventory/transfer`, window.location.origin);

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    console.log(response.status);
};

// Update selection on checkbox check
tableBody.addEventListener('change', (event) => {
    const checkboxes = tableBody.querySelectorAll('input[type="checkbox"][name="row-ids"]');
    const checkbox = event.target.closest('input[type="checkbox"][name="row-ids"]');
    if (!checkbox) return;

    if (checkbox.checked) {
        rowIds.add(checkbox.value);
    } else {
        rowIds.delete(checkbox.value);
    }

    if (selectAll) selectAll.checked = Array.from(checkboxes).every(c => c.checked);
});

// Select all implementation
const selectAllControlsAll = () => {
    const checkboxes = tableBody.querySelectorAll('input[type="checkbox"][name="row-ids"]');
    checkboxes.forEach((c) => {
        c.checked = selectAll.checked;
        selectAll.checked ? rowIds.add(c.value) : rowIds.delete(c.value);
    });
};

// Update selection on 'select all' check
selectAll.addEventListener('change', selectAllControlsAll);

/**
 * Request a re-render of the table as HTML.
 * @param {{ page?: number, query?: string }} args
 * @return {Promise<string>} A promise that resolves to the HTML for the updated table.
 */
const getTableUpdate = async ({ page, query } = {}) => {
    const branchId = window.location.pathname.split('/').filter(Boolean)[1];
    const url = new URL(`/api/v1/inventory/${branchId}/rows`, window.location.origin);

    if (page) url.searchParams.set('query', page);
    if (query) url.searchParams.set('query', query);

    const response = await fetch(url, {
        method: 'GET'
    });

    if (response.ok) {
        return await response.text();
    }
};

/**
 * Request a re-render of the dialog content as HTML.
 * @param {string} itemId
 * @return {Promise<string>} A promise that resolves to the HTML for the updated dialog content.
 */
const getItemDetails = async (itemId) => {
    const branchId = window.location.pathname.split('/').filter(Boolean)[1];
    const url = new URL(`/api/v1/inventory/${branchId}/rows/${itemId}`, window.location.origin);

    if (page) url.searchParams.set('query', page);
    if (query) url.searchParams.set('query', query);

    const response = await fetch(url, {
        method: 'GET'
    });

    if (response.ok) {
        return await response.text();
    }
}