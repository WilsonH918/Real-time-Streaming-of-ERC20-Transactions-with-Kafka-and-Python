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
2. In another command prompt, navigate to the Kafka installation directory and start the Kafka broker by running the command .\bin\windows\kafka-server-start.bat .\config\server.properties. Keep this command prompt open.  
3. Create a Kafka topic by running the command .\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --topic your-topic-name (replace "your-topic-name" with the desired topic name). In your case, the command would be .\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --topic ERC20-real-time-token.  
![image](https://user-images.githubusercontent.com/117455557/229311227-0a600481-d88f-40b1-b2ef-33da2d0cdbf7.png)  
4. Install the kafka-python package by running the command pip install kafka-python.  
5. Run the producer.py and consumer.py scripts to start the data pipeline. You should see the real-time web3 transactions being produced and consumed.  
![image](https://user-images.githubusercontent.com/117455557/229311318-2611e34b-bcee-41a8-a45b-a46e89fe42c9.png)
![image](https://user-images.githubusercontent.com/117455557/229311338-362ec60d-8457-464f-b03c-2a00a4a3f7d3.png)  
Note: Before running the scripts, make sure to update the API key and ERC-20 token address in the producer.py file.  

## Prerequisites  
To run this project, you will need the following:  
- Python 3  
- Apache Kafka (version 2.6 or later)  
- Kafka Connect (version 2.6 or later)  
- Etherscan API key  
