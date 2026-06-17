# 🧭 WonderWise — Multi-Agent Travel Planner

👉 **Live App**: https://wonderwise-k5hpmmu4feskczig9ktrko.streamlit.app/

**WonderWise** is a **multi-agent AI travel planning application** built with **Streamlit**, **LangGraph**, and **Groq LLMs**.  
It uses multiple specialized AI agents that collaborate to research destinations, recommend experiences, and generate a complete day-by-day travel itinerary.

This project is **interview-ready** and demonstrates real **agentic AI architecture** (not a single-prompt chatbot).

---

## 🧠 What Makes WonderWise Agentic?

WonderWise is a **true multi-agent system**, where each agent has a distinct responsibility:

### 🤖 Agents Involved

1. **Destination Research Agent**  
   - City overview  
   - Weather during travel dates  
   - Best time to visit  
   - Practical travel tips  

2. **Experiences & Attractions Agent**  
   - Top attractions  
   - Food & culture  
   - Activities based on user interests  

3. **Itinerary Planning Agent**  
   - Synthesizes outputs from other agents  
   - Generates a structured, day-by-day itinerary  

Agents communicate through a **shared state** using **LangGraph**, not by copying prompts.

---

## 📊 System Overview

- **Architecture**: Multi-Agent Workflow (LangGraph)  
- **LLM Provider**: Groq  
- **Model Used**: `llama-3.1-8b-instant` (stable)  
- **Search Tool**: Google Search (Serper API)  
- **Frontend**: Streamlit  

---

## 🛠 Tech Stack

| Layer        | Tools Used                                   |
|-------------|-----------------------------------------------|
| Frontend    | Streamlit                                     |
| Agent Orchestration | LangGraph                              |
| LLM         | Groq (`llama-3.1-8b-instant`)                 |
| Search      | Google Serper API                             |
| Backend     | Python                                        |
| Environment | python-dotenv                                 |
| Deployment  | Streamlit Cloud (live link above)             |

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/gupta04mohit/WonderWise.git
cd WonderWise
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

If that doesn’t work:

```powershell
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Set Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY="your_groq_api_key_here"
SERPER_API_KEY="your_google_serper_api_key_here"
```

> ⚠️ API keys must be inside quotes

### 6️⃣ Run the App

```bash
streamlit run app.py
```

### 7️⃣ Open in Browser

```
http://localhost:8501
```

---

## 🌐 Deployment

The application is deployed on **Streamlit Cloud** and available publicly:

🔗 [https://wonderwise-k5hpmmu4feskczig9ktrko.streamlit.app/](https://wonderwise-k5hpmmu4feskczig9ktrko.streamlit.app/)

---

## 📁 Project Structure

```
WonderWise/
│
├── app.py                  # Streamlit UI
├── graph.py                # LangGraph multi-agent workflow
├── agents/
│   ├── destination.py      # Destination research agent
│   ├── experiences.py      # Attractions & activities agent
│   └── itinerary.py        # Planner agent
│
├── tools/
│   └── google_search.py    # Google Serper search tool
│
├── requirements.txt
└── .gitignore
```

---

## 👤 Author

**Name**: Mohit Gupta 

**GitHub**: [https://github.com/gupta04mohit/Mohitgupta](https://github.com/gupta04mohit/Mohitgupta)

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 📢 Share it with peers
* 💼 Mention it in interviews (this is a solid agentic AI project)

---

## 📝 Notes

* This is **not** a simple prompt-based chatbot
* Demonstrates **real agent separation, orchestration, and synthesis**
* Ideal for **GenAI / Agentic AI / LLM Engineer interviews**
* Easy to extend with:

  * Budget agent
  * Hotel booking agent
  * Flight comparison agent

---

Happy building and exploring the world with agents 🌍🧠


