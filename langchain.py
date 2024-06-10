# Databricks notebook source
!pip install langchain

# COMMAND ----------

!pip install langchain-community langchain-core

# COMMAND ----------

!pip install mlflow

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return "hi"
    # return a + b

tools = [add]



# COMMAND ----------

from langchain.llms import Databricks
from langchain_core.messages import HumanMessage, SystemMessage

def transform_input(**request):
  request["messages"] = [
    {
      "role": "user",
      "content": request["prompt"]
    }
  ]
  del request["prompt"]
  return request

llm = Databricks(endpoint_name="databricks-dbrx-instruct", transform_input_fn=transform_input)
llm("What is a mixture of experts model?")


# COMMAND ----------

!pip install databricks-sql-connector

# COMMAND ----------

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain import OpenAI

db = SQLDatabase.from_databricks(catalog="workspace", schema="default")
llm = OpenAI(model_name="databricks-dbrx-instruct", temperature=.7)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

agent.run("What zip code has the highest patient count?")

