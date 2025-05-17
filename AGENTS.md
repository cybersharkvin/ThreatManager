# Project Bootstrap: MCP Server (Air-Gapped, Artifact-Driven AI Security Analysis)

This AGENTS.md is intended for use by an automated software engineering agent (e.g., OpenAI Codex) to create the entire MCP server project from scratch.  
**No source files or directories currently exist. All components, scaffolding, and configs must be generated according to these steps, in order.**

---

## 1. Repository Initialization

1. **Initialize a new Git repository.**
   - Command: `git init`
2. **Create a `.gitignore` suitable for Go, Python, Node, Docker, and Kubernetes projects.**

---

## 2. Project Directory Structure

1. **Create the following directories at the repo root:**
    - `/core`              # Orchestration server code
    - `/adapters`          # Ingest, scan, analysis adapters
    - `/deploy/helm`       # Helm charts for all components
    - `/deploy/k8s`        # Kubernetes manifests, RBAC, NetPol
    - `/ui`                # Frontend code (React) and backend API (FastAPI)
    - `/tests`             # Integration and golden artifact tests
    - `/docs/architecture` # Diagrams and onboarding docs

---

## 3. Core Orchestrator Scaffold

1. **In `/core/`, create an empty Go module:**
   - `go mod init github.com/<your-org>/mcp-core`
2. **Create the orchestrator server file:**  
   - `core/mcp_orchestrator.go` (start with a minimal main function and TODO stubs for REST/gRPC endpoints, session mgmt, and job control)
3. **Add placeholder proto/IDL definitions for gRPC API:**
   - `core/api.proto` (document key services: session, ingest, analysis, trace log)

---

## 4. Adapter Shims Scaffold

1. **In `/adapters/`, create initial subfolders:**
   - `/adapters/ingest/`        # Artifact ingest (Gitea, Tika, OCR)
   - `/adapters/scan/`          # Static/dep scanning (Semgrep, Trivy)
   - `/adapters/threatmodel/`   # Threat modeling (ThreatSpec, Cartography)
   - `/adapters/llm/`           # Local LLM interaction
2. **Add a minimal Go or Python file for each adapter, exporting a stub API (REST/gRPC) and placeholder for job logic.**
3. **Create a canonical JSON schema file for normalized adapter outputs:**  
   - `/adapters/schema/scan_result.schema.json`

---

## 5. UI and API Scaffold

1. **In `/ui/`, scaffold a new React app:**  
   - Command: `pnpm create react-app ./ui` (or similar, see your stack)
2. **Add a `backend/` subdir:**  
   - Create `backend/` folder inside `/ui/` for FastAPI/Flask session/audit API.
3. **Add placeholder for audit/session evidence view:**  
   - `ui/src/components/AuditTrail.jsx`
4. **Add a README with setup instructions for the UI.**

---

## 6. Deployment and Infra Scaffold

1. **In `/deploy/helm/`, create chart folders:**  
   - `/deploy/helm/mcp-core/`
   - `/deploy/helm/adapters/`
   - `/deploy/helm/ui/`
   - `/deploy/helm/neo4j/`
   - `/deploy/helm/minio/`
2. **Add Helm `Chart.yaml`, `values.yaml`, and template files for each chart, with TODOs for resource, service, RBAC, and NetPol.**
3. **In `/deploy/k8s/`, add base manifests for RBAC, ServiceAccounts, and default NetworkPolicy.**

---

## 7. Tests and Golden Artifacts

1. **In `/tests/`, create:**
   - `integration/` folder (add a placeholder test file for orchestrator-adapter E2E)
   - `golden/` folder (store sample artifact repos, diagrams, threatmodel YAMLs)
   - Add a minimal test runner config for Go, Python, and JS as appropriate.

---

## 8. Documentation and Architecture Diagrams

1. **In `/docs/architecture/`, add:**
   - `MCP-architecture.md` (paste the architecture blueprint you provided here)
   - `session-flow.md` (outline end-to-end workflow)
   - `components-overview.md`
   - `images/` folder for diagrams (add a placeholder PNG/SVG)

---

## 9. CI/CD and Tooling

1. **At repo root:**
   - Add `drone.yml` (scaffold jobs for lint, test, image build—placeholders ok)
   - Add a base `Dockerfile` in `/core/`, `/adapters/`, `/ui/backend/` as applicable
   - Add `Makefile` or task runner config for bootstrap, test, lint

---

## 10. Security, Secrets, and Hardening

1. **In `/deploy/k8s/`, add:**
   - `sealedsecrets.yaml` (empty placeholder)
   - `vault-config.yaml` (empty placeholder)
2. **Document in `/docs/architecture/security.md` your approach to ephemeral storage, RBAC, and session purge.**

---

## 11. Initial Commit and Push

1. **Stage and commit all created scaffolding.**
2. **Push to the default branch.**

---

## Additional Guidance for Codex Agents

- **Create each directory and file in order, filling in placeholder code, comments, and TODOs as indicated.**
- **Where files are referenced in other files (e.g., proto definitions, API endpoints), ensure import paths and module refs are correct.**
- **Populate all README/markdown docs with summaries of their intended purpose and any architectural notes.**
- **Do not skip setup of test, CI, and deploy scaffolding, even if all are not fully implemented.**
- **If unsure, refer to the architecture context above and annotate all stubs and placeholders for human review.**
- **Split the initial work into small, testable commits for traceability.**

---

**This process ensures the agent bootstraps the MCP server repo from zero, scaffolding all major components and preparing for iterative, test-driven development as per architecture.**
