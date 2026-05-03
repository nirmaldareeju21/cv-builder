function updateCV() {
    document.getElementById('display-name').innerText = document.getElementById('name').value || "Your Name";
    document.getElementById('display-job').innerText = document.getElementById('job').value || "Job Title";
    document.getElementById('display-about').innerText = document.getElementById('about').value || "Summary...";
}

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function() {
        const output = document.getElementById('display-photo');
        output.src = reader.result;
        output.style.display = 'block';
    }
    reader.readAsDataURL(event.target.files[0]);
}

function changeTemplate() {
    const template = document.getElementById('templateSelector').value;
    document.getElementById('cv-template').className = 'preview ' + template;
}

function downloadPDF() {
    const element = document.getElementById('cv-template');
    html2pdf().from(element).save('My_CV.pdf');
}
