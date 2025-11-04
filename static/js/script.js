// Get DOM elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const previewContainer = document.getElementById('previewContainer');
const previewImg = document.getElementById('previewImg');
const loading = document.getElementById('loading');
const error = document.getElementById('error');
const results = document.getElementById('results');

// Click to upload
uploadArea.addEventListener('click', () => {
    fileInput.click();
});

// File selected via input
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        handleImage(file);
    }
});

// Drag and drop functionality
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
        handleImage(file);
    } else {
        showError('Please drop an image file!');
    }
});

// Main function to handle image upload and analysis
function handleImage(file) {
    // Validate file size (16MB max)
    const maxSize = 16 * 1024 * 1024;
    if (file.size > maxSize) {
        showError('File is too large! Please upload an image under 16MB.');
        return;
    }
    
    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImg.src = e.target.result;
        previewContainer.style.display = 'block';
    };
    reader.readAsDataURL(file);
    
    // Reset UI
    results.style.display = 'none';
    error.style.display = 'none';
    loading.style.display = 'block';
    
    // Send to backend for analysis
    const formData = new FormData();
    formData.append('image', file);
    
    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loading.style.display = 'none';
        
        if (data.error) {
            showError(data.error);
        } else {
            displayResults(data);
        }
    })
    .catch(err => {
        loading.style.display = 'none';
        showError('Something went wrong! Please try again.');
        console.error('Error:', err);
    });
}

// Display results
function displayResults(data) {
    document.getElementById('englishDesc').textContent = data.english;
    document.getElementById('hindiDesc').textContent = data.hindi;
    document.getElementById('bengaliDesc').textContent = data.bengali;
    results.style.display = 'block';
    
    // Smooth scroll to results
    results.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Show error message
function showError(message) {
    error.textContent = '❌ ' + message;
    error.style.display = 'block';
    setTimeout(() => {
        error.style.display = 'none';
    }, 5000);
}

// Text-to-speech functionality
function speakText(lang, text) {
    // Stop any ongoing speech
    speechSynthesis.cancel();
    
    // Create new utterance
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = lang;
    utterance.rate = 0.9; // Slightly slower for clarity
    
    // Speak
    speechSynthesis.speak(utterance);
}
