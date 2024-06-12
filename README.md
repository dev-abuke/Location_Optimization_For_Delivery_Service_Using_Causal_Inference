# Logistic Optimization with Causal Inference

## Project Overview
This project aims to optimize the placement of Gokada drivers to increase the fraction of completed delivery orders using causal inference methodologies. The project involves data exploration, feature engineering, and causal analysis to identify the primary causes of unfulfilled requests and recommend optimal driver locations.

## Business Need

**Client:** Gokada, a last-mile delivery service in Nigeria.

**Business Need:** Optimize the placement of drivers (referred to as pilots) to increase the fraction of completed delivery orders.

**Key Issue:** Sub-optimal placement of drivers leading to a high number of unfulfilled requests.

**Proposed Methodology:** Use Causal Inference to understand the primary causes of unfulfilled requests and recommend optimal driver locations.


## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/dev-abuke/Location_Optimization_For_Delivery_Service_Using_Causal_Inference CausalInference
    ```
2. Navigate to the project directory:
    ```bash
    cd CausalInference
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the notebooks and scripts as needed.

## Requirements
- Python 3.11
- pandas
- geopy
- numpy
- matplotlib
- seaborn
- meteostat

# Plan

## 1. Data Exploration

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

## 2. Creative Visualization

### Interactive Web-Based Visualization
- Develop an interactive visualization to tell a story (e.g., similar to "A Day in the Life" of a NYC taxi).
- Use Python libraries like Flask or Streamlit for web-based visualizations.

## 3. Causal Learning

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

## 4. Logistic Optimization

### Integer and Linear Programming
- Read references on integer and linear programming optimization.
- Transform data to be suitable for placement optimization.
- Explore ML and optimization techniques for driver placement.

## Code Structure

      ├── notebooks
      │   ├──
      │   └── 
      ├── data
      │   ├── nb.csv                # Completed Orders
      │   └── driver_locations
      │       _during_request.csv   # Delivery Requests
      │  
      ├── Dockerfile                # Docker configuration
      ├── docker-compose.yml        # Docker Compose configuration
      ├── requirements.txt          # List of dependencies required for the project
      ├── README.md                 # Project documentation
      └── notebooks                 # Jupyter notebooks for experimentation and development

## Directory Structure
- `data/`: Contains sample data files.
- `notebooks/`: Jupyter notebooks for data exploration and feature engineering.
- `scripts/`: Python scripts for data processing and causal inference.
- `README.md`: Project overview and instructions.
- `Interim_Submission_Report.pdf`: Interim submission report.

## Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss your changes.
