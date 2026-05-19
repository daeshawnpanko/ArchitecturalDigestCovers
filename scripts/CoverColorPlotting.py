import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
"""
This probably shouldve been a notebook but oh well, maybe I'll change it to one later. \
This script reads the CSV file of cover data, imports it into a SQLite database, and then creates bar plots of the primary colors of the covers over time, by season, and by decade.
"""
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the CSV file
csv_path = os.path.join(script_dir, "../data/architectural_digest_covers.csv")

# Path to the SQLite database
db_path = os.path.join(script_dir, "../data/architectural_digest_covers.db")

# Read CSV file
df = pd.read_csv(csv_path)

# Connect to SQLite database (creates if doesn't exist)
conn = sqlite3.connect(db_path)

# Write dataframe to SQLite table
df.to_sql('covers', conn, if_exists='replace', index=False)

springQuery = "SELECT primary_color FROM covers WHERE season = 'Spring' ORDER BY year ASC"
springResult = pd.read_sql_query(springQuery, conn)
SpringColors = springResult['primary_color'].tolist()

summerQuery = "SELECT primary_color FROM covers WHERE season = 'Summer' ORDER BY year ASC"
summerResult = pd.read_sql_query(summerQuery, conn)
SummerColors = summerResult['primary_color'].tolist()

fallQuery = "SELECT primary_color FROM covers WHERE season = 'Fall' ORDER BY year ASC"
fallResult = pd.read_sql_query(fallQuery, conn)
FallColors = fallResult['primary_color'].tolist()

winterQuery = "SELECT primary_color FROM covers WHERE season = 'Winter' ORDER BY year ASC"
winterResult = pd.read_sql_query(winterQuery, conn)
WinterColors = winterResult['primary_color'].tolist()


x_positions = range(len(SpringColors))
plt.bar(x_positions,1, width=1, color=SpringColors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Spring Architectural Digest Covers (1922-2025)')
plt.savefig('./data/spring_colors_alltime.png', dpi=300, bbox_inches='tight')
plt.close()

x_positions = range(len(SummerColors))
plt.bar(x_positions,1, width=1, color=SummerColors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Summer Architectural Digest Covers (1922-2025)')
plt.savefig('./data/summer_colors_alltime.png', dpi=300, bbox_inches='tight')
plt.close()

x_positions = range(len(FallColors))
plt.bar(x_positions,1, width=1, color=FallColors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Fall Architectural Digest Covers (1922-2025)')
plt.savefig('./data/fall_colors_alltime.png', dpi=300, bbox_inches='tight')
plt.close()

x_positions = range(len(WinterColors))
plt.bar(x_positions,1, width=1, color=WinterColors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Winter Architectural Digest Covers (1922-2025)')
plt.savefig('./data/winter_colors_alltime.png', dpi=300, bbox_inches='tight')
plt.close()

_1920Query = "SELECT primary_color FROM covers WHERE Year >= 1920 AND Year < 1930 ORDER BY year ASC"
_1920Result = pd.read_sql_query(_1920Query, conn)
_1920Colors = _1920Result['primary_color'].tolist()

x_positions = range(len(_1920Colors))
plt.bar(range(len(_1920Colors)),1, width=1, color=_1920Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1920-1929)')
plt.savefig('./data/_1920_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_1930Query = "SELECT primary_color FROM covers WHERE Year >= 1930 AND Year < 1940 ORDER BY year ASC"
_1930Result = pd.read_sql_query(_1930Query, conn)
_1930Colors = _1930Result['primary_color'].tolist()

x_positions = range(len(_1930Colors))
plt.bar(range(len(_1930Colors)),1, width=1, color=_1930Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1930-1939)')
plt.savefig('./data/_1930_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_1940Query = "SELECT primary_color FROM covers WHERE Year >= 1940 AND Year < 1950 ORDER BY year ASC"
_1940Result = pd.read_sql_query(_1940Query, conn)
_1940Colors = _1940Result['primary_color'].tolist()

x_positions = range(len(_1940Colors))
plt.bar(range(len(_1940Colors)),1, width=1, color=_1940Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1940-1949)')
plt.savefig('./data/_1940_colors.png', dpi=300, bbox_inches='tight')
plt.close() 

_1950Query = "SELECT primary_color FROM covers WHERE Year >= 1950 AND Year < 1960 ORDER BY year ASC"
_1950Result = pd.read_sql_query(_1950Query, conn)
_1950Colors = _1950Result['primary_color'].tolist()

x_positions = range(len(_1950Colors))
plt.bar(range(len(_1950Colors)),1, width=1, color=_1950Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1950-1959)')
plt.savefig('./data/_1950_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_1960Query = "SELECT primary_color FROM covers WHERE Year >= 1960 AND Year < 1970 ORDER BY year ASC"
_1960Result = pd.read_sql_query(_1960Query, conn)
_1960Colors = _1960Result['primary_color'].tolist()

x_positions = range(len(_1960Colors))
plt.bar(range(len(_1960Colors)),1, width=1, color=_1960Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1960-1969)')
plt.savefig('./data/_1960_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_1970Query = "SELECT primary_color FROM covers WHERE Year >= 1970 AND Year < 1980 ORDER BY year ASC"
_1970Result = pd.read_sql_query(_1970Query, conn)
_1970Colors = _1970Result['primary_color'].tolist()

x_positions = range(len(_1970Colors))
plt.bar(range(len(_1970Colors)),1, width=1, color=_1970Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1970-1979)')
plt.savefig('./data/_1970_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_1980Query = "SELECT primary_color FROM covers WHERE Year >= 1980 AND Year < 1990 ORDER BY year ASC"
_1980Result = pd.read_sql_query(_1980Query, conn)
_1980Colors = _1980Result['primary_color'].tolist()

x_positions = range(len(_1980Colors))
plt.bar(range(len(_1980Colors)),1, width=1, color=_1980Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1980-1989)')
plt.savefig('./data/_1980_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_1990Query = "SELECT primary_color FROM covers WHERE Year >= 1990 AND Year < 2000 ORDER BY year ASC"
_1990Result = pd.read_sql_query(_1990Query, conn)
_1990Colors = _1990Result['primary_color'].tolist()

x_positions = range(len(_1990Colors))
plt.bar(range(len(_1990Colors)),1, width=1, color=_1990Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (1990-1999)')
plt.savefig('./data/_1990_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_2000Query = "SELECT primary_color FROM covers WHERE Year >= 2000 AND Year < 2010 ORDER BY year ASC"
_2000Result = pd.read_sql_query(_2000Query, conn)
_2000Colors = _2000Result['primary_color'].tolist()

x_positions = range(len(_2000Colors))
plt.bar(range(len(_2000Colors)),1, width=1, color=_2000Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (2000-2009)')
plt.savefig('./data/_2000_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_2010Query = "SELECT primary_color FROM covers WHERE Year >= 2010 AND Year < 2020 ORDER BY year ASC"
_2010Result = pd.read_sql_query(_2010Query, conn)
_2010Colors = _2010Result['primary_color'].tolist()

x_positions = range(len(_2010Colors))
plt.bar(range(len(_2010Colors)),1, width=1, color=_2010Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (2010-2019)')
plt.savefig('./data/_2010_colors.png', dpi=300, bbox_inches='tight')
plt.close()

_2020Query = "SELECT primary_color FROM covers WHERE Year >= 2020 AND Year < 2030 ORDER BY year ASC"
_2020Result = pd.read_sql_query(_2020Query, conn)
_2020Colors = _2020Result['primary_color'].tolist() 

x_positions = range(len(_2020Colors))
plt.bar(range(len(_2020Colors)),1, width=1, color=_2020Colors)
plt.xlabel('issue')
plt.ylabel('')
ax = plt.gca()
ax.set_yticks([])
plt.title('Primary Colors of Architectural Digest Covers (2020-2025)')
plt.savefig('./data/_2020_colors.png', dpi=300, bbox_inches='tight')
plt.close()

# Commit and close
conn.commit()
conn.close()

# print(f"Successfully imported {len(df)} rows from {csv_path} to {db_path}")
