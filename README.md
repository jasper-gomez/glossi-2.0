### 📈Glossi 2.0
An upgraded version of Glossi utilizing an interdisciplinary analytical approach.

##### [View Interactive Simulation](https://insightmaker.com/insight/1SV8tCmE31FiyYMc5VyI0s)

---

### 💡Objective
Glossi 2.0 aims to create a digital simulation of the hair data I gathered during Glossi 1.0. Through an interdisciplinary analytical pipeline (Machine Learning + Stochastic System Dynamics + HPC), this models the dynamics of hair dryness.

---

### ⚙️Methodology
1. **Data Gathering**: Data used is from Glossi 1.0.
2. **Data Preprocesing**: The data has undergone numerical encoding using `LabelEncoder`, feature selection using [`FeSeCo`](https://github.com/jasper-gomez/feature-selection-companion), and feature engineering.
3. **Model Development**: Developed a simple Linear Regression (LR) model.
4. **Coefficient Extraction**: Using the LR model, the coefficients and intercept have been used as empirical ground truth for system parameters.
5. **Simulation Modeling**: Created a Stochastic SD model in Vensim.
6. **Model Recalibration**: Conducted a structural parameter recalibration to optimize model behavior and eliminate systemic bias and variance error.

---

### 📝Evaluation Results (Linear Regression)
- **R2 Score**: 0.40240082566198 (Good enough for human factors)
- **MSE**: 0.7029867489580465
- **MAE**: 0.5328669897213666
- **RMSE**: 0.8384430505156844
- **Explained Variance Score**: 0.4531095763392293

---

### 🔍Findings (Linear Regression)

#### **Target Variable**: average_dryness

#### **Intercept**: 4.914931200064931

**Coefficients**
- `shampoo_used_today`: 0.64707195
- `conditioner_used_today`: - 0.02906673
- `leave_in_amt`: - 0.2646154
- `sweat`: - 0.03489914
- `humidity`: - 0.01720086
- `bath_intensity`: - 0.01400846
- `wind_exposure`: 0.06599629

---

### 🔧Model Recalibration (Simulation Model)

#### **Optimal Scaling Factor**: 5.05
**Theil's Statistics**
- MSE: 3.4878
- $U^m = 0.0$ (Bias Proportion)
- $U^s = 0.0$ (Variance Proportion)
- $U^c = 1.0$ (Covariation Proportion)