function updateCV() {
    document.getElementById('display-name').innerText = document.getElementById('name').value || "Nirmal Dareeju";
    document.getElementById('display-jobTitle').innerText = document.getElementById('jobTitle').value || "Job Title";
    document.getElementById('display-phone').innerText = document.getElementById('phone').value || "-";
    document.getElementById('display-email').innerText = document.getElementById('email').value || "-";
    document.getElementById('display-location').innerText = document.getElementById('location').value || "-";
    
    document.getElementById('display-about').innerText = document.getElementById('about').value;
    document.getElementById('display-education').innerText = document.getElementById('education').value;
    document.getElementById('display-experience').innerText = document.getElementById('experience').value;

    // Skills handling
    const skillsText = document.getElementById('skills').value;
    const skillsList = document.getElementById('display-skills');
    skillsList.innerHTML = '';
    
    if (skillsText) {
        skillsText.split('\n').forEach(skill => {
            if (skill.trim() !== "") {
                const li = document.createElement('li');
                li.innerText = skill.trim();
                skillsList.appendChild(li);
            }
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
    html2pdf().from(element).save('CV_Nirmal.pdf');
}
