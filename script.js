// 1. තොරතුරු Update කිරීම
function updateCV() {
    document.getElementById('display-name').innerText = document.getElementById('name').value || "NIRMAL DAREEJU";
    document.getElementById('display-jobTitle').innerText = document.getElementById('jobTitle').value || "Job Title";
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

// 2. ටෙම්ප්ලෙට් මාරු කිරීම
function setTemplate(styleName) {
    const cv = document.getElementById('cv-template');
    // සියලු පරණ classes අයින් කර අලුත් එක දාන්න
    cv.classList.remove('modern', 'classic', 'minimalist');
    cv.classList.add(styleName);
}

// 3. පාටවල් වෙන වෙනම ඇප්ලයි කිරීම
function applyColors() {
    const bgColor = document.getElementById('bgColor').value;
    const textColor = document.getElementById('textColor').value;
    
    const sidebar = document.getElementById('cv-sidebar');
    
    // Sidebar එකේ පසුබිම සහ අකුරු පාට
    sidebar.style.backgroundColor = bgColor;
    sidebar.style.color = textColor;

    // ප්‍රධාන මාතෘකා වල පාට (Sidebar එකේ පාටට ගැලපෙන ලෙස)
    document.querySelectorAll('.dynamic-heading').forEach(el => {
        el.style.color = bgColor;
    });
}

// 4. පින්තූරය Preview කිරීම
function previewImage(event) {
    const reader = new FileReader();
    reader.onload = () => {
        const img = document.getElementById('display-photo');
        img.src = reader.result;
        img.style.display = 'block';
    }
    reader.readAsDataURL(event.target.files[0]);
}

// 5. PDF ලෙස Download කිරීම
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
