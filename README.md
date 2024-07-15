# NYC Public School SAT Performance Analysis
This Python project utilizes pandas to analyze the performance data of public schools in New York City (NYC) based on SAT scores. The dataset schools.csv is provided and contains information about various schools including their borough, average math scores, average reading scores, average writing scores, and the percentage of students tested.
## Task
1.Identifying Top Math Performers:
 - Subset the data to find schools with math scores of at least 80% of the maximum possible score (800). Save the results in a pandas DataFrame called best_math_schools, including columns for school names and average math scores, sorted by average math scores in descending order.
2.Top 10 Schools Based on Combined SAT Scores:
 - Calculate the total SAT score for each school by summing the average math, reading, and writing scores. Identify and save the top 10 performing schools in a pandas DataFrame called top_10_schools, including school names and their total SAT scores, ordered by total SAT scores in descending order.
3.Borough with Largest SAT Score Deviation:
 - Determine which NYC borough exhibits the largest standard deviation in combined SAT scores across its schools. Save this information in a pandas DataFrame called largest_std_dev, containing:
   - "borough" - Name of the borough with the largest standard deviation.
   - "num_schools" - Number of schools in the borough.
   - "num_schools" - Number of schools in the borough.
   - "std_SAT" - Standard deviation of total SAT scores in the borough.
  - All numeric values are rounded to two decimal places.
## Requirements
 - Python v.3 or +
 - Pandas library
## Usage
1.Ensure you have Python and pandas installed.
2.Download or clone the repository containing 'schools.csv'.
3.Run the Python script to perform the analysis.
