# Databricks notebook source
dbutils.widgets.text("Symptom", "")

# COMMAND ----------

# MAGIC %run ./functions_notebook
# MAGIC
# MAGIC res = query_zipcodeSymptom(spark, "12345", "cough")
# MAGIC
# MAGIC display(res)

# COMMAND ----------

print(dbutils.widgets.get("Symptom"))
