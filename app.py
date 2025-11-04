from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from utils.image_caption import generate_caption
from utils.translator import translate_text

app = Flask(__name__)
CORS(app)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'temp_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Create temp folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    try:
        # Check if image was uploaded
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        
        # Check if file is valid
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Please upload an image.'}), 400
        
        # Save file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Generate English caption using AI
        print("Generating caption...")
        english_description = generate_caption(filepath)
        
        # Translate to Hindi and Bengali
        print("Translating...")
        hindi_description = translate_text(english_description, 'hi')
        bengali_description = translate_text(english_description, 'bn')
        
        # Clean up - delete the temporary file
        os.remove(filepath)
        
        # Return results
        return jsonify({
            'english': english_description,
            'hindi': hindi_description,
            'bengali': bengali_description
        })
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Project A.I.D. is running!'})

if __name__ == '__main__':
    print("🚀 Starting Project A.I.D....")
    print("🌍 Access the app at: http://localhost:5000")
    app.run(debug=False, host='0.0.0.0', port=5000)
