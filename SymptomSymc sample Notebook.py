# Databricks notebook source
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


