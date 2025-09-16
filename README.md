# Disease Prediction System

## Overview
The Disease Prediction System is a comprehensive web application designed to predict and analyze diseases such as cancer, diabetes, heart disease, HIV, kidney disease, and liver disease. It leverages machine learning models to provide accurate predictions and visualizations, aiding users in health management and risk assessment.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)
- [Screenshots](#screenshots)
- [Notes](#notes)
- [FAQ](#faq)
- [References](#references)

---

## Features
- **Disease Prediction:** Predicts risk for cancer, diabetes, heart disease, HIV, kidney disease, and liver disease using user input and historical data.
- **Dashboard:** Centralized dashboard for monitoring predictions and results.
- **User Management:** Registration, login, and profile management.
- **Results Visualization:** View and download prediction results.
- **History Tracking:** Track previous predictions for each user.

---

## Project Structure
```
Disease Prediction system/
├── Health_check/
│   ├── accounts/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   ├── cancer/
│   │   ├── breast-cancer.csv
│   │   ├── train_model.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── ml_model/
│   │   │   └── model.pkl
│   │   └── templates/
│   ├── diabetes/
│   │   ├── diabetes.csv
│   │   ├── train_model.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── ml_model/
│   │   │   └── model.pkl
│   │   └── templates/
│   ├── dashboard/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   ├── heart/
│   │   ├── heart.csv
│   │   ├── train_model.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── ml_model/
│   │   │   └── model.pkl
│   │   └── templates/
│   ├── hiv/
│   │   ├── hiv.csv
│   │   ├── train_model.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── ml_model/
│   │   │   └── model.pkl
│   │   └── templates/
│   ├── kidney/
│   │   ├── kidney.csv
│   │   ├── train_model.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── ml_model/
│   │   │   └── model.pkl
│   │   └── templates/
│   ├── liver/
│   │   ├── liver.csv
│   │   ├── train_model.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── ml_model/
│   │   │   └── model.pkl
│   │   └── templates/
│   ├── Health_Check_AI/
│   │   ├── utils.py
│   │   └── ...
│   ├── db.sqlite3
│   └── manage.py
├── README.md
├── requirements.txt
```

---

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates
- **Machine Learning:** scikit-learn, pandas, numpy
- **Database:** SQLite3

---

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtualenv (recommended)

### Steps
1. **Clone the repository:**
   ```powershell
   git clone https://github.com/yourusername/Disease-Prediction-system.git
   cd Disease-Prediction-system/Health_check
   ```
2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install manually:
   ```powershell
   pip install django pandas numpy scikit-learn
   ```
4. **Apply migrations:**
   ```powershell
   python manage.py migrate
   ```
5. **Run the development server:**
   ```powershell
   python manage.py runserver
   ```
6. **Access the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

---

## Usage
- **Dashboard:** Main page for accessing disease prediction modules.
- **Disease Prediction:** Select a disease, input relevant health data, and get risk analysis.
- **Results:** Download and view prediction results.
- **History:** View previous predictions.

---

## Model Details
### Disease Prediction
- **Models:** Trained using scikit-learn (RandomForest, Logistic Regression, etc.)
- **Data:** CSV files for each disease (e.g., `breast-cancer.csv`, `diabetes.csv`)
- **Artifacts:** 
  - Model: `model.pkl`
  - Scaler: `scaler.pkl` (if used)

---

## API Endpoints
| Module              | Endpoint                      | Method | Description                       |
|---------------------|------------------------------|--------|-----------------------------------|
| Dashboard           | `/dashboard/`                | GET    | Main dashboard                    |
| Cancer Prediction   | `/cancer/`                   | GET/POST| Cancer prediction form & results  |
| Diabetes Prediction | `/diabetes/`                 | GET/POST| Diabetes prediction form & results|
| Heart Prediction    | `/heart/`                    | GET/POST| Heart prediction form & results   |
| HIV Prediction      | `/hiv/`                      | GET/POST| HIV prediction form & results     |
| Kidney Prediction   | `/kidney/`                   | GET/POST| Kidney prediction form & results  |
| Liver Prediction    | `/liver/`                    | GET/POST| Liver prediction form & results   |

---

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a Pull Request

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
- **Author:** Fateh Ullah
- **GitHub:** https://github.com/fatehullah778866
- **Email:** fatehullah.dev@gmail.com

For issues, suggestions, or contributions, please open an issue or contact via email.

---

## Acknowledgements
- scikit-learn, pandas, numpy
- Django Documentation
- Open source contributors

---

## Notes
- Ensure all model files (`.pkl`) are present in their respective folders.
- For production deployment, configure proper settings in `Health_Check_AI/settings.py` and use a robust database.

---

## FAQ
**Q:** What diseases does this system predict?  
**A:** Cancer, diabetes, heart disease, HIV, kidney disease, and liver disease.

**Q:** Can I use my own data?  
**A:** Yes, you can input your own health data for predictions.

**Q:** How do I retrain the models?  
**A:** Use the `train_model.py` scripts in each disease folder.