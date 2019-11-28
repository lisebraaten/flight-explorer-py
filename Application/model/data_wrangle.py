import altair as alt
import vega_datasets
import pandas as pd
import numpy as np

#load dataset
path_to_data = "model/airline-safety.csv"
data = pd.read_csv(path_to_data)
#add incidents/accidents/fatalities for both time periods together
data["total_incidents"] = data["incidents_85_99"] + data["incidents_00_14"]

#calculate available seat km per week in billions
data["avail_seat_km_per_week_billions"] = data["avail_seat_km_per_week"]/1000000000

# include only airlines that had incidents
no_zeros = data[data["incidents_85_99"] > 0]
no_zeros_either = no_zeros[no_zeros["incidents_00_14"] > 0]
# create dataset to use for plot2 
data2 = no_zeros_either.drop(columns=["avail_seat_km_per_week", "incidents_85_99", "fatal_accidents_85_99", "incidents_00_14", "fatal_accidents_00_14", "total_incidents"])
data2["fatalities_85_99"] = data2["fatalities_85_99"]/data2["avail_seat_km_per_week_billions"]
data2["fatalities_00_14"] = data2["fatalities_00_14"]/data2["avail_seat_km_per_week_billions"]
data2 = data2.drop(columns="avail_seat_km_per_week_billions")
data2["fatalities_85_99"] = data2["fatalities_85_99"] + data2["fatalities_00_14"]
data2 = data2.drop(columns = "fatalities_00_14")
data2 = data2.rename(columns = {"fatalities_85_99" : "total_fatalities_per_b_avail_seat_km"})
data2 = data2.reset_index().drop(columns="index")

#classify first world countries based on https://www.nationsonline.org/oneworld/first_world.htm
data2["first_world"] = np.zeros(len(data2))
data2["first_world"] = "Other"
data2["first_world"][3,4,6, 7,8, 9, 10, 11, 12, 14, 16, 20, 22, 23, 24, 28, 30, 32, 34, 36, 40, 41, 42] = "First World"

#create data set for boxplot
data3 = no_zeros_either
data3["lethality_85_99"] = data3["fatal_accidents_85_99"]/data3["incidents_85_99"]
data3["lethality_00_14"] = data3["fatal_accidents_00_14"]/data3["incidents_00_14"]
data3 = pd.melt(data3, id_vars="airline", value_vars = ["lethality_85_99", "lethality_00_14"])
                                                        #"incidents_85_99", "incidents_00_14", "fatalities_00_14", "fatalities_85_99", "fatal_accidents_85_99", "fatal_accidents_00_14"])

#final data for charts
chart_2_data = data2
chart_1_data = data3