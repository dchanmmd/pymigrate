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

/** @type {HTMLDialogElement} */
const confirmDialog = document.getElementById('transfer-confirm-modal');

/** @type {HTMLUListElement} */
const transferSummary = document.getElementById('transfer-summary');

/** @type {HTMLButtonELement} */
const confirmTransferButton = document.getElementById('confirm-transfer-btn');

/** @type {HTMLButtonELement} */
const cancelTransferButton = document.getElementById('cancel-transfer-btn');

let page = null;
let query = null;
let last = false;

const updateSearchParams = () => {
    const params = new URLSearchParams(window.location.search);
    page = parseInt(params.get('page') ?? 1);
    query = params.get('query');
};

// Set page's initial state
window.addEventListener('DOMContentLoaded', () => {
    // Transfer button is disabled if no rows are selected
    submitTransferButton.disabled = !document.querySelectorAll('input[type="checkbox"][name="row-ids"]:checked').length;
    // Previous page button is disabled if page is 1 or less
    previousPageButton.disabled = page <= 1;
});

// Text clear implementation
const clearSearch = () => {
    searchBar.value = '';
};

// Clear search bar on 'X' button click
clearSearchButton.addEventListener('click', clearSearch);

// Text search implementation
const searchText = async () => {
    query = searchBar.value;
    const params = { query };
    if (page) params['page'] = page;
    const rows = await getTableUpdate(params);
    if (tableBody) tableBody.innerHTML = rows;
    syncCheckboxesToSet();
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
    const lastContent = tableBody.innerHTML;
    tableBody.innerHTML = '';
    const rows = await getTableUpdate({ page, query });
    if (tableBody) tableBody.innerHTML = rows ?? lastContent;
    resetSelection();
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
    const itemId = button.dataset['id'];
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
    if (submitTransferButton) submitTransferButton.disabled = !rowIds.size;
});

// Select all implementation
const selectAllControlsAll = () => {
    const checkboxes = tableBody.querySelectorAll('input[type="checkbox"][name="row-ids"]');
    checkboxes.forEach((c) => {
        c.checked = selectAll.checked;
        selectAll.checked ? rowIds.add(c.value) : rowIds.delete(c.value);
    });

    if (submitTransferButton) submitTransferButton.disabled = !rowIds.size;
};

// Update selection on 'select all' check
selectAll.addEventListener('change', selectAllControlsAll);

// Load previous page implementation
const previousPage = async () => {
    page = Math.max(page - 1, 0);
    console.log({ page });
    const rows = await getTableUpdate({ page, query });
    if (tableBody) tableBody.innerHTML = rows;
    syncCheckboxesToSet();
}

// Load next page on '>' button click
previousPageButton.addEventListener('click', previousPage);

// Load next page implementation
const nextPage = async () => {
    if (!page) page = 1;
    page++;
    const rows = await getTableUpdate({ page, query });
    if (tableBody) tableBody.innerHTML = rows;
    syncCheckboxesToSet();
}

// Load next page on '>' button click
nextPageButton.addEventListener('click', nextPage);

// Confirmation dialog implementation
const showConfirmationDialog = () => {
    if (!rowIds.size) return showAlert('Debe seleccionar al menos un registro para transferir.');
    
    const list = Array.from(rowIds);
    confirmDialog.showModal();
};

// Show confirmation dialog on transfer button click
submitTransferButton.addEventListener('click', showConfirmationDialog);

// Hide confirmation dialog implementation
const cancelTransfer = () => {
    confirmDialog.close();
}

// Hide confirmation dialog on cancel button click
cancelTransferButton.addEventListener('click', cancelTransfer);

/**
 * Request a re-render of the table as HTML.
 * @param {{ page?: number, query?: string }} args
 * @return {Promise<string>} A promise that resolves to the HTML for the updated table.
 */
const getTableUpdate = async ({ page, query } = {}) => {
    const branchId = window.location.pathname.split('/').filter(Boolean)[1];
    const url = new URL(`/api/v1/inventory/${branchId}/rows`, window.location.origin);

    if (page) url.searchParams.set('page', page);
    if (query) url.searchParams.set('query', query);

    const response = await fetch(url, {
        method: 'GET'
    });

    if (response.ok) {
        previousPageButton.disabled = page <= 1;
        nextPageButton.disabled = response.headers.get('X-Is-Last-Page')?.trim() === 'true';
        return await response.text();
    }
};

// Clear checkboxes and Set implementation
const resetSelection = () => {
    rowIds.clear();
    if (selectAll) selectAll.checked = false;
    if (submitTransferButton) submitTransferButton.disabled = true;
};

// Re-check boxes according to Set implementation
const syncCheckboxesToSet = () => {
    const checkboxes = tableBody.querySelectorAll('input[type="checkbox"][name="row-ids"]');
    checkboxes.forEach((c) => {
        c.checked = rowIds.has(c.value);
    });

    if (selectAll) selectAll.checked = checkboxes.length > 0 && Array.from(checkboxes).every(c => c.checked);
    if (submitTransferButton) submitTransferButton.disabled = !rowIds.size;
};

/**
 * Request a re-render of the dialog content as HTML.
 * @param {string} itemId
 * @return {Promise<string>} A promise that resolves to the HTML for the updated dialog content.
 */
const getItemDetails = async (itemId) => {
    const branchId = window.location.pathname.split('/').filter(Boolean)[1];
    const url = new URL(`/api/v1/inventory/${branchId}/rows/${itemId}`, window.location.origin);

    if (page) url.searchParams.set('page', page);
    if (query) url.searchParams.set('query', query);

    const response = await fetch(url, {
        method: 'GET'
    });

    if (response.ok) {
        return await response.text();
    }
}