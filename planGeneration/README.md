
### Plan Generation using Safe-Planner

This planner is determinising a probablisitc plans using Strong Cyclic Solutions (SCS) and supports extended PDDL files (PPDDL). For determinising, there exist all classical planners, i.e [Fast Forward (FF)](https://fai.cs.uni-saarland.de/hoffmann/ff.html), [Fast Downward (FD)](https://www.fast-downward.org/ObtainingAndRunningFastDownward), [Temporal planner (LPG-td)](https://lpg.unibs.it/lpg/), etc. 
There are two possible ways to get outcome from the planner: single-outcome vs all-outcomes (In default, we use `--all-outcome` or `-a`)

By installing GraphViz via pip, you can see all possible paths. Consider that finding plan using safe-planner is like BFS search algorithm by default.

#### Usage

```python
python3 run_program.py
```
#### Notes
Problem and Domain should be separated from each other. You can change filenames and folders.

#### Example

You can look for results including statistical of generating plans and also dot graph or PNG file of generated plan in <b>results</b> folder.

##### parameters in run_program.py
you can change name of deterministic planners although is not in the objective of this research work.

`-c <PLANNERS_LIST>`: a list of planners for dual planning mode, e.g., `-c ff` or `-c ff m` or `-c ff m fd`, ...

To see all possible sub-plans separately, you can find all paths in tmp folder (currently). 
