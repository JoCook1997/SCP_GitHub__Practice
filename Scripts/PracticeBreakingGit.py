# Practice python script for the SCP team to use to create a mrege conflict and try to resolve it
# Jo Cook
# date created: 22/10/2026
# last edited: 22/10/2026


# load libraries
import polars as pl
import matplotlib.pyplot as plt

# read in the first 1000 lines of data from last years GEIC release
data=pl.read_csv("Data/IOTA_GLORIA_full_run_exports_28-Jul-2025_first1000Lines.csv")

# select production in consumption and deforestation data only
data=data.select(["year", "FAO_commodity_name", "FAO_producing_country_name", "GLORIA_region_name", 
                  "production_embedded_in_consumption__tonnes", "def_risk_embedded_in_consumption_amoritized_ha"])

# filter the data
# (as it's only the first 1000 lines it represents the trade of wheat in 2005 for consuming regions "Rest of Americas", 
# "Rest of Europe", "Rest of Africa", "Rest of Asia-Pacific", "Afghanistan", "Angola", "Albania" only)
# Potential to create a merge conflict here if all of us choose a different region to filter by
region="Afghanistan"
data=data.filter(pl.col("GLORIA_region_name")==region)

# make a plot of production in consumption against deforestation risk
# Several opportunities for merge conflicts here by changing the axis titles, figsize, colours etc.
fig, ax=plt.subplots(figsize=(10,6))
ax.scatter(data["production_embedded_in_consumption__tonnes"], data["def_risk_embedded_in_consumption_amoritized_ha"],
           color="orange", marker="x")
ax.set_xlabel("Production in consumption (tonnes)")
ax.set_ylabel("Deforestation in consumption (ha)")
plt.savefig("Visualisations/simple_prod_deforestation_graph_"+region+".png")

print("Done")