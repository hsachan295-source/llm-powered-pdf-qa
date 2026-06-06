# LLM-powered PDF QA

A simple demo that loads a PDF, concatenates its text, and queries a Google generative LLM (Gemini) for answers.

Features
- Load PDF pages with `PyPDFLoader`.
- Concatenate full document text and pass it to `ChatGoogleGenerativeAI`.
- Example query flow implemented in `main.py`.

Files
- [main.py](main.py#L1-L26) — example script that loads `story.pdf` and queries the model.
- [io_diagram.md](io_diagram.md) — diagram showing the input/output flow.

## Input / Output Flow

Here is the horizontal block diagram showing the flow of data in this project:

![Input/Output Flow](io_diagram.png)

### System Architecture Flowchart

```mermaid
flowchart LR
    %% Define block styles
    classDef input fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b,font-weight:bold;
    classDef process fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c,font-weight:bold;
    classDef model fill:#e8f5e9,stroke:#388e3c,stroke-width:2px,color:#1b5e20,font-weight:bold;
    classDef output fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#e65100,font-weight:bold;

    %% Nodes
    A["📄 story.pdf\n(Input File)"]:::input
    B["⚙️ PyPDFLoader\n(Document Loader)"]:::process
    C["📝 Concatenator\n(Full Text Builder)"]:::process
    D["🤖 Gemini LLM\n(gemini-3.5-flash)"]:::model
    E["❓ User Query\n(Human Message)"]:::input
    F["💬 LLM Response\n(Output Text)"]:::output

    %% Connections
    A --> B
    B --> C
    C --> D
    E --> D
    D --> F
```

Setup
1. Create and activate a Python virtual environment.

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add credentials and the PDF:
- Place your PDF as `story.pdf` in the project root.
- Create a `.env` file with your Google credentials (example key name shown below). The exact variable depends on the Google client you use; try `GOOGLE_API_KEY` or follow the provider docs.

Example `.env`:

```
GOOGLE_API_KEY=your_api_key_here
```

Usage
1. Ensure `story.pdf` is present.
2. Run the script:

```bash
python main.py
```

If everything is configured the script will print the model's response to the console.

Pushing to your GitHub repo
1. Initialize git (if not already):

```bash
git init
git add .
git commit -m "Add project files and README"
```

2. Add your remote and push (replace with your repo URL):

```bash
git remote add origin https://github.com/hsachan295-source/llm-powered-pdf-qa.git
git branch -M main
git push -u origin main
```

Notes
- The `requirements.txt` includes the main libraries used in `main.py`. If your environment uses different package names, update accordingly.
