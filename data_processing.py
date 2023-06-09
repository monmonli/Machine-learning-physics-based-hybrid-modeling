import pandas as pd
import miceforest as mf
import numpy as np


class DataProcessing:
 
    def __init__(self,p1_2020,p1_2021):
        self.p1_2020 = p1_2020
        self.p1_2021 = p1_2021
         
    def data_process_20(self):
        p1_2020_data = self.p1_2020[['NB2_S_1_NYZ_sys_x_PcwOut_x', 'NB2_S_1_NYZ_sys_x_PcwIn_x', 'NB2_S_1_NYZ_cwp_9_HzSPR_x', 'NB2_S_1_NYZ_cwp_10_HzSPR_x', 'NB2_S_1_NYZ_cwp_11_HzSPR_x', 'NB2_S_1_NYZ_cwp_12_HzSPR_x', 'NB2_S_x_NYZ_x_x_Fcw_x']].copy()
        p1_2020_nonzero = p1_2020_data.loc[p1_2020_data['NB2_S_x_NYZ_x_x_Fcw_x']>500]
        p1_2020_state = pd.read_csv('EndUserData2020P2CWPState.csv', encoding = 'ISO-8859-1', skiprows = [0,2])
        p1_2020_state_nonzero = p1_2020_state.loc[p1_2020_data['NB2_S_x_NYZ_x_x_Fcw_x']>500]
        p1_2020_nonzero['NB2_S_1_NYZ_cwp_9_HzSPR_x'] = p1_2020_nonzero['NB2_S_1_NYZ_cwp_9_HzSPR_x']\
                                                    * p1_2020_state_nonzero['NB2_S_1_NYZ_cwp_9_State_x']
        p1_2020_nonzero['NB2_S_1_NYZ_cwp_10_HzSPR_x'] = p1_2020_nonzero['NB2_S_1_NYZ_cwp_10_HzSPR_x']\
                                                    * p1_2020_state_nonzero['NB2_S_1_NYZ_cwp_10_State_x']
        p1_2020_nonzero['NB2_S_1_NYZ_cwp_11_HzSPR_x'] = p1_2020_nonzero['NB2_S_1_NYZ_cwp_11_HzSPR_x']\
                                                    * p1_2020_state_nonzero['NB2_S_1_NYZ_cwp_11_State_x']
        p1_2020_nonzero['NB2_S_1_NYZ_cwp_12_HzSPR_x'] = p1_2020_nonzero['NB2_S_1_NYZ_cwp_12_HzSPR_x']\
                                                    * p1_2020_state_nonzero['NB2_S_1_NYZ_cwp_12_State_x']    
        p1_2020_nonzero['p_diff'] =  p1_2020_nonzero['NB2_S_1_NYZ_sys_x_PcwOut_x'] - p1_2020_nonzero['NB2_S_1_NYZ_sys_x_PcwIn_x']

        return p1_2020_nonzero

    def data_process_21(self):
        p1_2021_data = self.p1_2021[['NB2_S_1_NYZ_sys_x_PcwOut_x', 'NB2_S_1_NYZ_sys_x_PcwIn_x', 'NB2_S_1_NYZ_cwp_9_HzSPR_x', 'NB2_S_1_NYZ_cwp_10_HzSPR_x', 'NB2_S_1_NYZ_cwp_11_HzSPR_x', 'NB2_S_1_NYZ_cwp_12_HzSPR_x', 'NB2_S_x_NYZ_x_x_Fcw_x']].copy()
        p1_2021_nonidx = np.where(pd.isnull(p1_2021_data).any(1) == 1)[0]
        p1_2021_data = p1_2021_data.drop(p1_2021_nonidx)
        p1_2021_nonzero = p1_2021_data.loc[p1_2021_data['NB2_S_x_NYZ_x_x_Fcw_x']>500]
        p1_2021_state = pd.read_csv('EndUserData2020P2CWPState.csv', encoding = 'ISO-8859-1', skiprows = [0,2])
        p1_2021_state_nonzero = p1_2021_state.loc[p1_2021_data['NB2_S_x_NYZ_x_x_Fcw_x']>500]
        p1_2021_nonzero['NB2_S_1_NYZ_cwp_9_HzSPR_x'] = p1_2021_nonzero['NB2_S_1_NYZ_cwp_9_HzSPR_x']\
                                                  * p1_2021_state_nonzero['NB2_S_1_NYZ_cwp_9_State_x']
        p1_2021_nonzero['NB2_S_1_NYZ_cwp_10_HzSPR_x'] = p1_2021_nonzero['NB2_S_1_NYZ_cwp_10_HzSPR_x']\
                                                  * p1_2021_state_nonzero['NB2_S_1_NYZ_cwp_10_State_x']
        p1_2021_nonzero['NB2_S_1_NYZ_cwp_11_HzSPR_x'] = p1_2021_nonzero['NB2_S_1_NYZ_cwp_11_HzSPR_x']\
                                                  * p1_2021_state_nonzero['NB2_S_1_NYZ_cwp_11_State_x']
        p1_2021_nonzero['NB2_S_1_NYZ_cwp_12_HzSPR_x'] = p1_2021_nonzero['NB2_S_1_NYZ_cwp_12_HzSPR_x']\
                                                  * p1_2021_state_nonzero['NB2_S_1_NYZ_cwp_12_State_x']    
        p1_2021_nonzero['p_diff'] =  p1_2021_nonzero['NB2_S_1_NYZ_sys_x_PcwOut_x'] - p1_2021_nonzero['NB2_S_1_NYZ_sys_x_PcwIn_x']
        return p1_2021_nonzero
       