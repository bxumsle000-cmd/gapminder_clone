import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

connection= sqlite3.connect("data/gapminder.db")
plotting= pd.read_sql("""SELECT * FROM plotting ;""",con=connection)
connection.close()


fig,ax = plt.subplots()
def update_plot(year_to_plot :int):
    ax.clear()
    subset_df= plotting[plotting["dt_year"] == year_to_plot]
    lex = subset_df["life_expectancy"].values
    gdp_per_cap= subset_df["gdp_per_capita"].values
    cont= subset_df["continent"].values
    color_map= {
        "asia" : "y",
        "africa" : "k",
        "europe" : "b",
        "americas" : "c"
    }
    for xi, yi, ci in zip(gdp_per_cap, lex, cont):
        ax.scatter(xi, yi, color= color_map[ci])
    ax.set_title(f"THE WORLD in {year_to_plot}")
    ax.set_xlabel("GdP PER CAPITAL(in USD)")
    ax.set_ylabel("LIFE_EXPECTANCY")
    ax.set_xlim(0,100000)
    ax.set_ylim(20,100)

ani= animation.FuncAnimation(fig, func=update_plot, frames=range(1800,2024),interval=50)
ani.save("animation.gif",fps=10)
