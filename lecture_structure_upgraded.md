# Refined Idea: Advanced Online Lecture — Data Pipeline Engineering
**Author**: Võ Tự Đức (VinUni AI Lab)
**Topic**: "Dữ liệu bẩn vào - AI rác ra - Bạn có đang âm thầm phá hoại Model?"

---

## 1. Executive Summary & Improvements
The core objective is to move from **CSV-level cleaning** to **Unstructured Data Orchestration (PDF/Video)**. Modern AI Agents (RAG/Multi-modal) live or die by the quality of their chunks and embeddings. 

### **Key Improvements to the Base Idea:**
1.  **Semantic Observability**: Instead of just monitoring "Is the file there?", students will build monitors for "Is the content coherent?".
2.  **The "Conflict" Factor (Group Work)**: Introduce **Schema Harmonization**. Groups must merge disparate data sources (PDF text + Video tags) into a single unified knowledge base, forcing them to resolve naming and metadata conflicts.
3.  **Local "Agentic" Pipeline**: Using Python's `unstructured` library or lightweight local models to simulate production environments without complex cloud overhead.

---

## 2. Updated Schedule (09:00 – 13:00)

### **Phase 1: Theory & Extension (09:00 – 10:00)**
*   **09:00 - 09:20: The "Zillow" Story Recap & The Silent Failure**: Why conventional testing fails for AI. Visualizing "Semantic Drift" in embeddings.
*   **09:20 - 09:40: Multi-Modal Ingestion Patterns**:
    *   **PDFs**: Handling Layout vs. Logic (Tables, Footnotes, OCR artifacts).
    *   **Videos**: Frame extraction, Transcript cleaning, and Visual description pipelines.
*   **09:40 - 10:00: Data Contracts for Unstructured Data**: Defining "What is a good chunk?". Introduction to **Semantic Guardrails**.

### **Phase 2: The Multi-Modal Minefield Lab (10:00 – 12:30)**

#### **Part 1: Personal Challenge — "The PDF Purge" (60 mins)**
*   **Task**: Process a folder of "Messy PDFs" (Mixed languages, bad formatting).
*   **Goal**: Create a cleanup pipeline that:
    1.  Strips noise (Headers/Page numbers).
    2.  Normalizes text (Unicode stability).
    3.  **Quality Gate**: Write an "Integrity Checker" that tags chunks as `HIGH_QUALITY`, `MESSY`, or `CORRUPT`.
*   **Grading**: Automated tests against the personal `processed_output.json`.

#### **Part 2: Group Challenge — "The Knowledge Merger" (90 mins)**
*   **Setup**: Breakout rooms. Group A receives **PDF Data**; Group B receives **Video-to-Text Metadata**.
*   **Task**: Combine these two radically different sources into a single "Master Knowledge Base" for an AI Agent.
*   **The Conflict**: Group A used camelCase, Group B used snake_case. Group A categorized by "Theme," Group B by "Object Type."
*   **The Win Condition**: Create a **Harmonization Script** that transforms both sources into a unified Schema for a Vector DB.

### **Phase 3: Final Grading & Forensic Review (12:30 – 13:00)**
*   **Live Leaderboard**: Students submit their "Master CSV/JSON". We run a "Forensic Agent" that asks trick questions based on the messy source data.
*   **The Winner**: The group whose Agent gives the most accurate answer despite the "trash" in the original files.

---

## 3. Evaluation & Grading Matrix

| Component | Weight | Criteria |
| :--- | :--- | :--- |
| **Personal (Execution)** | 40% | Successful processing of all 5 "Nightmare PDFs" without manual intervention. |
| **Personal (Observability)** | 20% | Quality of the "Log Dashboard" (Did they catch the corrupt files?). |
| **Group (Harmonization)** | 30% | Zero schema conflicts in the final merged data. |
| **Final Accuracy** | 10% | AI Agent performance in the 12:30 Quiz. |

---

## 4. Technical Stack (Local Environment)
*   **Ingestion**: `unstructured` or `PyMuPDF`.
*   **Processing**: `pandas`, `pydantic` (for Schema Enforcement).
*   **Verification**: `Great Expectations` (Optional) or Custom Python Assertion Suites.
*   **Agent Simulation**: A provided Python script that runs a RAG-style query on their local data.

---

## 5. Standard Group Roles & Collaboration (Guru Framework)
To mirror a real-world Data Engineering team, each group (4 members) will follow a strict **Role-Based Collaboration** model. Individual contributions will be tracked via **GitHub Classroom commit history**.

### **Role 1: Lead Data Architect (The Strategist)**
*   **Accountability**: The Final Knowledge Base Schema.
*   **Primary Task**: Defines the **Data Contract** (JSON/CSV structure) that all members must adhere to.
*   **GitHub Focus**: Managing the `schema.json` and reviewing Pull Requests to ensure no "illegal" columns or naming conventions enter the master branch.

### **Role 2: ETL/ELT Builder (The Transformation Lead)**
*   **Accountability**: Data Extraction Fidelity.
*   **Primary Task**: Writing the core Python scripts to process PDFs/Videos. Focuses on **Normalization** (Unicode, date formats, category mapping).
*   **GitHub Focus**: Main logic scripts (e.g., `process_unstructured.py`).

### **Role 3: Observability & QA Engineer (The Watchman)**
*   **Accountability**: Data Integrity & Semantic Gates.
*   **Primary Task**: Implementing the **Quality Gates**. Writes the "Integrity Checker" and logging systems to detect "garbage" chunks before they hit the final DB.
*   **GitHub Focus**: Validation suites and monitoring scripts (e.g., `quality_check.py`).

### **Role 4: DevOps & Integration Specialist (The Connector)**
*   **Accountability**: Pipeline Orchestration & Agent Readiness.
*   **Primary Task**: Ensuring the final output is formatted correctly for the AI Agent. Manages the **Main Orchestrator** script that triggers ETL -> QA -> Load.
*   **GitHub Focus**: Repository structure, `requirements.txt`, and ensuring the **GitHub Actions** (Autograding) pass.

---

## 6. GitHub Classroom Workflow
1.  **Repository Setup**: One student (DevOps Lead) initializes the team repository.
2.  **Feature Branching**: Each role works on their specific script in a named branch (e.g., `feature/observability-suite`).
3.  **Peer Review**: Architect must approve PRs before merging to `main`.
4.  **Auto-Grading**: Contributions will be weighted by the density and relevance of commits to their assigned role.
