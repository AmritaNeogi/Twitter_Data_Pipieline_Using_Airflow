# YouTube Data Pipeline using Apache Airflow

This YouTube Data ETL with Airflow project automates the extraction, transformation, and loading of data from YouTube channels. It uses the YouTube Data API, transforms the data, and can store it in destinations like Amazon S3.
Apache Airflow schedules and orchestrates the ETL process, ensuring the data is up-to-date and reliable for analysis.

## Overview
<div class="image-container"><img src="/images/overview.png" alt="Project Image"></div>

## Project Components
This project consists of several vital components, each with a critical role in efficiently processing and organizing data from YouTube channels. The main components are as follows:

1. **Data Extraction:** Using the YouTube Data API, I retrieve data from YouTube channels, with my project focusing on the "DarshilParmar" channel. During development, I encountered challenges related to API query timeouts and rate limiting, resulting in intermittent failures and timeouts.

2. **Data Transformation:** The extracted data is converted into a structured format suitable for analysis.

3. **Data Loading:** Once the data is prepared, you can select the storage destination. In my project, data is configured to be stored in an Amazon S3 bucket, but you have the flexibility to choose other cloud storage solutions like Google Cloud Storage.

4. **Airflow Integration:** This project is seamlessly integrated with Apache Airflow, enabling scheduled or trigger-based ETL jobs. This integration has been pivotal in automating and orchestrating the entire pipeline. I've encountered and resolved issues related to configuring Airflow DAGs and tasks for reliable execution.

5. **Error Handling:** Robust error handling mechanisms are in place to ensure the pipeline gracefully manages exceptions and provides clear notifications of any issues. I've enhanced error handling and implemented detailed logging for effective troubleshooting when errors occur.

## Objectives:
The key objectives of this project are:

1. Automating data retrieval from YouTube channels.
2. Ensuring that the collected data is cleaned, organized, and ready for analysis through the use of data cleaning and structuring functions.
3. Allowing flexibility in selecting the data storage destination. In my project, data is stored in an Amazon S3 bucket, and it's adaptable to other cloud storage solutions.
4. Implementing a dependable and efficient ETL process that can be scheduled and monitored, achieved through the integration of scheduling with Apache Airflow.
5. Providing a framework for extending and customizing the ETL process to meet specific requirements.

## Conclusion:
The YouTube Data ETL with Airflow project automates YouTube channel data extraction and transformation. It's flexible, adaptable, and integrates with Apache Airflow for scheduling and monitoring ETL jobs. This project simplifies data collection and preparation for analysis, benefiting data enthusiasts, analysts, and engineers.

## Reference
I'd like to express my gratitude to <a href = "https://www.youtube.com/watch?v=q8q3OFFfY6c&t=2027s"  style="text-decoration: none;"> Darshil Parmar</a> for inspiring this project. <br>
Please check the requirement.txt for the necessary prerequisites.<br>
For a more comprehensive understanding of the Apache Airflow setup, refer to the Document.pdf.<br>
