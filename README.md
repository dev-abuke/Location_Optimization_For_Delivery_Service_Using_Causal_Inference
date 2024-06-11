## Logistic Optimization with Causal Inference

## Overview

Client: Gokada, a last-mile delivery service in Nigeria.

Business Need: Optimize the placement of drivers (referred to as pilots) to increase the fraction of completed delivery orders.

Key Issue: Sub-optimal placement of drivers leading to a high number of unfulfilled requests.

Proposed Methodology: Use Causal Inference to understand the primary causes of unfulfilled requests and recommend optimal driver locations.

# Plan

1. ## Data Exploration

### Conduct Exploratory Data Analysis (EDA)
- Load and inspect the datasets.
- Identify and handle missing values.
- Detect and treat outliers.
- Visualize data distributions and relationships.

### Feature Engineering
- Create new features based on time and location (e.g., rain, holiday, traffic conditions).
- Compute distances, driving speed, shortest distance, and driving route distance between geographic coordinates.
- Determine the number of riders and orders in 500m circles from accepted and unfulfilled orders.
- Cluster delivery starting locations and destinations.

### Visualization
- Use purpose-driven visualization tools like Datashader.
- Create visualizations to communicate insights effectively.

2. ## Creative Visualization

### Interactive Web-Based Visualization
- Develop an interactive visualization to tell a story (e.g., similar to "A Day in the Life" of a NYC taxi).
- Use Python libraries like Flask or Streamlit for web-based visualizations.

3. ## Causal Learning

### Data Splitting
- Split the data into training and hold-out sets.

### Causal Graph Creation
- Create causal graphs using all training data.
- Compare causal graphs with the ground truth using metrics like the Jaccard Similarity Index.

### Causal Inference Tasks
- Use the do operation to answer questions about the impact of different interventions (e.g., drivers moving 1km every 30 mins).

### Machine Learning Models
- Train ML models using all variables and variables selected by the causal graph.
- Evaluate model performance and overfitting on the hold-out set.

4. ## Logistic Optimization

### Integer and Linear Programming
- Read references on integer and linear programming optimization.
- Transform data to be suitable for placement optimization.
- Explore ML and optimization techniques for driver placement.
