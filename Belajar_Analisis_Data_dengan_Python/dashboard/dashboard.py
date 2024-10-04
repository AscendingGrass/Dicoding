import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_page_config(layout="wide")


data_paths = {
    "data_clean": ("data_clean.csv", "https://github.com/AscendingGrass/Dicoding/raw/refs/heads/master/Belajar%20Analisis%20Data%20dengan%20Python/dashboard/data_clean.csv"),
    "norm_seasonal_avg": ("normalized_seasonal_avg_pollution.csv", "https://github.com/AscendingGrass/Dicoding/raw/refs/heads/master/Belajar%20Analisis%20Data%20dengan%20Python/dashboard/normalized_seasonal_avg_pollution.csv"),
    "seasonal_avg": ("seasonal_avg_pollution.csv", "https://github.com/AscendingGrass/Dicoding/raw/refs/heads/master/Belajar%20Analisis%20Data%20dengan%20Python/dashboard/seasonal_avg_pollution.csv"),
    "yearly_avg": ("yearly_avg_pollution.csv", "https://github.com/AscendingGrass/Dicoding/raw/refs/heads/master/Belajar%20Analisis%20Data%20dengan%20Python/dashboard/yearly_avg_pollution.csv"),
    "yearly_avg_pct": ("yearly_avg_pollution_percentage_increase.csv", "https://github.com/AscendingGrass/Dicoding/raw/refs/heads/master/Belajar%20Analisis%20Data%20dengan%20Python/dashboard/yearly_avg_pollution_percentage_increase.csv"),
}

# data_clean columns: No,PM2.5,PM10,SO2,NO2,CO,O3,TEMP,PRES,DEWP,RAIN,wd,WSPM,station,time,season,season_name
# norm_seasonal_avg columns: PM2.5,PM10,SO2,NO2,CO,O3
# seasonal_avg columns: PM2.5,PM10,SO2,NO2,CO,O3
# yearly_avg columns: PM2.5,PM10,SO2,NO2,CO,O3
# yearly_avg_pct columns: PM2.5,PM10,SO2,NO2,CO,O3

pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
warned = False
data = {}
for name, (path, url) in data_paths.items():
    try:
        data[name] = pd.read_csv(path)
        if name == "data_clean":
            data[name]["time"] = pd.to_datetime(data[name]["time"])
    except:
        if warned is False:
            st.warning("Failed to load from local path, downloading data from GitHub: https://github.com/AscendingGrass/Dicoding")
            warned = True
        print(f"Warning, failed to load from local path, downloading {name} from {url}")
        data[name] = pd.read_csv(url)
        if name == "data_clean":
            data[name]["time"] = pd.to_datetime(data[name]["time"])

# make the dashboard wider
st.title("Dashboard")
expander = st.expander("Informasi Kolom")


expander.markdown("""
- PM2.5: Particulate matter with a diameter of 2.5 micrometers or less (μg/m³). These fine particles can affect human health.
- PM10 : Particulate matter with a diameter of 10 micrometers or less (μg/m³). These are larger than PM2.5 but still harmful.
- SO2  : Sulfur dioxide concentration (μg/m³), a gas commonly associated with air pollution.
- NO2  : Nitrogen dioxide concentration (μg/m³), another pollutant that can affect respiratory health.
- CO   : Carbon monoxide concentration (mg/m³), a harmful gas resulting from incomplete combustion.
- O3   : Ozone concentration (μg/m³), which can contribute to smog and affect respiratory health.
- TEMP : Temperature (°C), the air temperature at the time of recording.
- PRES : Atmospheric pressure (hPa or millibars), which can influence weather patterns.
- DEWP : Dew point (°C), the temperature at which air becomes saturated and dew forms.
- RAIN : Precipitation amount (mm), indicating how much rainfall occurred.
- wd   : Wind direction, likely categorical (e.g., "N" for north, "S" for south).
- WSPM : Wind speed (m/s), indicating the speed of the wind.
""")


frame1, frame2 = st.columns(2)
with frame1:
    columns = st.multiselect("Pilih kolom", pollutants, default=pollutants[0])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Polusi per-tahun")
        mode = st.selectbox("Pilih mode", ["normal", "persentase perubahan"])

        if mode == "normal":
            yearly_avg_df = data["yearly_avg"]

            
            plt.figure(figsize=(10, 6))
            for pollutant in columns:
                sns.lineplot(x=[2013, 2014, 2015, 2016, 2017], y=yearly_avg_df[pollutant], marker='o', label=pollutant)
            plt.xticks([2013, 2014, 2015, 2016, 2017])

            # Set labels and title
            plt.title(f"Perubahan rata-rata polusi per tahun", fontsize=16)
            plt.xlabel("Tahun")
            plt.ylabel(f"Level polusi")
            st.pyplot(plt)
        elif mode == "persentase perubahan":
            yearly_avg_pct_df = data["yearly_avg_pct"]

            plt.figure(figsize=(10, 6))
            for pollutant in columns:
                sns.lineplot(x=[2014, 2015, 2016, 2017], y=yearly_avg_pct_df[pollutant].iloc[1:], marker='o', label=pollutant)
            plt.xticks([2014, 2015, 2016, 2017],  ["2013-2014", "2014-2015", "2015-2016", "2016-2017"])

            # Set labels and title
            plt.title(f"Persentase perubahan rata-rata polusi per tahun", fontsize=16)
            plt.xlabel("Tahun")
            plt.ylabel(f"Persentasi perubahan dari [x-1] ke [x]")
            st.pyplot(plt)

    with col2:
        st.markdown("### Polusi per-musim")
        mode = st.selectbox("Pilih mode", ["normal", "normalized"])

        if mode == "normal":
            seasonal_avg_df = data["seasonal_avg"]

            plt.figure(figsize=(10, 6))
            for pollutant in columns:
                sns.lineplot(x=[1, 2, 3, 4], y=seasonal_avg_df[pollutant], marker='o', label=pollutant)
            plt.xticks([1, 2, 3, 4], ["Spring", "Summer", "Autumn", "Winter"])

            # Set labels and title
            plt.title(f"Rata-rata polusi per-musim", fontsize=16)
            plt.xlabel("Musim")
            plt.ylabel(f"Level polusi")
            st.pyplot(plt)
        elif mode == "normalized":
            norm_seasonal_avg_df = data["norm_seasonal_avg"]

            plt.figure(figsize=(10, 6))
            for pollutant in columns:
                sns.lineplot(x=[1, 2, 3, 4], y=norm_seasonal_avg_df[pollutant], marker='o', label=pollutant)
            
            plt.xticks([1, 2, 3, 4], ["Spring", "Summer", "Autumn", "Winter"])

            # Set labels and title
            plt.title(f"rata-rata polusi per-musim ternormalisasi", fontsize=16)
            plt.xlabel("Musim")
            plt.ylabel(f"Nilai")
            st.pyplot(plt)

with frame2:
    threshold = st.number_input("threshold minimal korelasi", min_value=0.0, max_value=1.0, step=0.05)
    st.markdown(f"### Korelasi antar data")
    correlation_table = data["data_clean"][pollutants + ["TEMP","PRES","DEWP","RAIN","WSPM"]].corr()
    
    st.dataframe(correlation_table[correlation_table.abs() >= threshold] )

