// script.js
document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        // Read the file as text
        const reader = new FileReader();
        reader.onload = function(e) {
            const fileContent = reader.result;
            // Do something with the file content, e.g., display it in the textarea
    
            // Append the file content to the textarea
            document.getElementById('textarea').innerText = e.target.result;
        }; 
        reader.readAsText(file);
    } else {
        alert("Please select a file."); 
    }
});
// document.addEventListener("DOMContentLoaded", () => {
//     const dropdown = document.querySelector(".dropdown");
//     const dropdownList = document.querySelector(".dropdown-list");

//     // Toggle dropdown visibility on hover
//     dropdown.addEventListener("mouseenter", () => {
//         dropdownList.style.display = "block";
//     });

//     dropdown.addEventListener("mouseleave", () => {
//         dropdownList.style.display = "none";
//     });
// });
