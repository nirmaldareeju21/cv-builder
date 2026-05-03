function updateCV() {
    // Basic Details
    document.getElementById('display-name').innerText = document.getElementById('name').value || "YOUR NAME";
    document.getElementById('display-jobTitle').innerText = document.getElementById('jobTitle').value || "Professional Title";
    document.getElementById('display-phone').innerText = document.getElementById('phone').value || "-";
    document.getElementById('display-email').innerText = document.getElementById('email').value || "-";
    document.getElementById('display-location').innerText = document.getElementById('location').value || "-";
    
    // Main Content
    document.getElementById('display-about').innerText = document.getElementById('about').value || "Summary details...";
    document.getElementById('display-experience').innerText = document.getElementById('experience').value || "Experience details...";
    document.getElementById('display-education').innerText = document.getElementById('education').value || "Education details...";

    // Skills List
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

// කැමති පාටක් තෝරාගැනීමේ පහසුකම
function changeColor() {
    const color = document.getElementById('themeColor').value;
    document.getElementById('sidebar-bg').style.backgroundColor = color;
    
    const themeTexts = document.querySelectorAll('.theme-text');
    themeTexts.forEach(el => {
        el.style.color = color;
    });
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
        margin: 0,
        filename: 'My_CV.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(element).save();
}
