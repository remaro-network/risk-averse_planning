import numpy as np

def transform(action, effects):
   ## Ground Probabilistic Effects
      prob_effects = []
      # print(action.probabilistic)
      prob_effects = []
      # print(action.probabilistic)
      delta = 0.5
      immediate_reward =2 #time_step which we need it from planner.py
      prob_effects_list = []
      utility_state = 1
      for prob_effects in action.probabilistic:
         print(prob_effects[0][0])
         # calculate transformation S space to S' space
         """
            # calculate transformation S space to S' space
         U(r) = -delta^r, 0 < delta < 1
         U_exp(r) = etha*delta^r where etha = sgn ln(delta)

         **************************************************
         Delta is a risk factor, r is immediate reward
         probabilities transformation does not change final result 
         in case planner only produces 1 solution
         """
         print(prob_effects[0][0])
         prob_effects_list.append(prob_effects[0][0])
         transformation = np.sign(np.log(delta)) * pow(delta,immediate_reward)
         utility_current_state = 0
         utility_future_state = 0
         utility_state = np.sum(prob_effects[0][0]* transformation * immediate_reward)
         print("Expected Utility State is " + str(utility_state))
         prob_effects.append(tuple([(utility_state, effects(prob_effect[1])) for prob_effect in prob_effects]))

         # self.prob_effects.append(tuple([(prob_effect[0], _effect_grounder(prob_effect[1])) for prob_effect in prob_effects]))
         print(prob_effects[0][0])
         return prob_effects[0][0]