# Databricks notebook source
Can you create sample data for database of patients with a particular disease and symptoms. Rules - 1. A patient can have one more than one disease. Each disease need to be categorized into one record.
2. Main goal is to know various symptoms observed by patient with comma separated value in same row.
Use below data as sample data for creating around 100 records with above rules. Below data contains first record as column headers and second record as sample data - 
Patient name	zipcode	treating doctor specialty	body part with issue	Disease	symptom
Samantha	30729	Oncology	Lung	Lung Cancer	headaches and loss of apetitie

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE Patients (
# MAGIC     PatientName VARCHAR(255),
# MAGIC     Zipcode VARCHAR(10),
# MAGIC     TreatingDoctorSpecialty VARCHAR(255),
# MAGIC     BodyPartWithIssue VARCHAR(255),
# MAGIC     Disease VARCHAR(255),
# MAGIC     Symptom VARCHAR(1000)
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Samantha', '30729', 'Oncology', 'Lung', 'Lung Cancer', 'headaches, loss of appetite');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('John', '10001', 'Pulmonology', 'Lung', 'Asthma', 'shortness of breath, wheezing');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Emily', '90001', 'Internal Medicine', 'Digestive System', 'Crohn''s Disease', 'abdominal pain, diarrhea');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Michael', '60007', 'Gastroenterology', 'Digestive System', 'Ulcerative Colitis', 'bloody stools, fatigue');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Sophia', '30303', 'Rheumatology', 'Joints', 'Rheumatoid Arthritis', 'joint pain, morning stiffness');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Daniel', '75001', 'Neurology', 'Brain', 'Parkinson''s Disease', 'tremors, bradykinesia');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Emma', '90210', 'Endocrinology', 'Thyroid', 'Hypothyroidism', 'fatigue, weight gain');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Olivia', '20001', 'Cardiology', 'Heart', 'Coronary Artery Disease', 'chest pain, shortness of breath');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('William', '60601', 'Dermatology', 'Skin', 'Psoriasis', 'red patches, itching');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Ava', '94102', 'Allergy & Immunology', 'Respiratory System', 'Allergic Rhinitis', 'sneezing, runny nose');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Benjamin', '02116', 'Ophthalmology', 'Eyes', 'Glaucoma', 'blurred vision, eye pain');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Isabella', '90064', 'Hematology/Oncology', 'Blood', 'Leukemia', 'easy bruising, frequent infections');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Mia', '75201', 'Nephrology', 'Kidneys', 'Chronic Kidney Disease', 'fatigue, swelling');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Ethan', '10023', 'Urology', 'Urinary System', 'Kidney Stones', 'severe flank pain, blood in urine');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Charlotte', '28202', 'Gynecology', 'Reproductive System', 'Endometriosis', 'pelvic pain, heavy periods');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Liam', '90045', 'Pulmonology', 'Lung', 'COPD', 'chronic cough, shortness of breath');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Charlotte', '28205', 'Endocrinology', 'Thyroid', 'Hyperthyroidism', 'rapid heartbeat, weight loss');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Noah', '30301', 'Neurology', 'Brain', 'Migraine', 'headache, nausea, sensitivity to light');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Ava', '10001', 'Ophthalmology', 'Eyes', 'Cataract', 'blurred vision, glare sensitivity');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('William', '60610', 'Dermatology', 'Skin', 'Eczema', 'itchy, dry skin, rash');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Isabella', '90064', 'Hematology/Oncology', 'Blood', 'Lymphoma', 'swollen lymph nodes, fever, weight loss');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Mason', '75201', 'Nephrology', 'Kidneys', 'Polycystic Kidney Disease', 'flank pain, high blood pressure');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Sophia', '30303', 'Gynecology', 'Reproductive System', 'PCOS', 'irregular periods, weight gain');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Oliver', '20002', 'Cardiology', 'Heart', 'Arrhythmia', 'palpitations, dizziness');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Emma', '90210', 'Endocrinology', 'Thyroid', 'Hashimoto''s Thyroiditis', 'fatigue, hair loss, weight gain');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from patients;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Liam', '90045', 'Pulmonology', 'Lung', 'COPD', 'chronic cough, shortness of breath');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Charlotte', '28205', 'Endocrinology', 'Thyroid', 'Hyperthyroidism', 'rapid heartbeat, weight loss');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Noah', '30301', 'Neurology', 'Brain', 'Migraine', 'headache, nausea, sensitivity to light');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Ava', '10001', 'Ophthalmology', 'Eyes', 'Cataract', 'blurred vision, glare sensitivity');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('William', '60610', 'Dermatology', 'Skin', 'Eczema', 'itchy, dry skin, rash');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Isabella', '90064', 'Hematology/Oncology', 'Blood', 'Lymphoma', 'swollen lymph nodes, fever, weight loss');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Mason', '75201', 'Nephrology', 'Kidneys', 'Polycystic Kidney Disease', 'flank pain, high blood pressure');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Sophia', '30303', 'Gynecology', 'Reproductive System', 'PCOS', 'irregular periods, weight gain');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Oliver', '20002', 'Cardiology', 'Heart', 'Arrhythmia', 'palpitations, dizziness');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Emma', '90210', 'Endocrinology', 'Thyroid', 'Hashimoto''s Thyroiditis', 'fatigue, hair loss, weight gain');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Aiden', '10023', 'Gastroenterology', 'Digestive System', 'Gastritis', 'abdominal pain, nausea');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Amelia', '75201', 'Allergy & Immunology', 'Respiratory System', 'Asthma', 'coughing, wheezing, chest tightness');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('James', '60601', 'Orthopedics', 'Bones', 'Osteoarthritis', 'joint pain, stiffness');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Harper', '94102', 'Rheumatology', 'Joints', 'Fibromyalgia', 'widespread muscle pain, fatigue');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Elijah', '02116', 'Dermatology', 'Skin', 'Acne', 'pimples, blackheads, oily skin');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Evelyn', '90001', 'Endocrinology', 'Pancreas', 'Diabetes', 'excessive thirst, frequent urination');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Benjamin', '30329', 'Neurology', 'Brain', 'Epilepsy', 'seizures, loss of consciousness');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Emily', '28202', 'Gynecology', 'Reproductive System', 'Polycystic Ovary Syndrome', 'irregular periods, acne');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Lucas', '10016', 'Cardiology', 'Heart', 'Hypertension', 'high blood pressure, headache');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Layla', '75209', 'Pulmonology', 'Lungs', 'Bronchitis', 'cough, phlegm production');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Henry', '90210', 'Orthopedics', 'Bones', 'Fracture', 'pain, swelling, inability to move');
# MAGIC
# MAGIC -- Add more INSERT statements for additional sample data here...
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Mia', '60611', 'Gastroenterology', 'Digestive System', 'GERD', 'heartburn, acid reflux');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Ethan', '10010', 'Urology', 'Urinary System', 'Urinary Tract Infection', 'painful urination, frequent urination');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Avery', '75204', 'Pediatrics', 'Respiratory System', 'Croup', 'barking cough, hoarse voice');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Mason', '30303', 'Oncology', 'Blood', 'Hemophilia', 'easy bruising, joint pain');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Harper', '90005', 'Dermatology', 'Skin', 'Rosacea', 'flushing, redness, visible blood vessels');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Evelyn', '60614', 'Endocrinology', 'Thyroid', 'Graves'' Disease', 'bulging eyes, weight loss');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Logan', '94107', 'Neurology', 'Brain', 'Multiple Sclerosis', 'fatigue, numbness, difficulty walking');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Luna', '10021', 'Gynecology', 'Reproductive System', 'Pelvic Inflammatory Disease', 'lower abdominal pain, fever');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Jackson', '28210', 'Orthopedics', 'Bones', 'Rheumatoid Arthritis', 'joint swelling, stiffness, fatigue');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Aria', '90210', 'Ophthalmology', 'Eyes', 'Macular Degeneration', 'blurred vision, blind spots');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Grayson', '60657', 'Cardiology', 'Heart', 'Heart Failure', 'shortness of breath, fatigue, swelling');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Aubrey', '75201', 'Pulmonology', 'Lung', 'Pneumonia', 'fever, cough with phlegm');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Ella', '02110', 'Pediatrics', 'Respiratory System', 'RSV', 'cough, wheezing, difficulty breathing');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Jack', '90036', 'Gastroenterology', 'Digestive System', 'Ulcer', 'abdominal pain, bloating');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Layla', '30331', 'Endocrinology', 'Pancreas', 'Pancreatitis', 'severe abdominal pain, nausea');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Carter', '10011', 'Neurology', 'Brain', 'Alzheimer''s Disease', 'memory loss, confusion, difficulty with familiar tasks');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Mila', '94103', 'Dermatology', 'Skin', 'Melanoma', 'changes in mole size, color, or shape');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Liam', '75205', 'Orthopedics', 'Bones', 'Osteoporosis', 'bone fractures, loss of height');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Emily', '90025', 'Gynecology', 'Reproductive System', 'Ovarian Cyst', 'pelvic pain, bloating');
# MAGIC
# MAGIC INSERT INTO Patients (PatientName, Zipcode, TreatingDoctorSpecialty, BodyPartWithIssue, Disease, Symptom)
# MAGIC VALUES ('Landon', '60661', 'Cardiology', 'Heart', 'Atrial Fibrillation', 'irregular heartbeat, palpitations');
# MAGIC
# MAGIC -- Add more INSERT statements for additional sample data here...
# MAGIC

# COMMAND ----------

pip install faker pandas

# COMMAND ----------

from faker import Faker
import pandas as pd

# Initialize the Faker library
fake = Faker()

# Define a function to generate fake data
def generate_fake_data(num_records=100):
    data = []
    specialties = ['Oncology', 'Cardiology', 'Neurology', 'Orthopedics', 'Dermatology']
    body_parts = ['Lung', 'Heart', 'Brain', 'Knee', 'Skin']
    diseases_symptoms = {
        'Lung Cancer': ['headaches', 'loss of appetite', 'coughing'],
        'Heart Disease': ['chest pain', 'shortness of breath', 'fatigue'],
        'Alzheimer\'s': ['memory loss', 'confusion', 'difficulty speaking'],
        'Arthritis': ['joint pain', 'stiffness', 'swelling'],
        'Eczema': ['itching', 'rashes', 'dry skin']
    }
    
    for _ in range(num_records):
        patient_name = fake.first_name()
        zipcode = fake.zipcode()
        specialty = fake.random.choice(specialties)
        body_part = fake.random.choice(body_parts)
        disease = fake.random.choice(list(diseases_symptoms.keys()))
        symptoms = ', '.join(fake.random.sample(diseases_symptoms[disease], k=2))  # Randomly pick 2 symptoms
        
        data.append([patient_name, zipcode, specialty, body_part, disease, symptoms])
    
    return data

# Generate sample data
sample_data = generate_fake_data(100)

# Define column headers
columns = ['Patient name', 'zipcode', 'treating doctor specialty', 'body part with issue', 'Disease', 'symptom']

# Create a DataFrame
df = pd.DataFrame(sample_data, columns=columns)

# Display the DataFrame
#import ace_tools as tools; tools.display_dataframe_to_user(name="Sample Patient Data", dataframe=df)

# Print the DataFrame
print(df)


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from patients

# COMMAND ----------

from faker import Faker
import pandas as pd

# Initialize the Faker library
fake = Faker()

# Define a function to generate fake data
def generate_fake_data(num_records=100):
    data = []
    specialties = ['Oncology', 'Cardiology', 'Neurology', 'Orthopedics', 'Dermatology']
    body_parts = ['Lung', 'Heart', 'Brain', 'Knee', 'Skin']
    diseases_symptoms = {
        'Lung Cancer': ['headaches', 'loss of appetite', 'coughing'],
        'Heart Disease': ['chest pain', 'shortness of breath', 'fatigue'],
        'Alzheimer\'s': ['memory loss', 'confusion', 'difficulty speaking'],
        'Arthritis': ['joint pain', 'stiffness', 'swelling'],
        'Eczema': ['itching', 'rashes', 'dry skin']
    }
    
    for _ in range(num_records):
        patient_name = fake.first_name()
        zipcode = fake.zipcode()
        specialty = fake.random.choice(specialties)
        body_part = fake.random.choice(body_parts)
        disease = fake.random.choice(list(diseases_symptoms.keys()))
        symptoms = ', '.join(fake.random.sample(diseases_symptoms[disease], k=2))  # Randomly pick 2 symptoms
        
        data.append([patient_name, zipcode, specialty, body_part, disease, symptoms])
    
    return data

# Generate sample data
sample_data = generate_fake_data(100)

# Define column headers
columns = ['Patient name', 'zipcode', 'treating doctor specialty', 'body part with issue', 'Disease', 'symptom']

# Create a DataFrame
df = pd.DataFrame(sample_data, columns=columns)

# Display the DataFrame
#import ace_tools as tools; tools.display_dataframe_to_user(name="Sample Patient Data", dataframe=df)

# Generate SQL INSERT statements
insert_statements = []
table_name = 'patients'
for index, row in df.iterrows():
    values = "', '".join(map(str, row.values))
    insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ('{values}');"
    insert_statements.append(insert_statement)

# Print SQL INSERT statements
for statement in insert_statements:
    print(statement)

# Optional: Save to a file
with open('insert_statements.sql', 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')

print("SQL INSERT statements have been generated and saved to 'insert_statements.sql'.")


# COMMAND ----------

from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Define a function to generate fake data
def generate_fake_data(num_records=1000):
    specialties = ['Oncology', 'Cardiology', 'Neurology', 'Orthopedics', 'Dermatology']
    body_parts = ['Lung', 'Heart', 'Brain', 'Knee', 'Skin']
    diseases_symptoms = {
        'Lung Cancer': ['headaches', 'loss of appetite', 'coughing'],
        'Heart Disease': ['chest pain', 'shortness of breath', 'fatigue'],
        'Alzheimer\'s': ['memory loss', 'confusion', 'difficulty speaking'],
        'Arthritis': ['joint pain', 'stiffness', 'swelling'],
        'Eczema': ['itching', 'rashes', 'dry skin']
    }
    
    data = []
    for _ in range(num_records):
        patient_name = fake.first_name().replace("'", "")
        zipcode = fake.zipcode()
        specialty = random.choice(specialties)
        body_part = random.choice(body_parts)
        disease = random.choice(list(diseases_symptoms.keys()))
        symptoms = ', '.join(random.sample(diseases_symptoms[disease], k=2))  # Randomly pick 2 symptoms
        
        data.append([patient_name, zipcode, specialty, body_part, disease, symptoms])
    
    return data

# Generate sample data
sample_data = generate_fake_data(1000)

# Define column headers
columns = ['Patientname', 'zipcode', 'treatingdoctorspecialty', 'bodypartwithissue', 'Disease', 'symptom']

# Generate SQL INSERT statements
insert_statements = []
table_name = 'patients'
for record in sample_data:
    values = "', '".join(map(str, record))
    insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ('{values}');"
    insert_statements.append(insert_statement)

# Print SQL INSERT statements
for statement in insert_statements:
    print(statement)

# Optional: Save to a file
with open('insert_statements_1.sql', 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')

print("SQL INSERT statements have been generated and saved to 'insert_statements_1.sql'.")


# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO patients (Patientname, zipcode, treatingdoctorspecialty, bodypartwithissue, Disease, symptom) VALUES ('Bruce', '89621', 'Cardiology', 'Skin', 'Eczema', 'dry skin, rashes');

# COMMAND ----------

from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Define a function to generate fake data
def generate_fake_data(num_records=1000):
    specialties = ['Oncology', 'Cardiology', 'Neurology', 'Orthopedics', 'Dermatology']
    body_parts = ['Lung', 'Heart', 'Brain', 'Knee', 'Skin']
    diseases_symptoms = {
        'Lung Cancer': ['headaches', 'loss of appetite', 'coughing'],
        'Heart Disease': ['chest pain', 'shortness of breath', 'fatigue'],
        'Alzheimer\'s': ['memory loss', 'confusion', 'difficulty speaking'],
        'Arthritis': ['joint pain', 'stiffness', 'swelling'],
        'Eczema': ['itching', 'rashes', 'dry skin']
    }
    
    data = []
    for _ in range(num_records):
        patient_name = fake.first_name()
        zipcode = fake.zipcode()
        specialty = random.choice(specialties)
        body_part = random.choice(body_parts)
        disease = random.choice(list(diseases_symptoms.keys()))
        symptoms = ', '.join(random.sample(diseases_symptoms[disease], k=2))  # Randomly pick 2 symptoms
        
        data.append([patient_name, zipcode, specialty, body_part, disease, symptoms])
    
    return data

# Generate sample data
sample_data = generate_fake_data(1000)

# Define column headers
columns = ['Patientname', 'zipcode', 'treatingdoctorspecialty', 'bodypartwithissue', 'Disease', 'symptom']

# Generate SQL INSERT statements
insert_statements = []
table_name = 'patients'
for record in sample_data:
    values = "', '".join(map(str, record))
    insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ('{values}');"
    insert_statements.append(insert_statement)

# Print SQL INSERT statements
for statement in insert_statements:
    print(statement)

# Optional: Save to a file
with open('insert_statements.sql', 'w') as file:
    for statement in insert_statements:
        file.write(statement + '\n')

print("SQL INSERT statements have been generated and saved to 'insert_statements.sql'.")

