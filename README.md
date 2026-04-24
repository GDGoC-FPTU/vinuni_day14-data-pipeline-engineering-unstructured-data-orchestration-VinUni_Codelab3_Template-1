[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23701297&assignment_repo_type=AssignmentRepo)
# Codelab 03: The Multi-Modal Minefield
**Author**: Võ Tự Đức (VinUni AI Lab)
**Topic**: Data Pipeline Engineering - Unstructured Data Orchestration

## Overview
In this lab, you will act as a 4-person Data Engineering team. Your goal is to ingest messy, unstructured data from two different sources (PDFs and Videos), normalize it, and unify it into a single, high-quality Knowledge Base for an AI Agent.

This is NOT just about writing Python. This is about **Schema Harmonization** and **Semantic Observability**.

## The Roles
Your team must divide into the following roles. Each role has specific files to edit in the `starter_code/` directory.

### 1. Lead Data Architect (The Strategist) -> `schema.py`
- Defines the `UnifiedDocument` Pydantic model. What fields does the AI actually need?
- Ensures both Group A (PDF) and Group B (Video) data fit into this schema.

### 2. ETL/ELT Builder (The Transformation Lead) -> `process_unstructured.py`
- Parses the messy JSON outputs from the "OCR/Speech-to-Text" services.
- Translates `camelCase` and `snake_case` into the Architect's unified schema.
- Cleans up "noise" (e.g., removing `HEADER_PAGE_1` from PDF text).

### 3. Observability & QA Engineer (The Watchman) -> `quality_check.py`
- Writes the "Quality Gates".
- Detects if an extracted document is missing core fields or contains corrupt content (e.g., "Null pointer exception").

### 4. DevOps & Integration Specialist (The Connector) -> `orchestrator.py`
- Glues the entire pipeline together.
- Reads `raw_data/`, passes it to the Builder, sends it through the Watchman's gates, and outputs the final `processed_knowledge_base.json`.

## Instructions
1. Navigate to the `starter_code/` directory.
2. Read the `TODO` comments assigned to your specific role.
3. Collaborate with your team. **The Builder cannot finish their job until the Architect finishes the Schema.**
4. Run `python orchestrator.py` to test your pipeline.
-----------------------------
