# Databricks notebook source
 !pip install databricks-genai


# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from databricks_genai_inference import ChatCompletion


response = ChatCompletion.create(model="databricks-dbrx-instruct",
                                messages=[{"role": "system", "content": "You are a helpful assistant."},
                                          {"role": "user","content": "What is a mixture of experts model?"}],
                                max_tokens=128)
print(f"response.message:{response.message}")

