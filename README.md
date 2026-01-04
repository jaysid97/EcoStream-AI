# 🌱 EcoStream AI: Supply Chain Optimizer

EcoStream AI is a **Snowflake Native Application** designed for real-time carbon footprint visibility and optimization.

### 🚀 Key Features
- **Real-time Tracking:** Live GPS and IoT data ingestion via Snowpipe.
- **Eco-Mode AI:** Uses **Snowflake Cortex** (Llama3-70b) to recommend low-carbon shipping routes.
- **Serverless Analytics:** **Snowpark Python** for high-performance carbon math without data movement.

### 🛠️ Technology Stack
- **Data Cloud:** Snowflake
- **Compute:** Snowpark Python
- **AI/LLM:** Snowflake Cortex
- **Frontend:** Streamlit

### 📥 Setup Instructions
1. Run `setup_queries.sql` in your Snowflake Worksheet to create the database and sample data.
2. Create a new Streamlit App in Snowflake and paste the contents of `streamlit_app.py`.