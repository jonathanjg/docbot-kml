# DocBot DSL

DocBot DSL is a small domain-specific language for describing knowledge mapping rules for RAG-DocBot.

The first goal is to let users write controlled statements such as:

```txt
relate chunks where doc_type = "pdf" to entity "audit";