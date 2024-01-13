import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Number of users in the dataset
num_users = 10000

# Generate synthetic data for the survey
data = {
    'User_ID': range(1, num_users + 1),
    'Email': [f'user{i}@example.com' for i in range(1, num_users + 1)],
    'Phone_Number': [''.join(np.random.choice(list('0123456789')) for _ in range(10)) for _ in range(num_users)],
    'Name': [f'User {i}' for i in range(1, num_users + 1)],
    
    # Lifestyle details
    'Physical_Activity_Frequency': np.random.choice(['None', 'Occasional', 'Regular'], size=num_users),
    'Workout_Type': np.random.choice(['Cardio', 'Strength Training', 'Yoga', 'None'], size=num_users),
    'Age': np.random.randint(18, 80, size=num_users),
    'Health_Issues': np.random.choice(['Yes', 'No'], size=num_users),
    'Existing_Medications': np.random.choice(['Aspirin', 'Ibuprofen', 'None'], size=num_users),
    
    # Existing Dietary details
    'Food_Consumptions': np.random.choice(['Balanced', 'Vegetarian', 'Vegan'], size=num_users),
    'Nutrition_Intake': np.random.choice(['Adequate', 'Inadequate'], size=num_users),
    'Water_Intake': np.random.randint(1, 4, size=num_users),  # Assuming 1-4 liters per day
    
    # Existing concerns
    'Bone_Health': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    'Skin_Health': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    'Heart_Health': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    'Gut_Health': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    'Overall_Physical_Health': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    'Mental_Brain_Health': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    
    # Symptoms
    'Energy_Symptoms': np.random.choice(['High', 'Moderate', 'Low'], size=num_users),
    'Skin_Hair_Symptoms': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    'Internal_Body_Function_Symptoms': np.random.choice(['Excellent', 'Good', 'Poor'], size=num_users),
    'Stress_Anxiety_Symptoms': np.random.choice(['Low', 'Moderate', 'High'], size=num_users),
    
    # History of Vitamin Intake
    'Vitamin_Intake_History': np.random.choice(['Yes', 'No'], size=num_users),
    
    # Goals
    'Active_Lifestyle_Goals': np.random.choice(['Maintain', 'Improve'], size=num_users),
    'Sports_Lifestyle_Goals': np.random.choice(['Participate', 'Excel'], size=num_users),
    'Health_Improvement_Goals': np.random.choice(['Weight_Loss', 'Muscle_Gain', 'Overall_Wellness'], size=num_users),
    'Special_Life_Stages_Goals': np.random.choice(['Elderly_Care', 'Pregnancy_Care', 'Young_Kids_Care'], size=num_users),
    
    # Recommended Vitamin (Target Column)
    'Recommended_Vitamin': np.nan,
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define rules for recommending vitamins based on existing concerns, symptoms, and goals
# This is a simplified example and may not reflect real-world medical advice
for index, row in df.iterrows():
    if row['Overall_Physical_Health'] == 'Poor' or row['Gut_Health'] == 'Poor':
        df.at[index, 'Recommended_Vitamin'] = 'D'
    elif row['Heart_Health'] == 'Poor' or row['Mental_Brain_Health'] == 'Poor' or row['Stress_Anxiety_Symptoms'] == 'High':
        df.at[index, 'Recommended_Vitamin'] = 'B12'
    elif row['Skin_Hair_Symptoms'] == 'Poor' or row['Internal_Body_Function_Symptoms'] == 'Poor':
        df.at[index, 'Recommended_Vitamin'] = 'A'
    else:
        df.at[index, 'Recommended_Vitamin'] = np.random.choice(['A', 'B12', 'C', 'D', 'E', 'K'])

# Save the dataset to a CSV file
df.to_csv('health_survey_dataset.csv', index=False)

# Display the first few rows of the generated dataset
print(df.head())
