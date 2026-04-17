from setuptools import find_packages,setup

setup(name="TradeAgent",
       version="0.0.1",
       author="gauranggiri",
       author_email="gauranggirimeghanathi@gmail.com",
       packages=find_packages(),
       install_requires=['lancedb','langchain','langgraph','tavily-python','polygon']
       )