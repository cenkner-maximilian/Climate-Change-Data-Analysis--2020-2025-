# -- PREPARING DATA --
#Importing Pandas for data cleaning and Matplotlib for data viz
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Loading dataset
    data = pd.read_csv("climate-change-data_2020-2025.csv")

    # Renaming columns for better accessibility and readability
    data.rename(
        columns={"Year": "year", "Continent": "continent", "Country": "country", "Avg_Temperature(°C)": "avg_temp",
                 "CO2_Emissions(Mt)": "co2_ems", "Sea_Level_Rise(mm)": "sea_levels", "Climate_Risk_Index": "cri"},
        inplace=True)

    # -- OBJECTIVE 1 --

    #Creating figure, Setting the position and title of 1st plot
    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
    ax[0,0].plot(data.groupby("year")["sea_levels"].mean(), color="#B7B1F2")
    ax[0,0].set_title("Sea Levels [mm]", fontweight="bold")

    #Position and title of 2nd plot
    ax[0,1].plot(data.groupby("year")["avg_temp"].mean(), color="#B7B1F2")
    ax[0,1].set_title("Average Temperature [°C]", fontweight="bold")

    #Position and title of 3rd plot
    ax[1,0].plot(data.groupby("year")["co2_ems"].mean(), color="#B7B1F2")
    ax[1,0].set_title("C02 Emissions [Millions of tons]", fontweight="bold")

    #Position and title of last plot
    ax[1,1].plot(data.groupby("year")["cri"].mean(), color="#B7B1F2")
    ax[1,1].set_title("Climate Risk Index", fontweight="bold")

    #Title for figure and showing figure
    plt.suptitle("Changes Throughout 2020-2025", fontsize=20, fontweight="bold")
    #plt.savefig("figures/obj_2_analysis.png")
    plt.show()

    year2020 = data[data["year"] == 2020].reset_index(drop=True).sort_values(by="continent")
    year2025 = data[data["year"] == 2025].reset_index(drop=True).sort_values(by="continent")

    # -- OBJECTIVE 2 --


    fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(20, 10))

    #2020 Plot
    ax[0].bar(year2020.continent.unique(), year2020.groupby("continent")["co2_ems"].median(), color="#FDB7EA")
    ax[0].set_title("Year 2020", fontweight="bold", fontsize=15)
    #2025 Plot
    ax[1].bar(year2025.continent.unique(), year2025.groupby("continent")["co2_ems"].median(), color="#FFDCCC")
    ax[1].set_title("Year 2025", fontweight="bold", fontsize=15)

    fig.suptitle("Continent-wise Emissions (2020 versus 2025)", fontweight="bold", fontsize=20)
    #plt.savefig("figures/obj_2_analysis.png")
    plt.show()
    return 0

if __name__ == "__main__":
    main()