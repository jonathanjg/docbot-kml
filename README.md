# DocBot DSL

DocBot DSL is a small domain-specific language for describing knowledge mapping rules for RAG-DocBot.

The first goal is to let users write controlled statements such as:

```txt
relate chunks where doc_type = "pdf" to entity "audit";
```

This DocBot DSL side project will hopefully be part of [RAG-DocBot project](https://docbot-private.com), where it could be used to define how documents, chunks, entities, and relationships should be mapped for retrieval-augmented generation workflows. My hope is that I can simplify my current query orchestration layer by adding this custom language.
