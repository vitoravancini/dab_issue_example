# Databricks notebook source
#!curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
import os
myToken = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().getOrElse(None)
os.environ['DATABRICKS_HOST'] = ""
os.environ['DATABRICKS_TOKEN'] = myToken


!/root/bin/databricks bundle deploy
