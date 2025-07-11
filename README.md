<h1 align="center">🏦 Loan Approval Prediction System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Accuracy-84%25-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deployed%20With-Streamlit-red?style=for-the-badge" />
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>This project predicts whether a loan will be approved based on applicant details using a <strong>Logistic Regression</strong> model. The entire system is wrapped in an interactive <strong>Streamlit web application</strong>.</p>

---

<h2>🗃️ Dataset Summary</h2>

<ul>
  <li><strong>Total Records:</strong> 614 (train), 367 (test)</li>
  <li><strong>Total Features Used:</strong> 11</li>
  <li><strong>Target Variable:</strong> Loan_Status (1 = Approved, 0 = Rejected)</li>
  <li><strong>Missing Values:</strong> Handled with median/mean/random fill</li>
</ul>

<h3>🔑 Input Features</h3>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Gender</td><td>Male / Female</td></tr>
    <tr><td>Married</td><td>Yes / No</td></tr>
    <tr><td>Dependents</td><td>0 / 1 / 2 / 3+</td></tr>
    <tr><td>Education</td><td>Graduate / Not Graduate</td></tr>
    <tr><td>Self_Employed</td><td>Yes / No</td></tr>
    <tr><td>ApplicantIncome</td><td>Monthly income of applicant</td></tr>
    <tr><td>CoapplicantIncome</td><td>Monthly income of co-applicant</td></tr>
    <tr><td>LoanAmount</td><td>Requested loan amount</td></tr>
    <tr><td>Loan_Amount_Term</td><td>Repayment term (in months)</td></tr>
    <tr><td>Credit_History</td><td>Credit score flag (1 = good)</td></tr>
    <tr><td>Property_Area</td><td>Urban / Semiurban / Rural</td></tr>
  </tbody>
</table>

---

<h2>📊 Exploratory Data Analysis</h2>

<ul>
  <li>Right-skewed income distribution</li>
  <li><strong>Credit_History</strong> is the strongest predictor</li>
  <li>Visuals include countplots, histograms, and correlation heatmap</li>
</ul>

---

<h2>⚙️ Data Preprocessing</h2>

<ul>
  <li>Label Encoding for categorical variables</li>
  <li>StandardScaler used for numeric fields</li>
  <li>Custom pipeline built for smooth preprocessing + modeling</li>
</ul>

---

<h2>🧠 Model Training</h2>

<ul>
  <li><strong>Train/Test Split:</strong> 80% / 20%</li>
  <li><strong>Models Tested:</strong></li>
  <ul>
    <li>✔️ Logistic Regression (Selected)</li>
    <li>🌲 Decision Tree</li>
    <li>🌳 Random Forest</li>
    <li>🤖 KNN</li>
  </ul>
  <li><strong>Best Accuracy:</strong> <code>84%</code> with Logistic Regression</li>
</ul>

---

<h2>🌐 Streamlit Web Application</h2>

<ul>
  <li>Interactive loan form for user input</li>
  <li>Live prediction with results display</li>
  <li>Fast and responsive UI</li>
</ul>

<h3>🚀 Run Locally</h3>

```bash
# Clone repo
git clone https://github.com/your-username/loan-approval-prediction.git
cd loan-approval-prediction

# Install dependencies
pip install -r requirements.txt

# Start the app
streamlit run app.py
