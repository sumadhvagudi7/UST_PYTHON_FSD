# 🫀 Heart Health Data Insights Challenge

## 📘 Dataset Overview

The dataset contains medical information used to predict the presence of heart disease (AHD).  
Each row represents a patient record with attributes such as age, cholesterol, resting blood pressure, and heart disease diagnosis.

**Columns:**
- `Age`: Age of the patient  
- `Sex`: 1 = male, 0 = female  
- `ChestPain`: Type of chest pain (typical angina, asymptomatic, etc.)  
- `RestBP`: Resting blood pressure (mm Hg)  
- `Chol`: Serum cholesterol (mg/dl)  
- `Fbs`: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)  
- `RestECG`: Resting electrocardiographic results  
- `MaxHR`: Maximum heart rate achieved  
- `ExAng`: Exercise-induced angina (1 = yes; 0 = no)  
- `Oldpeak`: ST depression induced by exercise  
- `Slope`: Slope of the peak exercise ST segment  
- `Ca`: Number of major vessels colored by fluoroscopy (0–3)  
- `Thal`: Thalassemia type (normal, fixed defect, reversible defect)  
- `AHD`: Presence of heart disease (Yes/No)

---

## 🎯 Objective

You are required to perform **exploratory data analysis (EDA)** and create **insightful visualizations** that help understand key factors influencing heart disease.

Use:
- **Pandas** for data handling and summarization  
- **Seaborn** and **Matplotlib** for visualization

---

## 🧩 Tasks / Questions

### **1️⃣ Basic Data Understanding**
- Display the first 5 rows and use `.info()` and `.describe()` to summarize the dataset.  
- Plot the **distribution of Age** using a histogram.  
  *Hint:* Use `plt.hist()` or `sns.histplot()`.

---

### **2️⃣ Gender Distribution**
- Create a **count plot** showing the number of males and females in the dataset.  
  *Hint:* Use `sns.countplot(x='Sex', data=df)` and label axes properly.

---

### **3️⃣ Age vs. Heart Disease**
- Plot a **boxplot** of `Age` grouped by `AHD` (Heart Disease).  
  *Goal:* Visualize if certain age groups are more prone to heart disease.

---

### **4️⃣ Cholesterol and Heart Disease**
- Plot a **violin plot** of `Chol` (Cholesterol) against `AHD`.  
  *Goal:* Observe how cholesterol levels differ between those with and without heart disease.

---

### **5️⃣ Resting Blood Pressure Distribution**
- Plot the **distribution of RestBP** and mark the mean value using a vertical line.  
  *Hint:* Use `sns.histplot(df['RestBP'], kde=True)` and `plt.axvline()`.

---

### **6️⃣ Correlation Heatmap**
- Compute and visualize the **correlation matrix** among numerical features using a heatmap.  
  *Hint:* Use `sns.heatmap(df.corr(), annot=True, cmap='coolwarm')`.

---

### **7️⃣ Pairwise Relationships**
- Use `sns.pairplot()` to plot relationships between **Age**, **Chol**, **RestBP**, and **MaxHR**, colored by `AHD`.  
  *Goal:* Detect any visible patterns or separations between healthy and diseased individuals.

---

### **8️⃣ Chest Pain Type and Heart Disease**
- Create a **bar plot** showing the proportion of heart disease cases by `ChestPain` type.  
  *Hint:* Group data using `df.groupby('ChestPain')['AHD'].value_counts(normalize=True).unstack()`.

---

### **9️⃣ Exercise-Induced Angina Impact**
- Plot a **stacked bar chart** showing the count of `ExAng` values (exercise-induced angina) across `AHD`.  
  *Goal:* Show how exercise-induced angina correlates with heart disease occurrence.

---

### **🔟 Combined Risk Analysis**
- Create a **scatter plot** of `Age` vs. `MaxHR`, with:
  - Color representing `AHD`
  - Size representing `Chol`
  *Hint:* Use `sns.scatterplot(x='Age', y='MaxHR', hue='AHD', size='Chol', sizes=(20,200))`.

---

## 🧠 Bonus Challenge (Optional)
Create a **custom dashboard-style layout** with subplots using `plt.subplots()` to display:
1. Age distribution  
2. Cholesterol distribution  
3. Count of heart disease by gender  

---

## 🧰 Required Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
```

---

## 📊 Learning Outcomes
By the end of this exercise, students will:
- Learn to clean, summarize, and explore medical datasets using Pandas  
- Use Seaborn and Matplotlib for creating statistical visualizations  
- Interpret patterns and relationships between features and disease presence  
- Understand the EDA workflow in health data analysis
