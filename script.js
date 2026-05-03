function updateCV() {
    document.getElementById('display-name').innerText = document.getElementById('name').value || "Your Name";
    document.getElementById('display-jobTitle').innerText = document.getElementById('jobTitle').value || "Job Title";
    
    document.getElementById('display-phone').innerText = document.getElementById('phone').value || "Phone Number";
    document.getElementById('display-email').innerText = document.getElementById('email').value || "Email Address";
    document.getElementById('display-location').innerText = document.getElementById('location').value || "City, Country";
    
    document.getElementById('display-about').innerText = document.getElementById('about').value || "Professional Summary...";
    document.getElementById('display-education').innerText = document.getElementById('education').value || "Education Details...";
    document.getElementById('display-experience').innerText = document.getElementById('experience').value || "Professional Experience Details...";

    // Handle Skills (comma separated to list)
    const skillsText = document.getElementById('skills').value;
    const skillsList = document.getElementById('display-skills');
    skillsList.innerHTML = ''; // Clear previous list
    if (skillsText) {
        skillsText.split(',').forEach(skill => {
            const li = document.createElement('li');
            li.innerText = skill.trim();
            skillsList.appendChild(li);
        });
    }
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

function downloadPDF() {
    const element = document.getElementById('cv-template');
    const opt = {
        margin: 10,
        filename: 'Professional_CV.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(element).save();
}
