import numpy as np
import pandas as pd

from typing import List, Union


def readReservoirData(reservoirs_csv_path, volume_level_csv_paths):
    res_df = pd.read_csv(reservoirs_csv_path, sep=",", index_col=0)
    vh_data_df = pd.read_csv(volume_level_csv_paths, sep=",", index_col=0)
    reservoirs = {}
    for index, row in res_df.iterrows():
        reservoirs[index] = Reservoir(index, vh_data_df.loc[index], row)
        reservoirs[index].set_Vsetpoints()

    return reservoirs

def SetRelease(self, res, Quser):
    # applies a (user-defined) release timeseries to a reservoir and distributes this release on turbine and spill according to reservoir parameters
    # physial limits for turbine and flow
    _Qturbine_max = self.reservoirs[res].properties['q_turbine_max']
    _Qspill_max = self.reservoirs[res].properties['q_spill_max']
    # _Qbottomoutlet_max = self.reservoirs[res].properties['q_bottomoutlet_max']
    # the user-defined total release

    # the portion that goes through the turbine
    Qturbine = min(_Qturbine_max, Quser)
    # the portion that goes through the lower valves
    # _Q_bottomoutlet = min(_Qbottomoutlet_max,(_Q_user - Qturbine))
    # the portion that goes through the spillway depends on the crestheight.
    if self.get_var("{}_V".format(res)) > self.reservoirs[res].Vsetpoints['crestheight']:
        Qspill = min(_Qspill_max, (Quser - Qturbine))
    else:
        Qspill = 0.0
    # the remainder must stay in the reservoir.
    Qremainder = Quser - Qturbine - Qspill
    print("SetRelease: {}, distributed to Qturbine = {},  Qspill =  {}, Qremainder =  {} (not released, remains in reservoir)".format(
        Quser, Qturbine, Qspill, Qremainder))

    # assign the values to the time series
    parameters = ['Q_turbine', 'Q_spill']
    parameterdict = {'Q_turbine': Qturbine, 'Q_spill': Qspill}
    for parameter in parameters:
        timeseriesID = '{}_{}'.format(res, parameter)
        self.set_var(timeseriesID, parameterdict[parameter])
    # Qout is calculated by Modelica

class Reservoir():

    def __init__(self, name, vh_data, reservoir_properties):
        self.__vh_lookup = vh_data
        self.name = name
        self.properties = reservoir_properties


    def level_to_volume(self, levels: Union[float, np.ndarray]):
        return np.interp(levels, self.__vh_lookup['Elevation_m'], self.__vh_lookup['Storage_m3'])

    def volume_to_level(self, volumes: Union[float, np.ndarray]):
        return np.interp(volumes, self.__vh_lookup['Storage_m3'], self.__vh_lookup['Elevation_m'])

    def set_Vsetpoints(self):
        # define interpolated volume setpoints corresponding to heights used in goals:
        self.Vsetpoints = {}
        self.Vsetpoints['surcharge'] = self.level_to_volume(self.properties['surcharge'])
        self.Vsetpoints['fullsupply'] = self.level_to_volume(self.properties['fullsupply'])
        self.Vsetpoints['crestheight'] = self.level_to_volume(self.properties['crestheight'])


