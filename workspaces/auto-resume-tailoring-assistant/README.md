# Auto Resume/CV Tailoring Assistant

An experimental n8n workflow designed to automatically tailor resumes based on specific Job Descriptions (JD). The system guarantees **zero hallucination** by using a local Master Profile as a single Source of Truth and employs an advanced RAG (Retrieval-Augmented Generation) pipeline via Qdrant to semantically match your past projects to job requirements.

## 🌟 Key Features

1. **Factual Integrity**: Never invents experiences. All projects and skills are strictly pulled from the user's `master_profile.json`.
2. **Semantic Search (RAG)**: Uses Qdrant Vector Database to understand the meaning behind a job description and pull the 3 most relevant portfolio projects.
3. **Dynamic DOCX Templating**: A built-in Python FastAPI microservice (`docxtpl_service`) to render MS Word documents natively. Supports infinite project loops and dynamic links without breaking MS Word styling.
4. **Human-in-the-Loop**: Integrated with Telegram for manual review and approval before the final CV is generated.

---

## 🏗 System Architecture

The architecture is split into several interconnected components running via Docker Compose:

- **n8n**: The central orchestration engine.
- **Qdrant**: Vector database for RAG (Semantic Search).
- **DOCX Engine**: A lightweight Python/FastAPI microservice running Jinja2 (`docxtpl`) to generate the final Word document.
- **Telegram Bot**: User interface for triggering requests and reviewing outputs.

### Workflow Phases

1. **Phase 1: Data Ingestion (One-off / Sync)**
   - Reads the Master Profile (`master_profile.json`).
   - Generates embeddings for all projects and skills.
   - Upserts vectors to the `resume_projects` collection in Qdrant.
   
2. **Phase 2: JD Retrieval & Tailoring (Main Pipeline)**
   - Triggered via Telegram command (e.g., `/update_resume <Job Description>`).
   - Extracts required skills from JD using an AI Information Extractor.
   - Queries Qdrant to find the top 3 most relevant projects.
   - Sends a summary to Telegram for user approval.
   - Upon approval, the AI rewrites the summary/bullets and sends JSON data to the DOCX Engine.
   - The final tailored `.docx` is sent back to the user via Telegram.

---

## 🚀 Setup & Installation

### 1. Prerequisites
- Docker & Docker Compose
- API Keys for your preferred AI Model (e.g., OpenAI or Google Gemini via n8n).
- Telegram Bot Token.

### 2. Start Services
Run the following command in the root directory:
```bash
docker compose up -d --build
```
This will start `n8n` (Port: 5678), `qdrant` (Port: 6333), and the `docx_engine` (Port: 8000).

### 3. Configure Master Profile
Edit the `master_profile.json` file in this workspace with your authentic professional details, skills, and projects. **This data serves as the Ground Truth for the AI.**

### 4. Prepare Your CV Template
1. Open `Riki_Ruswandi_CV_Dynamic.docx` in MS Word.
2. Note the use of Jinja2 tags (e.g., `{% for proj in projects %}`). You can edit fonts, margins, and styles directly in Word. The DOCX Engine will preserve all formatting.
3. Import this document into your n8n workflow using a **Read File** node.

---

## 🛠 Usage in n8n

Ensure you have created the two primary workflows in your n8n dashboard:
1. **Ingestion Workflow**: Pushes data from `master_profile.json` into Qdrant.
2. **Retrieval Workflow**: Connects Telegram -> Qdrant -> AI Agent -> DOCX Engine (`http://docx_engine:8000/render`) -> Telegram.

*Happy Tailoring!*
