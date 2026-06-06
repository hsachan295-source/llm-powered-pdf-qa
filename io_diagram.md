# Input / Output Flow (Horizontal)

Here is the horizontal block diagram showing the flow of data:

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

This diagram shows the left-to-right flow: PDF file -> loader -> text aggregation -> LLM + query -> response -> output.

