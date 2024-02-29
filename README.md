# Source Code
This repository is implementation of `Risk-averse Planning Framework for Marine Robots`

### planGeneration
To see instruction go into planGeneration folder

### planEvaluation
To see instruction go into planGeneration folder

#### Planner

Having executed the run_program inside `planGeneration`, Json file for possible actions generated called `[problemName].actions.json` in results folder, and for visualization you can refer to `[problemName].png`

##### SafePlanner
- We modified [Safe-Planner](https://arxiv.org/abs/2109.11471) which supports extension of PDDL files for probabilistic planning (PPDDL) and it includes all well-known deterministic planners
- system requirement: Refer to [Safe-Planner GitHub](https://github.com/mokhtarivahid/safe-planner)

### Plan Selection
- Using Safe-Planner you can have all possible outcomes, we save the safest plan in graph dot, json, and PNG file. It possible to see other sub-plans in your /tmp folder

### Plan Execution

- To execute specific plan, you should download specific scenario from [remaro_scenarios GitHub](https://github.com/remaro-network/remaro_scenarios)

## Acknowledgements
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 956200.

Pleave visit [our website](https://remaro.eu/) for more info on our project.

![REMARO Logo](https://remaro.eu/wp-content/uploads/2020/09/remaro1-right-1024.png)
