---

# **Project 1: Claims Data Analysis (SSIS)**

## **Overview**
This project implements an ETL workflow for the **Claims Data Analysis** use case using SQL Server Integration Services (SSIS). The goal is to automate the process of ingesting, transforming, and loading healthcare claims data into a star-schema-based Data Warehouse for analysis and visualization.

---

## **Directory Structure**
```
Project1_ClaimsDataAnalysis/
├── Packages/
│   ├── LoadClaims.dtsx           # SSIS package for claims data ingestion
│   ├── TransformClaims.dtsx      # SSIS package for transformations
│   ├── LoadToFactDim.dtsx        # SSIS package for loading data into fact/dim tables
├── Connections/
│   ├── ClaimsDatabase.dtsConfig  # Connection config for SQL database
│   ├── ClaimsFlatFile.dtsConfig  # Connection config for flat file sources
├── Logs/
│   ├── ClaimsETLLog.txt          # Log file for package execution
├── Documentation/
│   ├── README.md                 # This file
│   ├── WorkflowDiagram.png       # Visual representation of the ETL workflow
├── Samples/
│   ├── SampleClaims.csv          # Sample claims data for testing
│   ├── SampleClaimStatus.csv
```

---

## **ETL Workflow**

### **Step 1: Data Ingestion**
- **Package**: `LoadClaims.dtsx`
- **Purpose**: Ingest raw claims data from `SampleClaims.csv` into staging tables.
- **Steps**:
  1. Establish a connection to the flat file (`ClaimsFlatFile.dtsConfig`).
  2. Load the data into staging tables in the Data Warehouse.

### **Step 2: Data Transformation**
- **Package**: `TransformClaims.dtsx`
- **Purpose**: Cleanse and transform raw data in staging tables.
- **Steps**:
  1. Standardize data formats (e.g., dates, numeric values).
  2. Validate data integrity (e.g., remove duplicates, check foreign key constraints).
  3. Map transformed data to fact and dimension tables.

### **Step 3: Data Loading**
- **Package**: `LoadToFactDim.dtsx`
- **Purpose**: Load transformed data into the star-schema structure.
- **Steps**:
  1. Load cleansed data into `FactClaims`.
  2. Populate related dimension tables (e.g., `DimPayers`, `DimClaimStatus`).

---

## **How to Use**

### **1. Configure Connections**
- Update the `.dtsConfig` files in the `Connections/` folder:
  - **ClaimsDatabase.dtsConfig**: SQL Server connection string.
  - **ClaimsFlatFile.dtsConfig**: Path to `SampleClaims.csv`.

### **2. Run SSIS Packages**
1. **Open Project**:
   - Open the `NorthwellPracticeDWH.sln` solution file in Visual Studio Community.
2. **Load Data**:
   - Execute the `LoadClaims.dtsx` package to ingest raw claims data.
3. **Transform Data**:
   - Run the `TransformClaims.dtsx` package to cleanse and transform the data.
4. **Load Fact/Dim Tables**:
   - Execute the `LoadToFactDim.dtsx` package to populate the Data Warehouse.

### **3. Check Logs**
- Execution logs are stored in the `Logs/` directory. Review `ClaimsETLLog.txt` for details on package execution.

---

## **Prerequisites**
- **Software**:
  - SQL Server Developer Edition (with SSIS and SSDT).
  - Visual Studio Community Edition with SSIS extensions.
- **Data**:
  - Ensure the sample data files (`SampleClaims.csv`, `SampleClaimStatus.csv`) are placed in the `Samples/` folder.

---

## **Validation**
After running the SSIS packages, validate the data:
1. Check staging tables for completeness and correctness.
2. Verify data in fact and dimension tables for proper transformations.
3. Query SQL views (created in the main project) to confirm analytical insights.

---

## **Documentation**
- **Workflow Diagram**:
  - Refer to `WorkflowDiagram.png` for a visual representation of the ETL process.
- **Key Outputs**:
  - Claims denial trends, average processing times, and payer-specific KPIs.

---

## **Future Enhancements**
- Implement incremental data loading for real-time updates.
- Add error-handling and automated notifications (via `LoggingFramework.dtsx`).
- Integrate external data sources (e.g., APIs) for broader analytics.

---

## **Notes**
- This SSIS implementation is modular and focused on Project 1.
- Shared SSIS packages (e.g., logging, notifications) can be reused across other projects in the `Shared/` directory.

---

## **Contact**
For questions or feedback, please contact dandredesir@gmail.com.

---

