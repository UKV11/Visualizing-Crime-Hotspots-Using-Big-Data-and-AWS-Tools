# Crime Data Analysis and Visualization

This project focuses on visualizing crime hotspots across the United States using publicly available FBI crime data and advanced data processing and visualization techniques. The project leverages big data tools such as AWS Quicksight, Amazon EMR, and Apache Spark to deliver meaningful insights into crime patterns.

---

## Project Objectives

- **Analyze crime trends**: Investigate how crime rates have changed over the years.
- **Visualize crime hotspots**: Use interactive maps to highlight regions with high crime rates.
- **Crime type comparison**: Understand which types of crimes are most prevalent in different states.
- **Assist stakeholders**: Provide insights for law enforcement, policymakers, and the public.

---

## Process Workflow

The project follows a structured workflow, as depicted below:

### Architecture

![Architecture]![architecture](https://github.com/user-attachments/assets/f0370a6c-7e6a-4132-8aae-ff6180313805)


1. **Data Collection**: Crime data was obtained from the FBI API, covering multiple crime types across states and years.
2. **Data Storage**: Raw data was stored in Amazon S3 for scalable storage.
3. **Data Processing**: Data was cleansed and transformed using PySpark on Amazon EMR clusters.
4. **Data Storage**: Processed data was stored back in S3 for visualization.
5. **Visualization**: AWS Quicksight was used to create dashboards, including maps and interactive filters.

---

## Features

### 1. **Visualization of Crime Hotspots**

Using hotspot mapping techniques, this visualization helps identify regions with high crime intensities. 

#### Example:
[Hotspot Visualization]![Hypothesis1](https://github.com/user-attachments/assets/1b2cf9b1-3079-440c-b0fc-9644a6139723)


- **Goal**: Assist law enforcement in focusing resources on high-crime areas.
- **Insight**: Highlighted regions can be filtered by crime type and year.

---

### 2. **Crime Rates Across States**

Interactive dashboards visualize the distribution of crime rates by state.

#### Example:
[Crime Rates Visualization]![Hypothesis2](https://github.com/user-attachments/assets/dc3194bd-3caa-4945-a05d-f0c2be6c73a9)


- **Goal**: Provide insights into state-specific crime patterns.
- **Insight**: Enables users to drill down into individual state data.

---

### 3. **Crime Type Analysis**

Analyze the prevalence of various crime types across different states.

#### Example:
![Crime Type Analysis]![Hypothesis3](https://github.com/user-attachments/assets/2b5b4cbf-2b4d-49d6-b7c5-43216e6ba9d0)


- **Goal**: Understand dominant crime types by state.
- **Insight**: Supports tailored strategies to tackle specific crime types.

---

## Skills Used

- **Big Data Processing**:
  - **Apache Spark**: For distributed data processing.
  - **Amazon EMR**: To manage Spark clusters and execute transformations.

- **Cloud Computing**:
  - **Amazon S3**: For scalable storage of raw and processed data.
  - **AWS Quicksight**: To build interactive dashboards for visualization.

- **Data Analysis**:
  - Cleaning and transforming large datasets.
  - Statistical insights into crime trends.

- **Visualization**:
  - Interactive mapping and dashboarding.
  - Charting and filtering for trend analysis.

---

## Key Insights

- **Crime Trends**: Crime rates have fluctuated significantly over the past decade, with notable spikes in violent crimes.
- **Crime Hotspots**: High-crime areas can be visualized and prioritized for law enforcement efforts.
- **Interactive Dashboards**: Provide flexible analysis options for stakeholders, including filters by crime type, year, and location.

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/crime-analysis
   ```
2. Install dependencies for data preprocessing and visualization.
3. Upload the data files to S3 for processing.
4. Use the Quicksight dashboard link to explore visualizations interactively.

---

## Future Enhancements

- **Automated Data Pipeline**: Enable real-time updates from the FBI API.
- **Predictive Modeling**: Use machine learning to forecast future crime trends.
- **Integration with Public Platforms**: Provide public access to hotspots for safety awareness.

---

## Acknowledgements

- **FBI**: For providing the crime dataset.
- **AWS**: For supporting the big data infrastructure.
- **Professor Fitzroy Nembhard**: For guidance and mentorship.

---

Feel free to explore the project and contribute enhancements!
