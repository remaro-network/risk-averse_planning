# Source Code

## Sub-Folders

### planGeneration

### planEvaluation

### Planner

Having executed the run_program inside `planGeneration`, Json file for possible actions generated called `[problemName].actions.json` in results folder, and for visualization you can refer to `[problemName].png`

##### SafePlanner
- We use [Safe-Planner](https://arxiv.org/abs/2109.11471) which supports extension of PDDL files for probabilistic planning and it includes all well-known deterministic planners. You can visit the github for documentation, source code and examples (should refer to original repo using `submodule` in github). 
- system requirement: Refer to [Safe-Planner GitHub](https://github.com/mokhtarivahid/safe-planner)

### Plan Selection
- Using Safe-Planner you can have all possible outcome, we save the safest plan. It possible to see other sub-plans

### Plan Executor

- To execute specific plan, you should download specific scenario from [remaro_scenarios GitHub](https://github.com/remaro-network/remaro_scenarios)
