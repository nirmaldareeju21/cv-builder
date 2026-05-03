function updateCV() {
    document.getElementById('display-name').innerText = document.getElementById('name').value || "YOUR NAME";
    document.getElementById('display-jobTitle').innerText = document.getElementById('jobTitle').value || "Professional Title";
    document.getElementById('display-phone').innerText = document.getElementById('phone').value || "-";
    document.getElementById('display-email').innerText = document.getElementById('email').value || "-";
    document.getElementById('display-location').innerText = document.getElementById('location').value || "-";
    document.getElementById('display-about').innerText = document.getElementById('about').value || "Summary details...";
    document.getElementById('display-experience').innerText = document.getElementById('experience').value || "Experience details...";
    document.getElementById('display-education').innerText = document.getElementById('education').value || "Education details...";

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

// Template එක මාරු කරන Function එක
function setTemplate(styleName) {
    const cv = document.getElementById('cv-template');
    cv.classList.remove('modern', 'classic'); // කලින් තිබූ ඒවා අයින් කරන්න
    cv.classList.add(styleName); // අලුත් එක දාන්න
}

function changeColor() {
    const color = document.getElementById('themeColor').value;
    document.getElementById('sidebar-bg').style.backgroundColor = color;
    document.querySelectorAll('.theme-text').forEach(el => el.style.color = color);
}

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function() {
        const output = document.getElementById('display-photo');
        output.src = reader.result;
        output.style.display = 'block';
    };
    reader.readAsDataURL(event.target.files[0]);
}

function downloadPDF() {
    const element = document.getElementById('cv-template');
    html2pdf().from(element).set({
        margin: 0,
        filename: 'Custom_CV.pdf',
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    }).save();
}
