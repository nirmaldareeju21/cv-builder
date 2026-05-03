function updateCV() {
    document.getElementById('display-name').innerText = document.getElementById('name').value || "YOUR NAME";
    document.getElementById('display-jobTitle').innerText = document.getElementById('jobTitle').value || "Job Title";
    document.getElementById('display-phone').innerText = document.getElementById('phone').value || "-";
    document.getElementById('display-email').innerText = document.getElementById('email').value || "-";
    document.getElementById('display-location').innerText = document.getElementById('location').value || "-";
    document.getElementById('display-about').innerText = document.getElementById('about').value || "Summary...";
    document.getElementById('display-experience').innerText = document.getElementById('experience').value || "Experience...";
    document.getElementById('display-education').innerText = document.getElementById('education').value || "Education...";

    const skills = document.getElementById('skills').value.split('\n');
    const list = document.getElementById('display-skills');
    list.innerHTML = '';
    skills.forEach(s => { if(s.trim()) { let li = document.createElement('li'); li.innerText = s.trim(); list.appendChild(li); }});
}

function setTemplate(styleName) {
    const cv = document.getElementById('cv-template');
    cv.className = 'a4-page ' + styleName;
}

function applyColors() {
    const bgColor = document.getElementById('bgColor').value;
    const textColor = document.getElementById('textColor').value;
    const sidebar = document.getElementById('cv-sidebar');
    
    sidebar.style.backgroundColor = bgColor;
    sidebar.style.color = textColor;

    document.querySelectorAll('.dynamic-heading').forEach(el => {
        el.style.color = bgColor;
    });
}

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = () => {
        const img = document.getElementById('display-photo');
        img.src = reader.result;
        img.style.display = 'block';
    }
    reader.readAsDataURL(event.target.files[0]);
}

function downloadPDF() {
    const element = document.getElementById('cv-template');
    html2pdf().from(element).set({
        margin: 0,
        filename: 'CV_Download.pdf',
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    }).save();
}
