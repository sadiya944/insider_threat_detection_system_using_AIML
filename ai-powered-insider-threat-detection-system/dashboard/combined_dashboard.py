import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import os
from login import login_page

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# -----------------------------
# Login
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
    st.stop()

st.sidebar.title("Navigation")

st.sidebar.success(
    f"Welcome {st.session_state.user['username']}"
)

st.sidebar.write(
    f"Role : {st.session_state.user['role']}"
)

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

if st.session_state.user["role"] == "Admin":
    if st.button("Retrain Model"):
        st.success("Model Retrained")

# -----------------------------
# Page
# -----------------------------
st.set_page_config(layout="wide")
st.title("AI-Powered Insider Threat Detection: Combined Dashboard")


# -----------------------------
# Load Data
# -----------------------------
def load_all_data():

    files = [
        "merged_features.csv",
        "anomaly_scores.csv",
        "file_access.csv",
        "usb_usage.csv"
    ]

    for f in files:
        path = os.path.join(DATA_DIR, f)
        st.write(f"{path} : {os.path.exists(path)}")

    features_path = os.path.join(DATA_DIR, "merged_features.csv")
    scores_path = os.path.join(DATA_DIR, "anomaly_scores.csv")
    file_access_path = os.path.join(DATA_DIR, "file_access.csv")
    usb_usage_path = os.path.join(DATA_DIR, "usb_usage.csv")

    features = pd.read_csv(features_path)

    scores = pd.read_csv(scores_path)

    file_access = pd.read_csv(
        file_access_path,
        parse_dates=["access_time"]
    )

    usb_usage = pd.read_csv(
        usb_usage_path,
        parse_dates=["plug_time", "unplug_time"]
    )

    return (
        features,
        scores,
        file_access,
        usb_usage
    )


features, scores, file_access, usb_usage = load_all_data()

df = pd.merge(
    features,
    scores,
    on="user"
)
## System Overview
This system detects insider threats by analyzing user behavior, system access, and relationships using advanced machine learning and graph analysis techniques.

---

### 1. **Data Simulation & Feature Engineering**
- **Simulated Logs:** The system generates synthetic logs for user logins, file access, USB usage, and emails, mimicking real organizational activity.
- **Feature Engineering:** Extracts features such as:
    - Login/logout patterns (mean hours, frequency)
    - File/USB/email activity rates
    - Out-of-session file access
    - Graph centrality (degree, betweenness)
    - NLP features from email subjects (keyword flags, length)

---

### 2. **Anomaly Detection Algorithms**
- **Isolation Forest**
    - *Mathematics:* Randomly partitions data to isolate points. Anomalies are isolated faster (shorter average path length in trees).
    - *Computer Science:* Ensemble of binary trees; each tree splits on random features/values. The anomaly score is based on the average path length to isolate a sample.
- **One-Class SVM**
    - *Mathematics:* Finds a boundary in feature space that encloses most data (support vectors). Points outside are anomalies.
    - *Computer Science:* Uses kernel methods (e.g., RBF) to map data to high-dimensional space and find a maximal margin hyperplane.
- **Autoencoder**
    - *Mathematics:* Neural network learns to compress and reconstruct input. High reconstruction error indicates anomaly.
    - *Computer Science:* Trains a feedforward neural network (MLP) to minimize reconstruction loss (MSE) between input and output.

---

### 3. **Graph Analysis**
- **Entity Graph:** Users, files, and devices are nodes; edges represent access or usage.
- **Centrality Measures:**
    - *Degree Centrality:* Number of connections (activity level).
    - *Betweenness Centrality:* Frequency a node lies on shortest paths (potential for information flow/control).
- **At-Risk Subgraph:** Focuses on high-risk users and their direct connections for visualization and investigation.

---

### 4. **Explainability**
- **SHAP (SHapley Additive exPlanations):**
    - *Mathematics:* Based on cooperative game theory; attributes model output to each feature by averaging over all possible feature orderings.
    - *Computer Science:* Computes feature importances for each prediction, helping analysts understand why a user is flagged.
- **LIME (Local Interpretable Model-agnostic Explanations):**
    - *Mathematics:* Fits a simple, interpretable model locally around a prediction to approximate the complex model.
    - *Computer Science:* Perturbs input data and observes output changes to estimate feature influence (not supported for Isolation Forest, but available for other models).

---

### 5. **Dashboard & Visualization**
- **Streamlit:** Interactive web app for data exploration, anomaly review, and graph visualization.
- **PyVis/NetworkX:** Renders interactive network graphs for at-risk nodes and their relationships.

---

### 6. **Red Team Simulation**
- Injects malicious behaviors (after-hours access, mass downloads, suspicious USB usage) to test detection capability.

---

## Summary
This system combines unsupervised machine learning, graph theory, and explainable AI to provide a robust, interpretable approach to insider threat detection.
''') 
