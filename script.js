function generateCV() {
    // Input වලින් දත්ත ලබා ගැනීම
    document.getElementById('display-name').innerText = document.getElementById('name').value;
    document.getElementById('display-job').innerText = document.getElementById('job').value;
    document.getElementById('display-email').innerText = document.getElementById('email').value;
    document.getElementById('display-about').innerText = document.getElementById('about').value;
}

function downloadPDF() {
    const element = document.getElementById('cv-template');
    const opt = {
        margin:       10,
        filename:     'My_CV.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    // PDF එක සකසා Download කිරීම
    html2pdf().set(opt).from(element).save();
}
