# 🎬 Movie Analysis & JSON Extractor

An AI-powered web application built with **Streamlit**, **LangChain**, **OpenAI**, and **Pydantic**. This tool converts unstructured text paragraphs, plot summaries, or reviews about movies into validated, schema-compliant **JSON data** (extracting title, director, release year, cast, genres, rating, and summary points).

---

## 📌 Features

* **Unstructured to Structured:** Transforms raw text into clean, structured JSON.
* **Strict Schema Enforcement:** Powered by **Pydantic** and LangChain's `PydanticOutputParser`.
* **Clean UI:** Built with **Streamlit** for interactive text input and instant JSON rendering.
* **Copy-Ready Output:** Displays both interactive JSON trees and formatted raw code blocks.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM Orchestration:** [LangChain](https://www.langchain.com/)
* **Model:** [OpenAI](https://openai.com/) (`gpt-5-nano`)
* **Data Validation:** [Pydantic](https://www.google.com/search?q=https://docs.pydantic.dev/)
* **Environment Management:** `python-dotenv`

---

## 📁 Repository Structure

```text
├── app.py              # Main Streamlit UI and LLM parsing pipeline
├── .env.example        # Example environment variables file
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

```

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python 3.9+ installed and an **OpenAI API Key**.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/movie-script-parser.git
cd movie-script-parser

```

### 3. Create a Virtual Environment & Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here

```

### 5. Run the Application

```bash
streamlit run app.py

```

Open your browser at `http://localhost:8501` to use the app.

---

## 📋 JSON Schema Output Example

```json
{
  "title": "Inception",
  "release_year": 2010,
  "rating": 8.8,
  "genre": [
    "Action",
    "Sci-Fi",
    "Thriller"
  ],
  "cast": [
    "Leonardo DiCaprio",
    "Joseph Gordon-Levitt",
    "Elliot Page"
  ],
  "director": "Christopher Nolan",
  "summary": [
    "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
  ]
}

```
