import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model
model = joblib.load('music_clustering_model.pkl')

# Define feature columns used in the original clustering
features = [
    "Beats Per Minute (BPM)", "Energy", "Danceability", "Loudness (dB)",
    "Liveness", "Valence", "Length (Duration)", "Acousticness", "Speechiness", "Popularity"
]

def predict_cluster(input_data):
    # Prepare the input data
    input_df = pd.DataFrame([input_data], columns=features)
    
    # Scale the input data 
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(input_df)
    
    # Predict the cluster
    cluster = model.predict(X_scaled)[0]
    return cluster

def main():
    st.title('Music Genre Clustering Predictor')
    st.write('Enter the characteristics of a song to predict its cluster')

    # Create input fields for each feature
    input_data = {}
    for feature in features:
        if feature in ["Beats Per Minute (BPM)", "Energy", "Danceability", "Liveness", "Valence", "Acousticness", "Speechiness", "Popularity"]:
            input_data[feature] = st.slider(
                feature, 
                min_value=0, 
                max_value=100, 
                value=50
            )
        elif feature == "Loudness (dB)":
            input_data[feature] = st.slider(
                feature, 
                min_value=-60, 
                max_value=0, 
                value=-10
            )
        elif feature == "Length (Duration)":
            input_data[feature] = st.number_input(
                feature + " (seconds)", 
                min_value=0, 
                max_value=1000, 
                value=200
            )

    # Predict button
    if st.button('Predict Cluster'):
        cluster = predict_cluster(input_data)
        
        # Cluster descriptions based on the original analysis
        cluster_descriptions = {
            0: "High danceability and BPM values",
            1: "More acoustic, low energy level",
            2: "Popular and energetic tracks",
            3: "Lower popularity, experimental or niche music",
            4: "Cluster 4 details",
            5: "Cluster 5 details",
            6: "Cluster 6 details"
        }
        
        st.success(f'Predicted Cluster: {cluster}')
        st.write(f'Cluster Description: {cluster_descriptions.get(cluster, "Unknown Cluster")}')

if __name__ == '__main__':
    main()
    