function updateCV() {
    document.getElementById('display-name').innerText = document.getElementById('name').value || "Nirmal Dareeju";
    document.getElementById('display-jobTitle').innerText = document.getElementById('jobTitle').value || "AC Technician";
    document.getElementById('display-phone').innerText = document.getElementById('phone').value || "-";
    document.getElementById('display-email').innerText = document.getElementById('email').value || "-";
    document.getElementById('display-location').innerText = document.getElementById('location').value || "-";
    
    document.getElementById('display-about').innerText = document.getElementById('about').value || "Summary...";
    document.getElementById('display-experience').innerText = document.getElementById('experience').value || "Experience...";
    document.getElementById('display-education').innerText = document.getElementById('education').value || "Education...";

    const skillsText = document.getElementById('skills').value;
    const skillsList = document.getElementById('display-skills');
    skillsList.innerHTML = '';
    if (skillsText) {
        skillsText.split('\n').forEach(skill => {
            if (skill.trim()) {
                const li = document.createElement('li');
                li.innerText = skill.trim();
                skillsList.appendChild(li);
            }
        });
    }
}

// 1. ටෙම්ප්ලෙට් මාරු කිරීම
function setTemplate(styleName) {
    const cv = document.getElementById('cv-template');
    cv.className = 'a4-page ' + styleName;
    console.log("Template changed to: " + styleName); // පරීක්ෂා කිරීමට
}

// 2. පාටවල් වෙන වෙනම වෙනස් කිරීම
function applyColors() {
    const bgColor = document.getElementById('bgColor').value;
    const textColor = document.getElementById('textColor').value;
    
    const sidebar = document.getElementById('cv-sidebar');
    if (sidebar) {
        sidebar.style.backgroundColor = bgColor;
        sidebar.style.color = textColor;
    }

    // Heading වලටත් ඒ පාටම දීම
    document.querySelectorAll('.theme-text').forEach(el => {
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
        filename: 'My_Professional_CV.pdf',
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    }).save();
}
