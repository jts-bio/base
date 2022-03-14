
# West ED

::: mermaid
graph LR;
   subgraph IV Room
      MI-->7C-->EI-->N-->MI
   end
   subgraph P-Desk
      7P-->EP-->3-->N-->7P
   end
:::

# Process

::: mermaid
sequenceDiagram
   Server->>7P: Pick List Prints
   7P->>Carousel: Gather Components
   C-Rph->>7P: Verifies
:::

::: mermaid
graph TB;
   subgraph CPhT
      Pull[Pull Drugs] --> DEA{If C-II Drugs}
   end
   subgraph RPh
      DEA --> DEAform[Fill Form, RPh Signs]
   end
:::
