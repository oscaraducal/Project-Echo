# Data

## Purpose

Data-driven assets: Data Assets, Data Tables, Enums, and Structs used to tune and configure gameplay without hardcoding values in graphs.

## Allowed Assets

- `DA_` Data Assets
- Data Tables
- Blueprint Enums / Structs (as approved)
- Related data-only assets

## Examples

- `DataAssets/`, `DataTables/`, `Enums/`, `Structs/`

## Best Practices

- Prefer Data Assets for tunable values (ranges, costs, timings).
- Version save-related data carefully when schemas change.
- Do not store art or Blueprint class graphs here.
