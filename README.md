# Real-time-Streaming-of-ERC20-Transactions-with-Kafka-and-Python  

## Overview  
This project demonstrates how to build a real-time data pipeline to retrieve ERC20 token transactions and store them in a local CSV file. The project uses Apache Kafka, an open-source distributed streaming platform, to stream real-time data from the Etherscan API, a blockchain explorer for the Ethereum network, and then stores the data in CSV format in a local file.  

The project consists of three main components:  
- Data Retrieval: This component retrieves real-time data from the Etherscan API using a Python script. The script queries the API to get the latest ERC20 token transactions and formats the data into a JSON object.  

- Data Streaming: This component uses Apache Kafka to stream the JSON data from the Python script to a Kafka topic. Kafka is used as the messaging middleware to decouple the data retrieval and storage components of the pipeline.  

- Data Storage: This component uses a Kafka Connect connector to write the data from the Kafka topic to a CSV file in a local directory. Kafka Connect is a tool for building scalable and reliable data pipelines between Kafka topics and external data systems.  

By using this pipeline, users can retrieve real-time ERC20 token transactions and store them in a local file for further analysis. The pipeline can be customized to include additional data sources, such as other blockchain explorers or data providers, and can also be scaled up to handle large volumes of data.  

## Instructions to Run the Real-Time ERC20 Token Transactions Data Pipeline  
1. Open a command prompt and navigate to the Kafka installation directory. Start the ZooKeeper server by running the command .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties. Keep this command prompt open.  
![image](https://user-images.githubusercontent.com/117455557/229311120-7dcf84a9-2a50-4e3e-9894-622ab1a4e6e0.png)  
2. In another command prompt, navigate to the Kafka installation directory and start the Kafka broker by running the command .\bin\windows\kafka-server-start.bat .\config\server.properties. Keep this command prompt open.  
![image](https://user-images.githubusercontent.com/117455557/229311161-92abf856-e008-4e5d-b6eb-fd3ca29285b8.png)  


## Prerequisites  
To run this project, you will need the following:  
- Python 3  
- Apache Kafka (version 2.6 or later)  
- Kafka Connect (version 2.6 or later)  
- Etherscan API key  
