import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import plotly.express as px

st.title("📊 Data Explorer + Analytics Hub")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Summary Statistics
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Correlation Heatmap (numeric only)
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if not numeric_df.empty:
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns available for correlation heatmap.")

    # Interactive Scatter Plot
    st.write("### Interactive Scatter Plot")
    col_x = st.selectbox("X-axis", df.columns)
    col_y = st.selectbox("Y-axis", df.columns)
    fig = px.scatter(df, x=col_x, y=col_y, color=df.columns[0])
    st.plotly_chart(fig)

    # Linear Regression
    st.write("### Linear Regression")
    target = st.selectbox("Select target column", df.columns)
    features = st.multiselect("Select feature columns", df.columns)

    if features and target:
        X = df[features].select_dtypes(include=['float64','int64']).dropna()
        y = df[target].loc[X.index]

        model = LinearRegression().fit(X, y)
        preds = model.predict(X)

        # Metrics
        r2 = r2_score(y, preds)
        mse = mean_squared_error(y, preds)
        rmse = np.sqrt(mse)

        # Summary in a box
        with st.expander("📦 Linear Regression Model Summary"):
            st.write(f"**Target Variable:** {target}")
            st.write(f"**Features:** {features}")
            st.write(f"**Intercept:** {model.intercept_:.4f}")
            st.write(f"**Coefficients:** {dict(zip(features, model.coef_))}")
            st.write(f"**R² Score:** {r2:.4f}")
            st.write(f"**RMSE:** {rmse:.4f}")

        # Plot Actual vs Predicted
        st.line_chart(pd.DataFrame({"Actual": y, "Predicted": preds}))