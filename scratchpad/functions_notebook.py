# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC --query customers based on multiple symptoms and locations
# MAGIC
# MAGIC /*
# MAGIC Create a python function that can take multiple parameters and perform a sql query using these parameters as predicates
# MAGIC
# MAGIC Rules:
# MAGIC 1. The columns in the table are as follows:
# MAGIC     PatientName VARCHAR(255),
# MAGIC     Zipcode VARCHAR(10),
# MAGIC     TreatingDoctorSpecialty VARCHAR(255),
# MAGIC     BodyPartWithIssue VARCHAR(255),
# MAGIC     Disease VARCHAR(255),
# MAGIC     Symptom VARCHAR(1000)
# MAGIC
# MAGIC 2. The first parameter is ZipCode and a user can only provide one.
# MAGIC 3. The second parameter is Symptom. The user can only provide one and it shouldn't need to match exactly.
# MAGIC */

# COMMAND ----------

def query_zipcodeSymptom(spark, zipcode, symptom):
    # Create the SQL query with the provided parameters as predicates
    query = f"""
    SELECT *
    FROM Patients
    WHERE Zipcode = '{zipcode}'
    AND Symptom LIKE '%{symptom}%'
    """
    # Execute the query using Spark SQL
    result = spark.sql(query)
    
    # Return the result as a Spark DataFrame
    return result
