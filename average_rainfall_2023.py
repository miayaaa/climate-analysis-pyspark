import pandas as pd
import plotly.express as px


def load_data():
    """Load the dataset containing average rainfall by country."""
    data = pd.read_csv("avg_rainfall_by_country.csv")
    data_2023 = data[data['Year'] == 2023]
    fips_to_iso_df = pd.read_csv("countrycode_convert.csv", sep='\t')
    merged_df = pd.merge(data_2023, fips_to_iso_df,
                         how='left', on='CountryCode')

    return merged_df


def assign_missing_iso_codes(merged_df):
    """If needed, assign missing ISO codes."""
    return merged_df


def plot_rainfall_map(merged_df, title="Average Rainfall in 2023 by Country"):
    """Create a choropleth map to visualize average rainfall in 2023 by country."""
    valid_iso_df = merged_df[merged_df['ISO-3166_alpha3'].notnull()]

    fig = px.choropleth(
        valid_iso_df,
        locations="ISO-3166_alpha3",
        color="AverageRainfall",
        hover_name="CountryName",
        color_continuous_scale="Blues",
        range_color=[0, 2000],  # Adjust range to enhance visibility
        labels={'AverageRainfall': 'Average Rainfall (mm)'},
        title=title
    )

    fig.show()


def check_missing_data(merged_df):
    """Check missing data and how many countries are mapped."""
    num_countries_with_data = merged_df['ISO-3166_alpha3'].notnull().sum()
    num_countries_with_rainfall = merged_df['AverageRainfall'].notnull().sum()

    print(f"Number of countries with valid ISO codes: {
          num_countries_with_data}")
    print(f"Number of countries with rainfall data: {
          num_countries_with_rainfall}")

    # View rainfall data without valid ISO code
    missing_iso_countries = merged_df[merged_df['ISO-3166_alpha3'].isnull()
                                      & merged_df['AverageRainfall'].notnull()]
    print("Countries without valid ISO codes:")
    print(missing_iso_countries[['CountryName', 'AverageRainfall']])


if __name__ == "__main__":
    """Main program entry point."""
    merged_df = load_data()

    check_missing_data(merged_df)

    merged_df = assign_missing_iso_codes(merged_df)

    plot_rainfall_map(merged_df)
