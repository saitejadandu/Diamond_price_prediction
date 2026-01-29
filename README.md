💎 Diamond Price Prediction using KNN & Streamlit

This project is an end-to-end Machine Learning application developed to predict diamond prices based on their physical and quality attributes. The model uses the K-Nearest Neighbors (KNN) regression algorithm and is deployed as an interactive web application using Streamlit Cloud.

The dataset used for this project is diamonds.csv, which contains features such as carat weight, cut, color, clarity, depth, and table. The target variable is the diamond price. The data is loaded using pandas, split into training and testing sets in a 75:25 ratio, and preprocessed by encoding categorical variables and scaling numerical features. A KNN regression model is trained using scikit-learn and evaluated using MAE, RMSE, and R² score. The trained pipeline is saved using pickle for reuse during deployment.

A Streamlit application is created to load the saved model and take user input for diamond attributes. Based on the provided inputs, the app predicts and displays the estimated diamond price in a clear and user-friendly interface. The entire application is deployed on Streamlit Cloud, making it accessible through a public URL.


🚀 Deployment

The application is deployed on Streamlit Cloud. The deployment link has been submitted in the Discord submission channel as required for the assignment. The requirements.txt file ensures all dependencies are installed correctly during deployment.

<img width="928" height="881" alt="Screenshot 2026-01-30 012334" src="https://github.com/user-attachments/assets/4ff79d0c-256e-43f6-b8c7-3601507fff01" />


🛠 Technologies Used

Python, Pandas, NumPy, Scikit-learn, Streamlit, and Pickle are used to build, train, and deploy the application.

✅ Conclusion

This project demonstrates a complete machine learning workflow, starting from data preprocessing and model training to deployment as a web application. It highlights practical implementation of KNN regression and real-world ML deployment using Streamlit Cloud.
