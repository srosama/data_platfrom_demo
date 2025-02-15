# Architecture Overview

The data platform is divided into several components:

1. **Data Ingestion:**  
   - `src/ingestion/`: Modules for reading data from Kafka

2. **Staging:**  
   - `src/staging/`: Temporary storage and validation of raw data.

3. **Processing (ETL):**  
   - `src/processing/`: Transform and aggregate the raw data.

4. **Storage:**  
   - `src/storage/`: Load data into a data warehouse 

5. **Orchestration:**  
   - `src/orchestration`: Airflow manage and orcheste the jobs 

