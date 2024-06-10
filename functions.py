def query_zipcodeSymptom(zipcode, symptom):
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