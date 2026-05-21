# n8n Automation Workspaces

Welcome to the central repository for managing **n8n-based automation workflows**. This repository is designed with a multi-workspace structure to simplify management, version tracking, and collaboration for business automation workflows development.

---

## Repository Structure

This repository uses a simple monorepo structure with workspace isolation to separate each automation project alongside its specific dependencies (such as Docker Compose configurations, persistent data volumes, and workflow export files).

```bash
.
├── .gitignore
├── README.md               # Main repository documentation (English)
├── README.id.md            # Repository documentation (Bahasa Indonesia)
└── workspaces/             # Automation projects directory
    └── blog-content-engine/   # B2B automated blog content engine workspace
```

---

## Workspaces List

Currently, this repository manages the following active workspace:

| Workspace | Version | Core Components | Short Description |
| :--- | :---: | :--- | :--- |
| [**Blog Content Engine**](workspaces/blog-content-engine/README.md) | `v3.3.1` | n8n, Qdrant, Google Gemini | An SEO-friendly B2B blog article generator powered by RAG (Retrieval-Augmented Generation) to guarantee content factual accuracy based on modules and real-world case studies knowledge base. |

---

## General Prerequisites

To run any workflow inside this repository, ensure your system has the following installed:
*   [Docker](https://docs.docker.com/get-docker/) (Version 20.10+)
*   [Docker Compose](https://docs.docker.com/compose/install/) (Version 2.0+)
*   An active internet connection to pull Docker images and access external APIs (such as Google Gemini API).

---

## Getting Started

To start using a workspace:

1.  **Clone the Repository**:
    ```bash
    git clone <repository-url> n8n-automation
    cd n8n-automation
    ```

2.  **Select & Run the Project**:
    Navigate to your preferred workspace directory and spin up the services. For example, for the `blog-content-engine`:
    ```bash
    cd workspaces/blog-content-engine
    docker compose up -d
    ```

3.  **Access n8n**:
    Open your browser and navigate to the n8n dashboard: `http://localhost:5678`

4.  **Import the Workflow**:
    Import the workflow JSON file (such as `core.json`) directly into your n8n dashboard interface.

---

## Contribution & Git Policies

*   **Commit Pattern**: This repository strictly enforces the [Conventional Commits](https://www.conventionalcommits.org/) standard. All commit messages must be written in **English** using the following formats:
    *   `feat: <description>` for a new feature.
    *   `fix: <description>` for a bug fix.
    *   `docs: <description>` for documentation updates.
*   **Version Tagging**: Since this is a monorepo with multiple independent workspaces, version tagging must use **Scoped Tagging** to prevent version conflict:
    *   Format: `<workspace-name>@v<version>` (Example: `blog-content-engine@v3.3.1`)
*   **Credentials Safety**: **Strictly prohibited** to commit `.env` files containing sensitive API keys or production credentials. Use `.env.example` templates if required.

---
Documentation managed by mikeu-dev.
