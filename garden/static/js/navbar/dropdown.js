const dropdown = document.getElementById('about-dropdown');
const dropdownMenu = document.getElementById('dropdown-menu');

dropdown.addEventListener('click', function (e) {
    e.stopPropagation();
    const isDisplayed = dropdownMenu.style.display === 'flex';
    dropdownMenu.style.display = isDisplayed ? 'none' : 'flex';
});

document.addEventListener('click', function () {
    dropdownMenu.style.display = 'none';
});