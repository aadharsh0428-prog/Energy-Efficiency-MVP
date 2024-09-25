import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Function to render the home page
def render_home_page():
    st.title("Energy Efficiency and Renovation Opportunities in Germany")

    st.markdown("""
    ### Market Opportunity
    - **Energy Efficiency Demand**: Buildings in Germany consume **35%** of total energy, creating a huge demand for efficiency solutions.
    - **Renovation Backlog**: **7.3 million** private buildings need renovation, presenting a vast market opportunity.
    - **Regulatory Pressure and Incentives**: Stringent regulations and incentives make energy-efficient renovations a top priority.
    
    ### Challenges
    - **Aging Building Infrastructure**: Many German buildings are outdated, leading to inefficient energy consumption and high wastage.
    - **High Renovation Costs**: The expense of upgrading to modern, energy-efficient systems is a significant barrier for many property owners.
    - **Complex Regulatory Compliance**: Navigating the complex regulations for energy efficiency can be daunting for both homeowners and businesses.
    - **Seasonal Energy Demand Fluctuations**: Germany's climate causes significant seasonal variations in energy demand, straining existing infrastructure.
    
    ### Tech Stack
    - **AI & Machine Learning**: Predictive analytics for energy usage and building assessment.
    - **IoT and Smart Sensors**: Real-time energy monitoring and smart home integration.
    - **Data Analytics**: Big data processing to analyze energy patterns and trends.
    - **Cloud Computing**: Scalable infrastructure for secure data storage and processing.

    ### Rising Trends
    - **Rising Energy Costs**: Increasing energy prices drive demand for cost-saving, energy-efficient technologies.
    - **Sustainable Living Movement**: Growing consumer interest in sustainability fuels the market for eco-friendly homes.
    """)

    # Button to navigate to the MVP page
    if st.button("Go to MVP"):
        # Use query params to "navigate" to the MVP
        st.experimental_set_query_params(page="mvp")

# Function to render the MVP page
def render_mvp_page():
    st.title('MVP: Energy Consumption Predictions and Renovation Suggestions')

    # Button to go back to the home page
    if st.button("Go Back to Home"):
        st.experimental_set_query_params(page="home")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        st.write("Data Preview:")
        st.write(df.head())

        # Check if required columns are present
        if 'building_renovation_percent' not in df.columns or 'id' not in df.columns:
            st.error("The CSV file must contain 'building_renovation_percent' and 'id' columns.")
        else:
            # Feature and target selection
            X = df.drop(['building_renovation_percent', 'id'], axis=1)  # Drop target and ID
            y = df['building_renovation_percent']

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Standardize the data
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            st.write("Data has been split and scaled.")

            # Train the XGBoost model
            xg_reg = xgb.XGBRegressor(
                objective='reg:squarederror',  # Objective function for regression
                n_estimators=100,              # Number of boosting rounds
                random_state=42
            )
            xg_reg.fit(X_train_scaled, y_train)

            st.success("XGBoost model has been trained successfully!")

            # Make predictions on the test set
            y_pred = xg_reg.predict(X_test_scaled)

            # Evaluate the model
            mse = mean_squared_error(y_test, y_pred)
            st.write(f"Model Mean Squared Error: {mse:.2f}")

            # Visualization: Scatter Plot of Actual vs Predicted Values
            st.write("Scatter Plot of Actual vs Predicted Values:")
            fig, ax = plt.subplots()
            ax.scatter(y_test, y_pred, color='blue', alpha=0.7)
            ax.set_xlabel('Actual Values')
            ax.set_ylabel('Predicted Values')
            ax.set_title('Actual vs Predicted Building Renovation Percent')
            ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Line for perfect predictions
            st.pyplot(fig)

            # Optional: Show top 3 feature importance as a bar chart
            if st.checkbox("Show Top 3 Feature Importance Bar Chart"):
                importances = xg_reg.feature_importances_
                feature_names = X.columns
                feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})

                # Sort by importance and select the top 3 features
                top_3_features = feature_importance_df.nlargest(3, 'Importance')

                # Convert to percentages
                top_3_features['Importance'] = top_3_features['Importance'] * 100

                # Plot bar chart
                fig, ax = plt.subplots()
                ax.barh(top_3_features['Feature'], top_3_features['Importance'], color='skyblue')
                ax.set_xlabel('Importance (%)')
                ax.set_title('Top 3 Feature Importance')
                plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature on top

                st.pyplot(fig)

# Get the query parameters from the URL
query_params = st.experimental_get_query_params()

# Check if the "page" query param is set, and render the corresponding page
if "page" in query_params and query_params["page"][0] == "mvp":
    render_mvp_page()
else:
    render_home_page()
