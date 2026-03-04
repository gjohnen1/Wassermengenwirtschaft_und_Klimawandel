from rtctools.simulation.simulation_problem import SimulationProblem
from rtctools.simulation.csv_mixin import CSVMixin
from rtctools.util import run_simulation_problem
import logging
# import reservoir modelling features, stored in reservoir.py:
import reservoir

timestep = 0
logger = logging.getLogger("rtctools")

class BlueRiver(CSVMixin, SimulationProblem):
    csv_validate_timeseries = False
    timestep = 0

    def initialize(self):
        reservoirs_csv_path = '../model/reservoirs.csv'
        volume_level_csv_paths = '../model/volumelevel.csv'
        #read the input files with reservoir data
        self.reservoirs = reservoir.readReservoirData(reservoirs_csv_path, volume_level_csv_paths)

        super().initialize()

    def get_output_variables(self):
        output_variables = super().get_output_variables().copy()
        for res in self.reservoirs:
            output_variables.extend(['{}_V'.format(res), '{}_H'.format(res), '{}_Q_spill'.format(res), '{}_Q_turbine'.format(res)])
        return output_variables

    def update(self, dt):

        operation_mode = 'pass-inflow'
        #operation_mode = 'user-defined-release'
        #operation_mode = 'constant flow'

        # get the volume of the last time step
        res = 'TroutLake'
        volume = self.get_var("{}_V".format(res))
        # compute the pool elevation and add the crest level
        elevation = self.reservoirs[res].volume_to_level(volume)
        self.set_var('{}_H'.format(res), elevation)


        self.timestep += 1
        dt = self.times()[self.timestep] - self.times()[self.timestep-1]
        self.new_time = self.get_current_time() + dt
        self.new_time_date = self.io.sec_to_datetime(self.new_time, self.io.reference_datetime)

        print("*** Simulation time:", self.new_time_date, " ***")

        # pass inflow
        if operation_mode == 'pass-inflow':
            Q = self.timeseries_at('TroutLake_Inflow', self.new_time)
            print("pass inflow")
        # user-defined release, from import time series
        elif operation_mode == 'user-defined-release':
            Q = self.timeseries_at('Q_release_user', self.new_time)
            print("user-defined release")
        # average flow as third option
        else:
            Q = 13.32
        # set Q via the SetRelease function from the reservoir library
        res = "TroutLake"
        reservoir.SetRelease(self, res, Q)

        # move one time step forward
        super().update(dt)

# Run
run_simulation_problem(BlueRiver)
