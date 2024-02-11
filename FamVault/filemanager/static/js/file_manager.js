// file_manager.js
document.addEventListener('DOMContentLoaded', function () {
    const folders = document.querySelectorAll('.folder');
    folders.forEach(folder => {
        const folderName = folder.querySelector('.folder-name');
        folderName.addEventListener('click', function () {
            folder.classList.toggle('open');
        });
    });
});
// python manage.py makemigrations
// python manage.py migrate

