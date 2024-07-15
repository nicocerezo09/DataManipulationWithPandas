# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("NYCPublicSchool\schools.csv")

# Preview the data
schools.head()

#New DataFrame best_math_schools
best_math_schools = schools[schools["average_math"] >= 0.80 * 800]
best_math_schools = best_math_schools[['school_name', 'average_math']]
best_math_schools = best_math_schools.sort_values(by="average_math", ascending=False)

#Top 10 schools in SAT average
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["total_SAT", "school_name"]].sort_values(by="total_SAT", ascending=False).head(10)
print(top_10_schools)

# Group by 'borough' and calculate necessary statistics
borough_stats = schools.groupby('borough').agg(
    num_schools=('school_name', 'count'),
    average_SAT=('total_SAT', 'mean'),
    std_SAT=('total_SAT', 'std')
).reset_index()

# Find the district with the largest standard deviation of total_SAT
largest_std_dev_borough = borough_stats.loc[borough_stats['std_SAT'].idxmax()]

# Round numerical values to two decimal places
largest_std_dev_borough['average_SAT'] = round(largest_std_dev_borough['average_SAT'], 2)
largest_std_dev_borough['std_SAT'] = round(largest_std_dev_borough['std_SAT'], 2)

# Create the final DataFrame with a single row
largest_std_dev = pd.DataFrame([largest_std_dev_borough])

# Show the results
print(largest_std_dev)



