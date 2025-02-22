# 🏥 Disease Outbreak Prediction using Machine Learning

This project is a **Machine Learning-powered Disease Prediction System** built using **Streamlit**. It predicts the likelihood of an individual having **Diabetes, Heart Disease, or Parkinson’s Disease** based on user input.

## 🚀 Features
- **Diabetes Prediction** 🩸
- **Heart Disease Prediction** ❤️
- **Parkinson’s Disease Prediction** 🧠
- Interactive UI using **Streamlit**
- Deployed on **Streamlit Cloud**

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** (for UI)
- **Scikit-learn** (Machine Learning models)
- **Pandas & NumPy** (Data Processing)
- **Pickle** (Model Serialization)
- **Git & GitHub** (Version Control)

---

## 📂 Project Structure
```
📁 disease-outbreak-prediction
│-- 📁 training_model
│   ├── diabetes_model.sav
│   ├── heart_model.sav
│-- app.py
│-- requirements.txt
│-- README.md
```

---

## 🎯 How to Run the Project Locally

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/vidhya1312lakshmi/disease-outbreak-prediction.git
cd disease-outbreak-prediction
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```sh
streamlit run app.py
```

---

## 🌐 Deployment on Streamlit Cloud
### **Steps to Deploy:**
1. Push the project to **GitHub**.
2. Go to **[Streamlit Cloud](https://share.streamlit.io/)** and sign in with GitHub.
3. Click **“New App”** → Select **your repository**.
4. In "Main file path", enter:
   ```
   app.py
   ```
5. Click **Deploy** 🎉

---

## 🐞 Troubleshooting
- **GitHub Push Error (`Updates were rejected`)**
  ```sh
  git pull origin main --rebase
  git push origin main
  ```
- **Streamlit Not Detecting Repo?**
  - Ensure the repository is **public**.
  - Reconnect GitHub in **Streamlit Cloud Settings**.
- **Error Installing Requirements?**
  - Ensure `requirements.txt` has only necessary dependencies.
  - Run `pip freeze > requirements.txt` and update GitHub.

---

## 👥 Contributors
- **[Vidhya Lakshmi](https://github.com/vidhya1312lakshmi)**

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

