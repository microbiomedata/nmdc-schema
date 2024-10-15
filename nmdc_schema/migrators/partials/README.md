# Partials

Partials are migrators that do not fully migrate a database between two named schema versions. Instead, they only
_partially_ migrate a database between two named schema versions. You can think of them as "partial migrators."

In practice, they are imported into "top-level" migrators that use them in combination, to migrate a database between
two named schema versions.

```mermaid
flowchart LR
    dba["Database<br>conforming<br>to Schema A"]

    subgraph "Top-level migrator"
        p1["Partial migrator 1"]
        p2["Partial migrator 2"]
        ellipses["..."]
        pn["Partial migrator N"]
    end

    dbb["Database<br>conforming<br>to Schema B"]
    dba -.-> p1 --> p2 --> ellipses --> pn -.-> dbb
```

An example of a "top level" migrator is `migrator_from_10_2_0_to_11_0_0.py`. That migrator imports the partial migrator,
`migrator_from_10_2_0_to_11_0_0_part_01.py` (among others).