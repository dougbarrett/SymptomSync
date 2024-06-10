# Databricks notebook source
# MAGIC %md
# MAGIC # Overview of dbrx models in Databricks Marketplace Listing
# MAGIC
# MAGIC The dbrx models offered in Databricks Marketplace are text generation models released by Databricks. They are [MLflow](https://mlflow.org/docs/latest/index.html) models that packages
# MAGIC [Hugging Face’s implementation for dbrx models](https://huggingface.co/collections/databricks/dbrx-6601c0852a0cdd3c59f71962)
# MAGIC using the [transformers](https://mlflow.org/docs/latest/models.html#transformers-transformers-experimental)
# MAGIC flavor in MLflow.
# MAGIC
# MAGIC **Input:** Request that describes the conversation containing the text of instructions, where the messages field must alternate between user and assistant roles, ending with a user message. ([AWS](https://docs.databricks.com/en/machine-learning/foundation-models/api-reference.html#chat-request)|[Azure](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/foundation-models/api-reference#chat-request))
# MAGIC
# MAGIC **Output:** Chat completion object that provides the next assistant message containing the generated response text in the conversation([AWS](https://docs.databricks.com/en/machine-learning/foundation-models/api-reference.html#chat-response)|[Azure](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/foundation-models/api-reference#chat-response))
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Listed Marketplace Models
# MAGIC - dbrx_base:
# MAGIC   - It packages [Hugging Face’s implementation for the dbrx model](https://huggingface.co/databricks/dbrx-base).
# MAGIC   - It has 132 billion parameters.
# MAGIC   - It is a pre-trained generative text model that can be used for further fine-tuning on specific applications.
# MAGIC
# MAGIC - dbrx_instruct:
# MAGIC   - It packages [Hugging Face’s implementation for the dbrx_instruct model](https://huggingface.co/databricks/dbrx-instruct).
# MAGIC   - Thanks to its MoE architecture, DBRX Instruct is highly efficient for inference, activating only 36 billion parameters out of a total of 132 billion trained parameters.
# MAGIC   - It is capable of handling input length up to 32k tokens, and generating outputs of up to 4k tokens.
# MAGIC   - It is fine-tuned specifically for instruction-based use cases, and excels at a broad set of natural language tasks such as text summarization, question-answering, extraction, and coding.

# COMMAND ----------

# MAGIC %md
# MAGIC # Suggested environment
# MAGIC Creating and querying serving endpoint don't require specific runtime versions and GPU instance type.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Install Dependencies
# MAGIC To create and query the model serving endpoint, Databricks recommends to install the newest Databricks SDK for Python.

# COMMAND ----------

# Upgrade to use the newest Databricks SDK
%pip install --upgrade databricks-sdk
dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

# Select the model from the dropdown list
model_names = ['bge_base_en_v1_5']
dbutils.widgets.dropdown("model_name", model_names[0], model_names)

# COMMAND ----------

# Default catalog name when installing the model from Databricks Marketplace.
# Replace with the name of the catalog containing this model
catalog_name = "system"

# You should specify the newest model version to load for inference
version = "1"
model_name = dbutils.widgets.get("model_name")
model_uc_path = f"{catalog_name}.ai.{model_name}"
endpoint_name = f'{model_name}_marketplace'

# Minimum desired provisioned throughput
min_provisioned_throughput = 500

# Maximum desired provisioned throughput
max_provisioned_throughput = 1000

# COMMAND ----------

# MAGIC %md
# MAGIC # Usage

# COMMAND ----------

# MAGIC %md
# MAGIC Databricks recommends that you primarily work with this model via Model Serving
# MAGIC ([AWS](https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html)|[Azure](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/model-serving/create-manage-serving-endpoints)).

# COMMAND ----------

# MAGIC %md
# MAGIC ## Deploying the model to Model Serving
# MAGIC
# MAGIC You can deploy this model directly to a Databricks Model Serving Endpoint
# MAGIC ([AWS](https://docs.databricks.com/machine-learning/model-serving/create-manage-serving-endpoints.html)|[Azure](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/model-serving/create-manage-serving-endpoints)).
# MAGIC
# MAGIC Note: Model serving is not supported on GCP.
# MAGIC
# MAGIC You can create the endpoint by clicking the “Serve this model” button above in the model UI. And you can also
# MAGIC create the endpoint with Databricks SDK as following:
# MAGIC

# COMMAND ----------

import requests
import json

# Get the API endpoint and token for the current notebook context
API_ROOT = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()
API_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

# send the POST request to create the serving endpoint
data = {
    "name": endpoint_name,
    "config": {
        "served_entities": [
            {
                "entity_name": model_uc_path,
                "entity_version": version,
                "min_provisioned_throughput": min_provisioned_throughput,
                "max_provisioned_throughput": max_provisioned_throughput,
            }
        ]
    },
}

headers = {"Context-Type": "text/json", "Authorization": f"Bearer {API_TOKEN}"}

response = requests.post(
    url=f"{API_ROOT}/api/2.0/serving-endpoints", json=data, headers=headers
)

print(json.dumps(response.json(), indent=4))

# COMMAND ----------

# MAGIC %md
# MAGIC ## SQL transcription using ai_query
# MAGIC
# MAGIC To generate the text using the endpoint, use `ai_query`
# MAGIC to query the Model Serving endpoint. The first parameter should be the
# MAGIC name of the endpoint you previously created for Model Serving. The second
# MAGIC parameter should be a string containing the instruction text.
# MAGIC
# MAGIC NOTE: `ai_query` is currently in Public Preview. Please sign up at [AI Functions Public Preview enrollment form](https://docs.google.com/forms/d/e/1FAIpQLScVyh5eRioqGwuUVxj9JOiKBAo0-FWi7L3f4QWsKeyldqEw8w/viewform) to try out the new feature.
# MAGIC
# MAGIC ```sql
# MAGIC SELECT 
# MAGIC ai_query(
# MAGIC   <endpoint name>,
# MAGIC   """What is ML?"""
# MAGIC )
# MAGIC ```
# MAGIC
# MAGIC You can use `ai_query` in this manner to generate text in
# MAGIC SQL queries or notebooks connected to Databricks SQL Pro or Serverless
# MAGIC SQL Endpoints.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Generate the text by querying the serving endpoint
# MAGIC With the Databricks SDK, you can query the serving endpoint as follows:

# COMMAND ----------

from databricks.sdk import WorkspaceClient

from databricks.sdk.service.serving import ChatMessage

w = WorkspaceClient()

# Change it to your own input
messages = [
    {
      "role": "user",
      "content": "Hello!"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I assist you today?"
    },
    {
      "role": "user",
      "content": "What is Databricks?"
    }
]

messages = [ChatMessage.from_dict(message) for message in messages]
response = w.serving_endpoints.query(
    name=endpoint_name,
    messages=messages,
)
response.as_dict()

# COMMAND ----------

import mlflow
import pandas as pd

mlflow.set_registry_uri("databricks-uc")

logged_model = f"models:/{catalog_name}.models.{model_name}/{version}"
# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

loaded_model._model_impl.pipeline("What is ML?")
