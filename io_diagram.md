# Input / Output Flow (Horizontal)

```mermaid
flowchart LR
  A[story.pdf] --> B[PyPDFLoader]
  B --> C[Concatenate text]
  C --> D[ChatGoogleGenerativeAI (Gemini)]
  E[User question] --> D
  D --> F[Response text]
  F --> G[Console output / downstream]
```

This diagram shows the left-to-right flow: PDF file -> loader -> text aggregation -> LLM + query -> response -> output.
