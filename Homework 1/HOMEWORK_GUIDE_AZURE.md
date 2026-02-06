# Azure & Microsoft Fabric Guide for Module 1 Homework

This guide provides information on Azure products and Microsoft Fabric capabilities you can use to complete the Module 1 homework as an alternative or complement to the Docker-based approach.

---

## **Yes, You Can Use Microsoft Fabric!** ✅

Microsoft Fabric is an excellent all-in-one platform for this homework. Here's what Fabric offers:

### **Microsoft Fabric Data Engineering Components:**

1. **Fabric Lakehouse** - Alternative to PostgreSQL for storing structured data
   - Built on Delta Lake format
   - Supports both data lake and data warehouse workloads
   - Can ingest Parquet and CSV files directly
   - Provides SQL analytics endpoint for querying

2. **Fabric Notebooks** - For data transformation and analysis
   - Write PySpark/Python code for data ingestion and transformation
   - Interactive data exploration
   - Built-in Spark runtime

3. **Fabric Data Pipelines** - Alternative to Docker-based ingestion
   - Copy activity for data ingestion from 200+ connectors
   - Orchestrate data workflows
   - Support for Parquet and CSV file formats

4. **Fabric Dataflows Gen2** - Low-code ETL
   - Visual Power Query interface
   - Transform and load data into Lakehouse
   - No-code data preparation

5. **Fabric Data Warehouse** - Alternative to PostgreSQL
   - SQL-based analytics
   - T-SQL query support
   - COPY statement for ingesting Parquet/CSV

---

## **Azure Data Engineering Products (Traditional):**

### **Database Services:**

1. **Azure Database for PostgreSQL** - Direct replacement for the Docker PostgreSQL container
   - Flexible Server or Single Server options
   - Fully managed PostgreSQL service
   - No need for Docker setup

2. **Azure SQL Database** - Alternative relational database
   - T-SQL support
   - Built-in intelligence and security
   - Fully managed service

### **Data Storage:**

3. **Azure Data Lake Storage Gen2 (ADLS Gen2)** - For storing Parquet/CSV files
   - Optimized for big data analytics
   - Hierarchical namespace
   - Integration with all Azure services

4. **Azure Blob Storage** - General-purpose object storage
   - Store Parquet and CSV files
   - Cost-effective for large datasets
   - Multiple access tiers

### **Data Integration & ETL:**

5. **Azure Data Factory** - Data integration service
   - Copy activity for data ingestion
   - Support for Parquet, CSV, and many formats
   - Pipeline orchestration
   - Connect to PostgreSQL, ADLS, and more
   - 200+ connectors

6. **Azure Synapse Analytics** - Unified analytics platform
   - Combines data integration, big data, and data warehousing
   - Spark pools for data processing
   - SQL pools for analytics
   - Synapse Pipelines (similar to ADF)

### **Data Processing:**

7. **Azure Databricks** - Apache Spark-based analytics
   - Notebooks for PySpark/Python/Scala
   - Delta Lake support
   - Data engineering workflows
   - Connect to PostgreSQL for ingestion
   - Lakeflow Connect for PostgreSQL ingestion

8. **Azure HDInsight** - Managed Hadoop/Spark clusters
   - Process Parquet files
   - Run Spark jobs
   - Multiple cluster types

### **Infrastructure as Code:**

9. **Azure Resource Manager (ARM) Templates** - Alternative to Terraform
   - Native Azure IaC solution
   - JSON-based declarative syntax

10. **Bicep** - DSL for Azure resources
    - Simpler than ARM templates
    - Compiles to ARM templates
    - Better developer experience

11. **Terraform with Azure Provider** - Already mentioned in homework
    - Provision Azure resources instead of GCP
    - Use azurerm provider
    - Cross-platform support

---

## **How to Complete the Homework Using Azure/Fabric:**

### **Approach 1: Using Microsoft Fabric (Recommended)**

```
1. Create a Fabric Workspace
   - Sign up for Microsoft Fabric trial (free)
   - Create a new workspace

2. Create a Lakehouse
   - Navigate to Data Engineering workload
   - Create new Lakehouse item
   - This will be your data store

3. Use Data Pipeline to ingest Parquet/CSV files
   - Create a new Data Pipeline
   - Add Copy activity
   - Source: HTTP (for the URLs in homework)
   - Destination: Lakehouse Files or Tables

4. Transform data (if needed)
   - Use Fabric Notebooks with PySpark
   - Or use Dataflows Gen2 for visual transformation

5. Query data using SQL analytics endpoint
   - Every Lakehouse has a built-in SQL endpoint
   - Write SQL queries just like PostgreSQL
   - Answer Questions 3-6

6. Use Terraform for Q7
   - Use Terraform with Fabric REST API
   - Or manually provision resources via portal
```

**Benefits:**
- All-in-one platform
- No Docker required
- Serverless compute (auto-scaling)
- Free trial available

---

### **Approach 2: Using Azure Traditional Services**

```
1. Provision Azure Database for PostgreSQL
   terraform {
     required_providers {
       azurerm = {
         source  = "hashicorp/azurerm"
         version = "~> 3.0"
       }
     }
   }

   provider "azurerm" {
     features {}
   }

   resource "azurerm_postgresql_flexible_server" "taxi_db" {
     name                = "ny-taxi-server"
     resource_group_name = azurerm_resource_group.rg.name
     location            = azurerm_resource_group.rg.location
     version             = "13"
     administrator_login = "postgres"
     administrator_password = var.admin_password
     storage_mb          = 32768
     sku_name            = "B_Standard_B1ms"
   }

2. Store Parquet/CSV in Azure Blob Storage or ADLS Gen2
   - Upload green_tripdata_2025-11.parquet
   - Upload taxi_zone_lookup.csv

3. Use Azure Data Factory to copy data into PostgreSQL
   - Create linked services for Blob Storage and PostgreSQL
   - Create Copy activity pipeline
   - Transform Parquet to SQL inserts

4. Connect to PostgreSQL using Azure Data Studio or pgAdmin
   - Use connection string from Azure Portal
   - Public endpoint or private endpoint

5. Run SQL queries
   - Execute the same SQL queries as in homework
   - Answer Questions 3-6

6. Use Terraform with Azure provider
   - Provision all resources with Terraform
   - Resource group, storage account, PostgreSQL, ADF
```

**Benefits:**
- Similar to homework setup
- Managed PostgreSQL (no Docker)
- Scalable and production-ready

---

### **Approach 3: Hybrid (Best Learning)**

```
1. Keep Docker + PostgreSQL locally (as in homework)
   - Complete the original homework first
   - Understand the fundamentals

2. Add Azure Data Factory to ingest from cloud sources
   - Self-hosted integration runtime on your machine
   - Connect to local PostgreSQL
   - Ingest from Azure Blob Storage

3. Store results in Azure SQL Database or Fabric Lakehouse
   - Sync data from local to cloud
   - Compare performance

4. Practice both local and cloud workflows
   - Local development and testing
   - Cloud deployment and production

5. Use Terraform to provision Azure resources
   - Learn Terraform with both GCP and Azure
   - Compare cloud providers
```

**Benefits:**
- Best of both worlds
- Learn local and cloud
- Gradual migration path

---

## **Complete List of Azure Data Engineering Tools & Products:**

| **Category** | **Products** |
|---|---|
| **Unified Analytics** | Microsoft Fabric, Azure Synapse Analytics |
| **Databases** | Azure Database for PostgreSQL, Azure SQL Database, Azure Cosmos DB, Azure SQL Managed Instance |
| **Storage** | Azure Data Lake Storage Gen2, Azure Blob Storage, Azure Files, Azure NetApp Files |
| **Data Integration** | Azure Data Factory, Fabric Data Pipelines, Fabric Dataflows Gen2, Azure Logic Apps |
| **Big Data Processing** | Azure Databricks, Azure HDInsight, Fabric Spark, Azure Synapse Spark |
| **Data Warehousing** | Fabric Data Warehouse, Azure Synapse dedicated SQL pools, Azure SQL Database |
| **Real-Time Analytics** | Fabric Real-Time Intelligence, Azure Stream Analytics, Event Hubs, Fabric Eventstreams |
| **Orchestration** | Azure Data Factory, Logic Apps, Azure Functions, Fabric Pipelines |
| **Development** | Fabric Notebooks, Azure Databricks Notebooks, Synapse Notebooks, Azure Data Studio |
| **Infrastructure as Code** | Terraform (Azure provider), ARM Templates, Bicep, Azure CLI, PowerShell |
| **Containers** | Azure Container Instances, Azure Kubernetes Service (AKS), Azure Container Apps |
| **BI & Reporting** | Power BI, Power BI Embedded, Power BI Report Server |
| **Data Governance** | Microsoft Purview, Fabric Information Protection, Azure Policy |
| **ML & AI** | Azure Machine Learning, Fabric Data Science, Azure AI Services, Azure OpenAI |

---

## **Terraform Example: Azure vs GCP**

### **Original Homework (GCP):**
```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = "us-central1"
}

resource "google_storage_bucket" "data_bucket" {
  name     = "ny-taxi-data-bucket"
  location = "US"
}

resource "google_bigquery_dataset" "taxi_dataset" {
  dataset_id = "ny_taxi"
  location   = "US"
}
```

### **Azure Alternative:**
```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-ny-taxi"
  location = "East US"
}

resource "azurerm_storage_account" "storage" {
  name                     = "nytaxidatastorage"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled          = true  # For ADLS Gen2
}

resource "azurerm_storage_data_lake_gen2_filesystem" "filesystem" {
  name               = "taxi-data"
  storage_account_id = azurerm_storage_account.storage.id
}
```

### **Terraform Workflow (Answer to Q7 - Azure Version):**

1. **Downloading provider plugins and setting up backend**
   ```bash
   terraform init
   ```

2. **Generating proposed changes and auto-executing the plan**
   ```bash
   terraform apply -auto-approve
   ```

3. **Remove all resources managed by terraform**
   ```bash
   terraform destroy
   ```

---

## **Fabric-Specific SQL Queries (Alternative to PostgreSQL):**

### **Setup in Fabric Lakehouse:**

1. Upload files to Lakehouse Files section
2. Load them as Delta tables:
   ```python
   # In Fabric Notebook
   from pyspark.sql import SparkSession
   
   # Read Parquet
   df_trips = spark.read.parquet("Files/green_tripdata_2025-11.parquet")
   df_trips.write.format("delta").mode("overwrite").saveAsTable("green_taxi_trips")
   
   # Read CSV
   df_zones = spark.read.csv("Files/taxi_zone_lookup.csv", header=True)
   df_zones.write.format("delta").mode("overwrite").saveAsTable("taxi_zone_lookup")
   ```

3. Query using SQL Analytics Endpoint (same queries as PostgreSQL)

---

## **Question 3 Example - Fabric SQL:**

```sql
-- Fabric Lakehouse SQL Analytics Endpoint
SELECT COUNT(*) AS trip_count
FROM green_taxi_trips
WHERE DATE(lpep_pickup_datetime) >= '2025-11-01' 
  AND DATE(lpep_pickup_datetime) < '2025-12-01'
  AND trip_distance <= 1.0;
```

**Note:** Fabric Lakehouse uses T-SQL syntax, which is similar to PostgreSQL but with some differences.

---

## **Question 5 Example - Fabric SQL:**

```sql
-- Fabric Lakehouse SQL Analytics Endpoint
SELECT TOP 1
    z.Zone,
    SUM(t.total_amount) AS total_revenue
FROM green_taxi_trips t
INNER JOIN taxi_zone_lookup z 
    ON t.PULocationID = z.LocationID
WHERE CAST(t.lpep_pickup_datetime AS DATE) = '2025-11-18'
GROUP BY z.Zone
ORDER BY total_revenue DESC;
```

---

## **Cost Considerations:**

### **Microsoft Fabric:**
- **Free Trial:** 60-day trial with capacity included
- **Pricing:** Capacity-based pricing (F2, F4, F8, etc.)
- **Best for:** Learning and small to medium workloads

### **Azure Traditional Services:**
- **Azure Database for PostgreSQL:** ~$20-50/month for Basic tier
- **Azure Blob Storage:** ~$0.018/GB per month
- **Azure Data Factory:** Pay per activity run and data movement
- **Free Tier:** Azure Free Account includes 12 months of free services

### **Recommendation for Learning:**
1. Use **Microsoft Fabric free trial** - easiest to get started
2. Or use **Azure Free Account** - $200 credit for 30 days
3. Remember to **delete resources** after homework to avoid charges

---

## **Resources & Documentation:**

### **Microsoft Fabric:**
- [Get Started with Fabric](https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview)
- [Fabric Lakehouse Overview](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview)
- [Fabric Data Pipelines](https://learn.microsoft.com/en-us/fabric/data-factory/data-factory-overview)
- [Fabric Notebooks](https://learn.microsoft.com/en-us/fabric/data-engineering/how-to-use-notebook)

### **Azure Services:**
- [Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/)
- [Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/)
- [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)
- [Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/)

### **Terraform:**
- [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Terraform Azure Examples](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples)

---

## **Recommendation:**

For learning purposes, I'd suggest the following path:

1. **Complete the original homework with Docker + PostgreSQL** (as designed)
   - This teaches you the fundamentals
   - Understand local development workflow
   - No cloud costs

2. **Then recreate it using Microsoft Fabric** for cloud experience
   - Use the free trial
   - Learn cloud-native data engineering
   - Experience unified analytics platform

3. **Use Terraform** to provision resources
   - Start with GCP (as in homework)
   - Then learn Azure provider
   - Compare the two cloud platforms

This gives you both local development skills and cloud platform experience, making you a well-rounded data engineer! 🚀

---

## **Quick Start: 5-Minute Fabric Setup**

```bash
# Step 1: Sign up for Microsoft Fabric
# Visit: https://app.fabric.microsoft.com/
# Use your Microsoft account or create one

# Step 2: Create a Workspace
# Click "Workspaces" > "New workspace"
# Name it "ny-taxi-homework"

# Step 3: Create a Lakehouse
# In workspace, click "New" > "Lakehouse"
# Name it "taxi_lakehouse"

# Step 4: Upload data files
# Click "Files" > "Upload" > "Upload files"
# Upload green_tripdata_2025-11.parquet
# Upload taxi_zone_lookup.csv

# Step 5: Create tables
# Click "New notebook"
# Run the PySpark code above to create tables

# Step 6: Query with SQL
# Click on the SQL analytics endpoint
# Run your SQL queries

# Done! You now have a cloud lakehouse with your data.
```

---

## **Comparison Matrix:**

| Feature | Docker + PostgreSQL | Microsoft Fabric | Azure PostgreSQL |
|---------|-------------------|------------------|------------------|
| **Setup Time** | 30 minutes | 5 minutes | 15 minutes |
| **Cost** | Free | Free trial (60 days) | ~$20-50/month |
| **Scalability** | Limited | Auto-scaling | Manual scaling |
| **Learning Curve** | Moderate | Low | Low |
| **Production Ready** | No | Yes | Yes |
| **SQL Support** | PostgreSQL | T-SQL | PostgreSQL |
| **Data Formats** | Tables only | Parquet, CSV, Delta | Tables only |
| **Best For** | Learning basics | Cloud + Analytics | PostgreSQL in cloud |

---

## **Next Steps:**

After completing this homework, consider exploring:

1. **Stream Processing** with Fabric Eventstreams or Azure Stream Analytics
2. **Machine Learning** with Fabric Data Science or Azure ML
3. **Real-Time Dashboards** with Power BI connected to your Lakehouse
4. **Advanced ETL** with Dataflows Gen2 or Azure Data Factory
5. **Data Governance** with Microsoft Purview
6. **CI/CD Pipelines** for your Terraform code with Azure DevOps

Good luck with your homework! 🎉
