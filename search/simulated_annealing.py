from search.local_search_base import LocalSearchBase
import math
import random

class SimulatedAnnealing(LocalSearchBase):
    def run(self, initial_state, **kwargs):
        """
        TODO: Implement the Simulated Annealing algorithm.
        
        Parameters
        ----------
        initial_state : list of tuples
            The initial configuration of sensors.
        **kwargs : 
            Define and add all necessary parameters required for Simulated Annealing 

        Returns
        -------
        best_state : list of tuples
        best_cost : int or float
        evaluations : list
        states_history : list of lists
        """
        
        current_state = initial_state
        current_cost=self.evaluate(current_state)
        evaluations=[current_cost]
        states_history=[current_state]
        best_state=current_state
        best_cost=current_cost
        temp=kwargs.get('initial_temp',100)
        min_temp=kwargs.get('min_temp',0.01)
        d_rate=kwargs.get('d_rate',0.97)
        iteration=kwargs.get('iteration',25)

        while temp > min_temp:
            for i in range (iteration):
                neighbor=self.get_neighbor(current_state)
                next_cost=self.evaluate(neighbor)
                delta_E=current_cost - next_cost
                if delta_E>0 :
                    current_state=neighbor
                    current_cost=next_cost
                    evaluations.append(current_cost)
                    states_history.append(current_state)
                else:
                    probability=math.exp(delta_E/temp)
                    if random.random()<probability:
                        current_state=neighbor
                        current_cost=next_cost
                        evaluations.append(current_cost)
                        states_history.append(current_state)

            if current_cost<best_cost:
                best_state=current_state
                best_cost=current_cost

            temp=temp*d_rate
        return best_state,best_cost,evaluations,states_history