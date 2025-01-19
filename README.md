

# 🏥 Medical Imaging Diagnosis Agent

This project is a **Medical Imaging Diagnosis Agent** that combines advanced computer vision techniques and OpenAI's GPT-4 model to analyze chest X-rays and provide detailed insights. The application is built using **Streamlit** for an interactive web-based interface.

---

## Features

### 1. Computer Vision Analysis
- Utilizes a pre-trained medical imaging model (**ResNet50**) from `torchxrayvision`.
- Identifies common pathologies in chest X-rays (e.g., pneumonia, effusion, atelectasis).

### 2. OpenAI GPT-4 Integration
- Processes findings extracted from the X-ray analysis.
- Generates detailed diagnostic insights and explanations.
- Provides patient-friendly descriptions of complex medical terms.

### 3. User-Friendly Interface
- Built with **Streamlit** for a simple and intuitive user experience.
- Allows users to upload medical images and receive real-time results.

---

## How It Works

1. **Upload Image**: Users upload a chest X-ray image (supported formats: JPG, JPEG, PNG).
2. **Image Preprocessing**: The image is converted to grayscale, resized, and normalized for analysis.
3. **Disease Prediction**:
   - A pre-trained `torchxrayvision` model (`resnet50-res512-all`) identifies possible abnormalities.
   - Outputs confidence scores for detected conditions.
4. **Textual Analysis**:
   - The findings from the image analysis are sent to OpenAI's GPT-4 model.
   - GPT-4 provides a comprehensive diagnostic report and suggestions.
5. **Results Display**: The diagnostic report is presented in a user-friendly format.

---

## Installation

### Prerequisites
- Python 3.12

### Clone the Repository
```bash
git clone https://github.com/sachnaror/ai_medical_image_analysis.git
cd medical-imaging-diagnosis-agent
```

### Install Dependencies
Create a virtual environment and install the required Python packages:
```bash
pip install -r requirements.txt
```

### Run the Application
Launch the Streamlit application:
```bash
streamlit run medical_image.py
```

---

## File Structure

```plaintext
medical-imaging-diagnosis-agent/
├── medical_image.py       # Main application file
├── requirements.txt       # Required Python dependencies
└── README.md              # Project documentation
```

---

## Dependencies

- **openai**: For GPT-4 integration
- **streamlit**: For building the web-based interface
- **torchxrayvision**: For chest X-ray analysis
- **torch**: Required by `torchxrayvision`
- **torchvision**: Required for image transformations
- **Pillow**: For image processing

Install these dependencies using the `requirements.txt` file:
```plaintext
openai>=0.27.0
streamlit>=1.21.0
Pillow>=10.0.0
torch>=1.9.0
torchvision>=0.10.0
torchxrayvision>=0.0.32
```

---

## Usage

1. Open the application in your browser after starting the Streamlit server.
2. Enter your OpenAI API Key in the sidebar.
3. Upload a chest X-ray image.
4. Click the **Analyze Image** button to view predictions and a detailed diagnostic report.

---

## Example Output

### Input:
A chest X-ray image of a patient.

### Output:
**Predicted Pathologies:**
```plaintext
- Pneumonia: 0.85
- Effusion: 0.78
- Atelectasis: 0.65
```

**Diagnostic Report:**
```markdown
### Comprehensive Image Analysis
1. Scan Type: Chest X-ray
2. Abnormalities: Pneumonia and Effusion detected.

### Diagnostic Insights
- Pneumonia: High likelihood.
- Effusion: Moderate likelihood.
- No significant findings of masses or fractures.

### Patient-Friendly Explanation
Your chest X-ray indicates possible pneumonia and fluid buildup (effusion). Please consult your healthcare provider for further evaluation and treatment.
```

---

## Disclaimer
This tool is for **educational purposes only**. All analyses should be reviewed by qualified healthcare professionals. Do not make medical decisions based solely on this application.

---

## License
This project is licensed under the [MIT License](LICENSE).

---


## 📩 Contact

| Name              | Details                             |
|-------------------|-------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                      |
| **📧 Email**       | [sachnaror@gmail.com](mailto:sachnaror@gmail.com) |
| **📍 Location**    | Noida, India                       |
| **📂 GitHub**      | [github.com/sachnaror](https://github.com/sachnaror) |
| **🌐 Website**     | [https://about.me/sachin-arora](https://about.me/sachin-arora) |
| **📱 Phone**       | [+91 9560330483](tel:+919560330483) |

