# Energy-Efficiency-MVP

# Energy Efficiency and Renovation Prediction App

This web application leverages machine learning to predict building renovation percentages in Germany based on various energy consumption and building characteristic factors. Built using **Streamlit**, the app provides an intuitive interface to upload data, train an **XGBoost** model, and visualize results.

## Project Overview

With Germany’s aging building infrastructure and stringent energy efficiency regulations, the demand for renovation and sustainable energy solutions is growing rapidly. This project aims to help building owners, energy consultants, and policymakers estimate the potential energy savings and renovation requirements for buildings, using data-driven insights.

The app not only predicts building renovation percentages but also highlights the most critical factors driving energy inefficiency, providing valuable guidance for strategic investments.

### Key Components of the Application:

1. **Data Upload**: Users can upload a CSV file containing building and energy-related data.
2. **Machine Learning**: The app trains an XGBoost model using the uploaded data to predict building renovation percentages.
3. **Visualization**:
   - View actual vs. predicted building renovation percentages.
   - Explore the top features influencing the predictions through visual charts.
4. **Feature Importance**: Provides insights into which building characteristics or energy metrics are most important for the prediction task.

## Sample Use Cases

This tool can be valuable for various sectors involved in energy efficiency, building renovation, and sustainability. Some key use cases include:

### 1. **Energy Consultants and Auditors**:
   - **Problem**: Building auditors need to assess which buildings need the most urgent renovation to improve energy efficiency.
   - **Solution**: The app helps prioritize which buildings require renovation by predicting the percentage of renovation needed and identifying key inefficiency factors.

### 2. **Property Developers**:
   - **Problem**: Developers must understand the energy efficiency landscape of existing buildings before planning new constructions or renovations.
   - **Solution**: By using historical data, developers can estimate renovation efforts and associated costs, driving more accurate project planning and budget allocation.

### 3. **Government Policymakers**:
   - **Problem**: Policymakers require data-driven insights to push energy efficiency initiatives and allocate funds for building renovations.
   - **Solution**: The app can support policy decisions by analyzing patterns of energy inefficiency, highlighting which regions or building types have the most critical renovation needs.

### 4. **Homeowners and Property Owners**:
   - **Problem**: Homeowners may not know where to invest in renovation to maximize energy efficiency.
   - **Solution**: The app allows them to predict renovation needs based on existing energy consumption patterns and characteristics, providing a data-driven decision-making tool for upgrades.

## How to Run the Application

### Prerequisites

Ensure that you have the following installed:

- Python 3.8+
- Required Python libraries (see `requirements.txt`)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/aadharsh0428-prog/Energy-Efficiency-MVP.git
    cd Energy-Efficiency-MVP
    ```

2. **Install required dependencies**:
    Install the necessary libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    Start the application by running:
    ```bash
    streamlit run app.py
    ```

4. **Access the app**:
    Once the app is running, open your browser and navigate to `http://localhost:8501`. The home page will provide background information on energy efficiency and renovation opportunities in Germany. You can then navigate to the MVP page to upload a CSV file for predictions.

### CSV File Format

The CSV file you upload should contain at least the following columns:

- `id`: A unique identifier for each building.
- `building_renovation_percent`: The target variable representing the percentage of building renovation needed.
- Additional columns for features relevant to energy efficiency and building renovation, such as:
  - Energy consumption metrics (`energy_consumption_kwh`, `energy_market_eur_kwh`, etc.)
  - Building characteristics (`building_stock_characteristics`, `building_shell_performance`, etc.)
  - Environmental factors (`solar_radiation_kwh_m2`, `climatic_conditions`, etc.)

### Example Workflow

1. **Home Page**: The app starts by providing key information on energy efficiency challenges, regulatory pressures, and the renovation backlog in Germany.
   
2. **MVP Page**: Click on the "Go to MVP" button to access the CSV upload feature.

3. **Model Training and Prediction**: After uploading a CSV, the app will automatically train an XGBoost model on the provided data and display performance metrics such as Mean Squared Error (MSE).

4. **Visualization**: 
   - View actual vs. predicted building renovation percentages.
   - Optionally, view the top 3 most important features influencing the model’s predictions via a bar chart.

### Requirements

- **Python 3.8+**
- **Streamlit** for the interactive web app
- **Pandas** for data manipulation
- **Scikit-learn** for preprocessing and evaluation
- **XGBoost** for the regression model
- **Matplotlib** for data visualization

### License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as needed.

