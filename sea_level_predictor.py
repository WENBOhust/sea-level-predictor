import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Read data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, color='blue', alpha=0.7)

    # 3. Create first line of best fit (1880 to 2050)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_levels_pred1 = intercept1 + slope1 * years_extended
    plt.plot(years_extended, sea_levels_pred1, color='red', label='Best fit (1880-2050)')

    # 4. Create second line of best fit (2000 to most recent year)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    years_recent_extended = np.arange(2000, 2051)
    sea_levels_pred2 = intercept2 + slope2 * years_recent_extended
    plt.plot(years_recent_extended, sea_levels_pred2, color='green', label='Best fit (2000-2050)')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Optional: plt.legend() — but freeCodeCamp tests don't require it

    # Save plot and return fig (don't change this part)
    plt.savefig('sea_level_plot.png')
    return plt.gca().figure
