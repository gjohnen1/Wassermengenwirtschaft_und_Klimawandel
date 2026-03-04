from rtctools.optimization.collocated_integrated_optimization_problem \
    import CollocatedIntegratedOptimizationProblem
from rtctools.optimization.goal_programming_mixin \
    import GoalProgrammingMixin, Goal, StateGoal
from rtctools.optimization.modelica_mixin import ModelicaMixin
from rtctools_interface.optimization.goal_generator_mixin import GoalGeneratorMixin
from rtctools_interface.optimization.plot_goals_mixin import PlotMixin
from rtctools.optimization.pi_mixin import PIMixin
#from rtctools.optimization.csv_mixin import CSVMixin
from rtctools_diagnostics.export_results import ExportResultsEachPriorityMixin
from rtctools.util import run_optimization_problem 
import logging

logger = logging.getLogger("rtctools")

class StateRangeGoal(StateGoal):
    """
    A state goal applies for each state variable and each time step.
    """
    def __init__(self, optimization_problem, target_min, target_max, variable, priority, weight, order=1):
        self.target_min = target_min
        self.target_max = target_max
        self.state = variable
        self.priority = priority
        self.weight = weight
        self.order = order
        super(StateRangeGoal, self).__init__(optimization_problem)

class RateOfChangeGoal(Goal):
    """
    Keep a rate of change within range (in m3/s).
    As rate of change is not a model state (but a derivative of it), the Goal class must be used instead of the StateGoal class.
    N.B. A drawdown is here defined with positive values, such that a raise in waterlevel resuls in negative values
    """
    def __init__(self, optimization_problem, target_min, target_max, variable, priority, weight, function_range, function_nominal=1):
        self.state = variable
        self.priority = priority
        self.target_min = target_min
        self.target_max = target_max
        self.function_range = function_range
        self.function_nominal = function_nominal   
        self.order = 2  # use 2 to let the square be minimized (= RTC default)
        # NOTE: change order to 4 or 6 (Hession not constant!!!) to improve accuracy of this target
        # the objective function term is the time derivative of the state
    def function(self, optimization_problem, ensemble_member):
        return optimization_problem.der(self.state)        # m3/s

class StateMinimizationGoal(StateGoal):
    """
    A state goal applies for each state variable and each time step.
    This goal is used to minimize the state variable.
    """
    def __init__(self, variable, priority, weight=1.0, function_nominal=1.0, order=1):
        self.state = variable
        self.priority = priority
        self.weight = weight
        self.function_nominal=function_nominal
        self.order = order

class BlueRiver(ExportResultsEachPriorityMixin, PlotMixin, GoalGeneratorMixin, GoalProgrammingMixin, PIMixin, ModelicaMixin, CollocatedIntegratedOptimizationProblem):
    csv_equidistant = False
    """
    A basic example for introducing users to RTC-Tools 2, based on the HEC-ResPRM case
    """

    plot_max_rows = 4
# path goals apply for each time step individually
    def path_goals(self):
# make sure that no other goals are overwritten        
        g = super().path_goals()
# The objectives (goals) for the reservoir system:
# 010 Reservoir volume goal for flood control
#        g.append(StateRangeGoal(self, 505066826.8963750, 715419465.7775500, 'TroutLake_V', 1, 1.0))
# 020 Reservoir volume goal for recreation boating
#        g.append(StateRangeGoal(self, 616740918.8, 629075737.1, 'TroutLake_V', 3, 0.1))
# 030 Flow range goal for River City
#        g.append(StateRangeGoal(self, 7.044311236, 23.48103745, 'RiverCity_Q', 2, 0.9))
# 040 Reservoir release goal for recreation rafting
#        g.append(StateRangeGoal(self, self.get_timeseries('Rafting_Qmin'), self.get_timeseries('Rafting_Qmax'), 'TroutLake_Q_out', 2, 1.0))
# 050 Rate of change goal for the reservoir volume: pass inflow (no volume change), priority = 0
#        dt = self.times()[1] - self.times()[0]
#        g.append(RateOfChangeGoal(self, 0, 0, 'TroutLake_V', 1, 1.0, [-10, 10],1/dt))
# 055 Set release goal, don't use with with other flow range goal and release goal
#        g.append(StateRangeGoal(self, self.get_timeseries('Q_release_user'), self.get_timeseries('Q_release_user'),'TroutLake_Q_out', 0, 1.0, 2))
# 060 Minimize spill flow (priority 10, weight = 1.0, nominal = 1.0, order = 1)
#        g.append(StateMinimizationGoal('TroutLake_Q_spill', 10, 1.0, 1.0, 1))
#        logger.info('Number of goals added: {}'.format(len(g)))
        return g

# other goals (not path goals), e. g. average or total values, not used here
    def goals(self):
        g = super().goals()
        return g

# constraints         
    def constraints(self, ensemble_member):
        constraints = super(BlueRiver, self).constraints(ensemble_member).copy()
        # for the following locations, the volume at t0 and at t_end must be the same.
        location = ['TroutLake_V']
        for i in [0, -1]:
            times = self.times(location[i])
#            constraints.append((self.state_at(location[i], times[0], ensemble_member) - self.state_at(location[i], times[-1],ensemble_member),0.0, 0.0))
        return constraints

# Run
if __name__ == "__main__":
    run_optimization_problem(BlueRiver, log_level=logging.INFO)
