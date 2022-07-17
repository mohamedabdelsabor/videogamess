# %% [markdown]
# ## Libraries

# %%
import pandas as pd 
import numpy as np
from dash import dcc, Dash, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input,Output ,MATCH
import plotly.figure_factory as ff
import dash_bootstrap_components as dbc
# pio.templates
import numpy as np
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# %% [markdown]
# ## Reading dataset

# %%
vgsales = "vgsales.csv"
companies = "video-games-developers.csv"
ps4_data = pd.read_csv('PS4_GamesSales.csv' ,encoding = 'windows-1252')


# %%
data_df = pd.read_csv(vgsales)


# %%
region_df = pd.read_csv(companies)


# %%

# %% [markdown]
# ## Data Cleaning

# %%
#Column wise null values in train data set 
null_vgd_perc = pd.DataFrame((data_df.isnull().sum())*100/data_df.shape[0]).reset_index()
null_vgd_perc.columns = ['Column Name', 'Null Values Percentage']
null_vgd_value = pd.DataFrame(data_df.isnull().sum()).reset_index()
null_vgd_value.columns = ['Column Name', 'Null Values']
null_vgd = pd.merge(null_vgd_value, null_vgd_perc, on='Column Name')


# %% [markdown]
# ## Imputation Years

# %%
year_data = data_df['Year']

# %%
max_entry = year_data.idxmax()
max_entry = data_df.iloc[max_entry]

# %%
data_df['Year'] = data_df['Year'].replace(2020.0, 2009.0)

# %%
game_missedyear = data_df[data_df['Year'].isnull()]["Name"].unique()

# %%
data_df['Year'] = data_df['Year'].fillna(2009.0)

# %%
data_df['Year']=data_df['Year'].astype('int')

# %% [markdown]
# ## Publisher Imputation


# %%
data_df = data_df.dropna()

# %% [markdown]
# ## Region_df cleaning

# %%

# %%
region_country = pd.DataFrame(region_df['country_code'].value_counts())
r = pd.DataFrame(region_df['Country'].value_counts())

# %%
region_country.reset_index(inplace = True)
region_country.rename(columns = {'index':'country_code', 'country_code':'count'}, inplace = True)

# %%
fig27 = px.choropleth(region_country, locations="country_code",
                    color="count", 
                    hover_name = 'count',
                    template = 'seaborn',
                    color_continuous_scale=px.colors.sequential.Plasma ,title = 'Number of Developers around the world' )


# %% [markdown]
# ## PS4 Games Sales

# %%
rockstar = ps4_data[ps4_data.Publisher == 'Rockstar Games']
activision = ps4_data[ps4_data.Publisher == 'Activision']
sony = ps4_data[ps4_data.Publisher == 'Sony Interactive Entertainment']
bethesda = ps4_data[ps4_data.Publisher == 'Bethesda Softworks']

# %% [markdown]
# ## who is the best company sales

# %%
# fig_24 = px.scatter(rockstar, x = 'Global', y=["North America","Europe","Japan"] , trendline = 'ols')
# fig_24

# %%
# fig1 = plt.subplots(figsize = (10,5))
# plt.plot(activision.Global,activision['North America'],color = 'red',label = 'North America')
# plt.plot(activision.Global,activision['Europe'],color = 'green',label = 'Europe')
# plt.plot(activision.Global,activision['Japan'],color = 'blue',label = 'Japan')
# plt.legend()
# plt.xlabel('Global Sale')
# plt.show()

# %%
# fig = plt.subplots(figsize = (10,5))
# plt.plot(sony.Global,sony['North America'],color = 'red',label = 'North America')
# plt.plot(sony.Global,sony['Europe'],color = 'green',label = 'Europe')
# plt.plot(sony.Global,sony['Japan'],color = 'blue',label = 'Japan')
# plt.legend()
# plt.xlabel('Global Sale')
# plt.show()

# %%
# plt.subplots(figsize = (10,5))
# plt.plot(bethesda.Global,bethesda['North America'],color = 'red',label = 'North America')
# plt.plot(bethesda.Global,bethesda['Europe'],color = 'green',label = 'Europe')
# plt.plot(bethesda.Global,bethesda['Japan'],color = 'blue',label = 'Japan')
# plt.legend()
# plt.xlabel('Global Sale')
# plt.show()

# %% [markdown]
# ## Adding Country codes

# %%

# %%
df = pd.merge(data_df, region_df[['Developer', 'Country']], left_on='Publisher', right_on='Developer')


# %%
df_country = pd.DataFrame(df['Country'].value_counts())
df_country.reset_index(inplace=True)
df_country.rename(columns = {'index':'Country', 'Country':'Count'}, inplace = True)

# %%
condition_one = df_country["Country"] == 'United States'
condition_two = df_country["Country"] == 'Japan'
condition_three = df_country["Country"] == 'Europe'
condition_four = df_country["Country"] == 'United Kingdom'
condition_five = df_country["Country"] == 'France'
condition_six = df_country["Country"] == 'Germany'
condition_seven = df_country["Country"] == 'South Korea'
condition_eight = df_country["Country"] == 'Russia'
condition_nine = df_country["Country"] == 'Norway'
condition_ten = df_country["Country"] == 'Czech Republic'

conditions = [condition_one, condition_two, condition_three, condition_four, condition_five
             , condition_six , condition_seven , condition_eight ,
              condition_nine , condition_ten]
choices = ["USA", "JPN" , "ITA" , "GBR" , "FRA" , "DEU" , "KOR" , "RUS" , 
           "NOR" , "CZE"]
df_country["country_code"] = np.select(conditions, choices, default="")

# %%
condition_one = df["Country"] == 'United States'
condition_two = df["Country"] == 'Japan'
condition_three = df["Country"] == 'Europe'
condition_four = df["Country"] == 'United Kingdom'
condition_five = df["Country"] == 'France'
condition_six = df["Country"] == 'Germany'
condition_seven = df["Country"] == 'South Korea'
condition_eight = df["Country"] == 'Russia'
condition_nine = df["Country"] == 'Norway'
condition_ten = df["Country"] == 'Czech Republic'

conditions = [condition_one, condition_two, condition_three, condition_four, condition_five
             , condition_six , condition_seven , condition_eight ,
              condition_nine , condition_ten]
choices = ["USA", "JPN" , "EUR" , "GBR" , "FRA" , "DEU" , "KOR" , "RUS" , 
           "NOR" , "CZE"]
df["country_code"] = np.select(conditions, choices, default="")

# %% [markdown]
# ## Plots

# %%

# %%
fig26 = px.choropleth(df_country, locations="country_code",
                    color="Count", 
                    hover_data = ['Country' , 'Count'],
                    hover_name = 'Count',
                    color_continuous_scale=px.colors.sequential.Plasma ,title = 'Number of Game Studios around the world' )

# %%
fig27 = px.choropleth(region_country, locations="country_code",
                    color="count", 
                    hover_name = 'count',
                    color_continuous_scale=px.colors.sequential.Plasma ,title = 'Number of Developers around the world' )

# %%
total_sales_column = "Total_Sales"

# %%
if 'Total_Shipped' in data_df.columns:
    data_df[total_sales_column] = data_df['Total_Shipped'].fillna(0) + data_df['Global_Sales'].fillna(0)
else:
    regions = ['NA', 'JP', 'EU', 'Other']
    region_sales_sufix = '_Sales'
    
    data_df[total_sales_column] = data_df['Global_Sales']

# %%
tdf = data_df.copy()
# tdf['Year'] = df['Year'].fillna(df['Year'].mean())
tdf = data_df[data_df['Year'].notna()] # Carefull about this
tdf = tdf.sort_values('Year', ascending=True)


# %% [markdown]
# ## EDA

# %%
games = data_df['Name'].unique()
publisher = data_df['Publisher'].unique()
platforms = data_df['Platform'].unique()
genres = data_df['Genre'].unique()

# %%


# %%
# fig_1 = go.Figure()
# fig_1.add_trace(go.Indicator(
#     mode = "number",
#     value = len(games),
#     title = {'text': "Games",'font': {'color': '#ffed24','size':20}},
#     number={'font':{'color': '#ffed24','size':50}},
#     domain = {'row': 0, 'column': 0}
# ))
# fig_1.add_trace(go.Indicator(
#     mode = "number",
#     value = len(publisher),
#     title = {'text': "Publishers",'font': {'color': '#f0d5c2','size':20}},
#     number={'font':{'color': '#f0d5c2','size':50}},
#     domain = {'row': 0, 'column': 1}
# ))

# fig_1.add_trace(go.Indicator(
#     mode = "number",
#     value = len(platforms),
#     title = {'text': "Platforms",'font': {'color': '#faef73','size':20}},
#     number={'font':{'color': '#faef73','size':50}},
#     domain = {'row': 0, 'column': 2}
# ))

# fig_1.add_trace(go.Indicator(
#     mode = "number",
#     value = len(genres),
#     title = {'text': "Genres",'font': {'color': '#f28e46','size':20}},
#     number={'font':{'color': '#f28e46','size':50}},
#     domain = {'row': 0, 'column': 3}
# ))

# fig_1.update_layout(
#     grid = {'rows': 1, 'columns': 4, 'pattern': "independent"})
# fig_1.show()

# %%
yearwisegame =  data_df.groupby('Year')['Name'].count().reset_index()

# %%
# Yearwise Total Game Published
fig_2 = go.Figure(go.Bar(x=yearwisegame['Year'],y=yearwisegame['Name'],
                       marker={'color': yearwisegame['Name'],'colorscale': 'tealgrn'}))
fig_2.update_layout(title_text='Video Game Release by Year' ,xaxis_title="Year",yaxis_title="Number of Games Released")

# %%
# Video Game Sales by Year
yearwisesale =  data_df.groupby('Year')['Global_Sales'].sum().reset_index()

# %%
# Yearwise Total Game Sales
fig_3 = go.Figure(go.Bar(x=yearwisesale['Year'],y=yearwisesale['Global_Sales'],
                       marker={'color': yearwisesale['Global_Sales'],'colorscale': 'tealgrn'}))
fig_3.update_layout(title_text='Video Game Global Sales by Release Year',xaxis_title="Year",yaxis_title="Sum of Sales")

# %% [markdown]
# ### Publisher wise analysis

# %% [markdown]
# #### Number of game releases

# %%
# Video Game releases by Publisher ( Number of games released by this publisher)
pubwisegame =  data_df.groupby('Publisher')['Name'].count().reset_index()
pubwisegame = pubwisegame.sort_values('Name',ascending=False).reset_index()
pubwisegame.drop("index",axis = 1,inplace=True)

# %%
# Video Game Global Sales by Publisher
pubwisegamesale =  data_df.groupby('Publisher')['Global_Sales'].sum().reset_index()
pubwisegamesale = pubwisegamesale.sort_values('Global_Sales',ascending=False).reset_index()
pubwisegamesale.drop("index",axis = 1,inplace=True)

# %%
# Initialize figure
fig_4 = go.Figure()

# Add Traces
fig_4.add_trace(
    go.Bar(x=pubwisegame['Publisher'][:10],
           y=pubwisegame['Name'][:10],
           name="Top 10 C",
          marker={'color': pubwisegame['Name'][:10],'colorscale': 'tealgrn'}))
fig_4.add_trace(
    go.Bar(x=pubwisegame['Publisher'][:50],
           y=pubwisegame['Name'][:50],
           name="Top 50 C",
           marker={'color': pubwisegame['Name'][:50],'colorscale': 'tealgrn'},
           visible=False))

fig_4.add_trace(
    go.Bar(x=pubwisegamesale['Publisher'][:10],
           y=pubwisegamesale['Global_Sales'][:10],
           name="Top 10 S",
          marker={'color': pubwisegamesale['Global_Sales'][:10],'colorscale': 'tealgrn'} ,visible = False))

fig_4.add_trace(
    go.Bar(x=pubwisegamesale['Publisher'][:50],
           y=pubwisegamesale['Global_Sales'][:50],
           name="Top 50 S",
           marker={'color': pubwisegamesale['Global_Sales'][:50],'colorscale': 'tealgrn'},
           visible=False))

# Update 3D scene options
fig_4.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Add dropdowns
button_layer_1_height = 1.2
fig_4.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="Top 20",
                     method="update",
                     args=[{"visible": [False,False, True, False]},
                           {"title": "Top 10 Publishers Based on Game Releases"}]),
                dict(label="Top 50",
                     method="update",
                     args=[{"visible": [False,False, False, True]},
                           {"title": "Top 50 Publishers Based on Game Releases"}]),
                
            ]),
            direction="down",
            showactive=True,            
            x=0.7,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(label="Game Releases",
                     method="update",
                     args=[{"visible": [True,False, False, False]},
                           {"title": "Top 10 Publishers Based on Game Releases"}]),
                dict(label="Game Sales",
                     method="update",
                     args=[{"visible": [False,True, False, False]},
                           {"title": "Top 50 Publishers Based on Game Sales"}])
            ]),
            direction="down",
            showactive=True,
            x=0.85,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),

    ]
)



# %% [markdown]
# #### Global Sales for each publisher

# %%
df = data_df

# %%
# Video Game Global Sales by Publisher
pubwisegamesale =  data_df.groupby('Publisher')['Global_Sales'].sum().reset_index()
pubwisegamesale = pubwisegamesale.sort_values('Global_Sales',ascending=False).reset_index()
pubwisegamesale.drop("index",axis = 1,inplace=True)

# %%
# Initialize figure
fig_5 = go.Figure()

# Add Traces

fig_5.add_trace(
    go.Bar(x=pubwisegame['Publisher'][:20],
           y=pubwisegame['Name'][:20],
           name="Game Releases",
           marker={'color': pubwisegame['Name'][:20],'colorscale': 'tealgrn'},
           visible=False))

fig_5.add_trace(
    go.Bar(x=pubwisegamesale['Publisher'][:20],
           y=pubwisegamesale['Global_Sales'][:20],
           name="Game Releases",
          marker={'color': pubwisegamesale['Global_Sales'][:20],'colorscale': 'tealgrn'}))

fig_5.update_layout(
    updatemenus=[
        dict(
            type="dropdown",
            direction="down",
            active=0,
            x=1.0,
            y=1.2,
            buttons=list([
                dict(label="Game Releases",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Top 20 Publishers Based on No. of Game Releases"}]),
                dict(label="Game Sales",
                     method="update",
                     args=[{"visible": [False,True]},
                           {"title": "Top 20 Publishers Based on Game Sales"}]),
             
            ]),
        )
    ])

# Set title
fig_5.update_layout(
    title_text="Top 20 Publishers Based on Game Sales",
    xaxis_domain=[0.05, 1.0]
)



# %%
from plotly.tools import FigureFactory as ff
from plotly.offline import init_notebook_mode,iplot

# %%
vgsales = data_df

# %%
xaction=vgsales[vgsales.Genre=="Action"]
xsports=vgsales[vgsales.Genre=="Sports"]
xmisc=vgsales[vgsales.Genre=="Misc"]
xrole=vgsales[vgsales.Genre=="Role-Playing"]
xshooter=vgsales[vgsales.Genre=="Shooter"]
xadventure=vgsales[vgsales.Genre=="Adventure"]
xrace=vgsales[vgsales.Genre=="Racing"]
xplatform=vgsales[vgsales.Genre=="Platform"]
xsimulation=vgsales[vgsales.Genre=="Simulation"]
xfight=vgsales[vgsales.Genre=="Fighting"]
xstrategy=vgsales[vgsales.Genre=="Strategy"]
xpuzzle=vgsales[vgsales.Genre=="Puzzle"]

# %%
trace1 = go.Histogram(
    x=xaction.Platform,
    opacity=0.75,
    name = "Action",
    marker=dict(color='rgb(165,0,38)'))
trace2 = go.Histogram(
    x=xsports.Platform,
    opacity=0.75,
    name = "Sports",
    marker=dict(color='rgb(215,48,39)'))
trace3 = go.Histogram(
    x=xmisc.Platform,
    opacity=0.75,
    name = "Misc",
    marker=dict(color='rgb(244,109,67)'))
trace4 = go.Histogram(
    x=xrole.Platform,
    opacity=0.75,
    name = "Role Playing",
    marker=dict(color='rgb(253,174,97)'))
trace5 = go.Histogram(
    x=xshooter.Platform,
    opacity=0.75,
    name = "Shooter",
    marker=dict(color='rgb(254,224,144)'))
trace6 = go.Histogram(
    x=xadventure.Platform,
    opacity=0.75,
    name = "Adventure",
    marker=dict(color='rgb(170,253,87)'))
trace7 = go.Histogram(
    x=xrace.Platform,
    opacity=0.75,
    name = "Racing",
    marker=dict(color='rgb(171,217,233)'))
trace8 = go.Histogram(
    x=xplatform.Platform,
    opacity=0.75,
    name = "Platform",
    marker=dict(color='rgb(116,173,209)'))
trace9 = go.Histogram(
    x=xsimulation.Platform,
    opacity=0.75,
    name = "Simulation",
    marker=dict(color='rgb(69,117,180)'))
trace10 = go.Histogram(
    x=xfight.Platform,
    opacity=0.75,
    name = "Fighting",
    marker=dict(color='rgb(49,54,149)'))
trace11 = go.Histogram(
    x=xstrategy.Platform,
    opacity=0.75,
    name = "Strategy",
    marker=dict(color="rgb(10,77,131)"))
trace12 = go.Histogram(
    x=xpuzzle.Platform,
    opacity=0.75,
    name = "Puzzle",
    marker=dict(color='rgb(1,15,139)'))

data = [trace1, trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9,trace10,trace11,trace12]
layout = go.Layout(barmode='stack',
                   title='Genre Counts According to Platform',
                   xaxis=dict(title='Platform'),
                   yaxis=dict( title='Count'),
                   paper_bgcolor='beige',
                   plot_bgcolor='beige'
)
fig_20 = go.Figure(data=data, layout=layout)
# %% [markdown]
# #### Top Publishers

# %%
EU = data_df.pivot_table('EU_Sales', columns='Publisher', aggfunc='sum').T
EU = EU.sort_values(by='EU_Sales', ascending=False).iloc[0:5]
EU_publishers = EU.index

JP = data_df.pivot_table('JP_Sales', columns='Publisher', aggfunc='sum').T
JP = JP.sort_values(by='JP_Sales', ascending=False).iloc[0:5]
JP_publishers = JP.index

NA = data_df.pivot_table('NA_Sales', columns='Publisher', aggfunc='sum').T
NA = NA.sort_values(by='NA_Sales', ascending=False).iloc[0:5]
NA_publishers = NA.index

Other = data_df.pivot_table('Other_Sales', columns='Publisher', aggfunc='sum').T
Other = Other.sort_values(by='Other_Sales', ascending=False).iloc[0:5]
Other_publishers = Other.index

Global = data_df.pivot_table('Global_Sales', columns='Publisher', aggfunc='sum').T
Global = Global.sort_values(by='Global_Sales', ascending=False).iloc[0:5]
Global_publishers = Global.index

# %%
# Initialize figure
fig_6 = go.Figure()

# Add Traces

fig_6.add_trace(
    go.Bar(y=NA['NA_Sales'],
           x=NA_publishers,
           name="North America",
          marker={'color': NA['NA_Sales'],'colorscale': 'tealgrn'}))
fig_6.add_trace(
    go.Bar(y=EU['EU_Sales'],
           x=EU_publishers,
           name="Europe",
           marker={'color': EU['EU_Sales'],'colorscale': 'tealgrn'},
           visible=False))
fig_6.add_trace(
    go.Bar(y=JP['JP_Sales'],
           x=JP_publishers,
           name="Japan",
           marker={'color': JP['JP_Sales'],'colorscale': 'tealgrn'},
           visible=False))

fig_6.add_trace(
    go.Bar(y=Other['Other_Sales'],
           x=Other_publishers,
           name="Others",
           marker={'color': Other['Other_Sales'],'colorscale': 'tealgrn'},
           visible=False))

fig_6.add_trace(
    go.Bar(y=Global['Global_Sales'],
           x=Global_publishers,
           name="Global",
           marker={'color': Global['Global_Sales'],'colorscale': 'tealgrn'},
               visible=False ))

fig_6.update_layout(
    updatemenus=[
        dict(
            type="dropdown",
            direction="down",
            active=0,
            x=0.7,
            y=1.2,
            buttons=list([
                dict(label="North America",
                     method="update",
                     args=[{"visible": [True, False,False, False, False]},
                           {"title": "Top 5 Publishers for North America"}]),
                dict(label="Europe",
                     method="update",
                     args=[{"visible": [False,True, False, False, False]},
                           {"title": "Top 5 Publishers for Europe"}]),
                dict(label="Japan",
                     method="update",
                     args=[{"visible": [False,False, True, False, False]},
                           {"title": "Top 5 Publishers for Japan"}]),
                dict(label="Others",
                     method="update",
                     args=[{"visible": [False,False, False, True, False]},
                           {"title": "Top 5 Publishers for Other Region"}]),
                dict(label="Global",
                     method="update",
                     args=[{"visible": [False,False, False, False, True]},
                           {"title": "Top 5 Publishers for Global"}]),
            ]),
        )
    ])

# Set title
fig_6.update_layout(
    title_text="Top 5 Publishers for North America",
    xaxis_domain=[0.05, 1.0]
)


# %% [markdown]
# ### Platform Analysis

# %% [markdown]
# #### Platform video game count

# %%
# Video Game Count by Platform
platform_wise_game =  data_df.groupby('Platform')['Name'].count().reset_index().sort_values("Name",ascending=False)
platform_wise_game = platform_wise_game.reset_index()
platform_wise_game.drop("index",axis = 1,inplace=True)
# Initialize figure
fig_7 = go.Figure()

# Add Traces

fig_7.add_trace(
    go.Bar(x=platform_wise_game['Platform'][:5],
           y=platform_wise_game['Name'][:5],
           name="Top 5",
          marker={'color': platform_wise_game['Name'][:5],'colorscale': 'tealgrn'}))
fig_7.add_trace(
    go.Bar(x=platform_wise_game['Platform'][:10],
           y=platform_wise_game['Name'][:10],
           name="Top 10",
           marker={'color': platform_wise_game['Name'][:10],'colorscale': 'tealgrn'},
           visible=False))
fig_7.add_trace(
    go.Bar(x=platform_wise_game['Platform'][:20],
           y=platform_wise_game['Name'][:20],
           name="Top 20",
           marker={'color': platform_wise_game['Name'][:20],'colorscale': 'tealgrn'},
           visible=False))

fig_7.add_trace(
    go.Bar(x=platform_wise_game['Platform'],
           y=platform_wise_game['Name'],
           name="All",
           marker={'color': platform_wise_game['Name'],'colorscale': 'tealgrn'},
               visible=False ))

fig_7.update_layout(
    title_text="Number of Video Games Per Platform",
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=0.8,
            y=1.2,
            buttons=list([
                dict(label="Top 5",
                     method="update",
                     args=[{"visible": [True, False,False, False]},
                           {"title": "Top 5 Platforms Count Games"}]),
                dict(label="Top 10",
                     method="update",
                     args=[{"visible": [False,True, False, False]},
                           {"title": "Top 10 Platforms Count Games"}]),
                dict(label="Top 20",
                     method="update",
                     args=[{"visible": [False,False, True,False]},
                           {"title": "Top 20 Platforms Count Games"}]),
                dict(label="All",
                     method="update",
                     args=[{"visible": [False,False, False,True]},
                           {"title": "All Platforms Count Games"}]),
            ]),
        )
    ])




# %%
# Video Game Sale by Platform
platform_wise_gamesale =  df.groupby('Platform')['Global_Sales'].sum().reset_index().sort_values("Global_Sales",ascending=False)
platform_wise_gamesale = platform_wise_gamesale.reset_index()
platform_wise_gamesale.drop("index",axis = 1,inplace=True)

# %%
# Video Game Sales by Platform
# Initialize figure
fig_8 = go.Figure()

# Add Traces

fig_8.add_trace(
    go.Bar(x=platform_wise_gamesale['Platform'][:5],
           y=platform_wise_gamesale['Global_Sales'][:5],
           name="Top 5",
          marker={'color': platform_wise_gamesale['Global_Sales'][:5],'colorscale': 'tealgrn'}))
fig_8.add_trace(
    go.Bar(x=platform_wise_gamesale['Platform'][:10],
           y=platform_wise_gamesale['Global_Sales'][:10],
           name="Top 10",
           marker={'color': platform_wise_gamesale['Global_Sales'][:10],'colorscale': 'tealgrn'},
           visible=False))
fig_8.add_trace(
    go.Bar(x=platform_wise_gamesale['Platform'][:20],
           y=platform_wise_gamesale['Global_Sales'][:20],
           name="Top 20",
           marker={'color': platform_wise_gamesale['Global_Sales'][:20],'colorscale': 'tealgrn'},
           visible=False))

fig_8.add_trace(
    go.Bar(x=platform_wise_gamesale['Platform'],
           y=platform_wise_gamesale['Global_Sales'],
           name="All",
           marker={'color': platform_wise_gamesale['Global_Sales'],'colorscale': 'tealgrn'},
               visible=False ,))

fig_8.update_layout(
    title_text="Top 5 Platform Sales",
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=0.8,
            y=1.2,
            buttons=list([
                dict(label="Top 5",
                     method="update",
                     args=[{"visible": [True, False,False, False]},
                           {"title": "Top 5 Platforms Game Sales"}]),
                dict(label="Top 10",
                     method="update",
                     args=[{"visible": [False,True, False, False]},
                           {"title": "Top 10 Platforms Game Sales"}]),
                dict(label="Top 20",
                     method="update",
                     args=[{"visible": [False,False, True,False]},
                           {"title": "Top 20 Platforms Game Sales"}]),
                dict(label="All",
                     method="update",
                     args=[{"visible": [False,False, False,True]},
                           {"title": "All Platforms Game Sales"}]),
            ]),
        )
    ])


# %% [markdown]
# ### Genre Wise Analysis

# %% [markdown]
# #### Video Games count by genre

# %%
# Video Game Count by Genre
genre_wise_game =  df.groupby('Genre')['Name'].count().reset_index().sort_values("Name",ascending=False)
genre_wise_game = genre_wise_game.reset_index()
genre_wise_game.drop("index",axis = 1,inplace=True)
#display()

# %%
fig_9 = go.Figure([go.Pie(labels=genre_wise_game['Genre'], 
                        values=genre_wise_game['Name'],
                        hole=0.3)])  

fig_9.update_traces(hoverinfo='label+percent+value', 
                  textinfo='percent', 
                  textfont_size=15)
fig_9.update_layout(title="Genre Wise Game Count",title_x=0.5)

# %% [markdown]
# #### Each Genre Global Sales

# %%
# Genre wise Game Sales
genre = df.loc[:,['Genre','Global_Sales']]
genre['total_sales'] = genre.groupby('Genre')['Global_Sales'].transform('sum')
genre.drop('Global_Sales', axis=1, inplace=True)
genre = genre.drop_duplicates()

fig_10 = px.pie(genre, names='Genre', values='total_sales', template='seaborn')
fig_10.update_traces(rotation=90, pull=[0.2,0.06,0.06,0.06,0.06], textinfo="percent+label")
fig_10.update_layout(title="Genre Wise Game Sales",title_x=0.5)

# %% [markdown]
# ## Top 5 Games by Genre

# %%
# Top 5 Games by Genre
genre_wise_game= data_df.groupby(['Genre','Name'])['Global_Sales'].sum().reset_index().sort_values(['Genre','Global_Sales'],ascending = (True,False))

# %%
genre = data_df['Genre'].unique()
genre_s = sorted(genre)

# %% [markdown]
# ### Top 5 Games for each Genre

# %%
# Top 5 Games per Genre
fig_11 = go.Figure()
for genre in genre_s:
    dfg = genre_wise_game[genre_wise_game['Genre']==genre]
    fig_11.add_trace(
        go.Bar(x=dfg['Name'][:10],
               y=dfg['Global_Sales'][:10],
               name=genre,
               marker={'color': df['Global_Sales'][:10] ,'colorscale': 'tealgrn'}))
    
fig_11.update_layout(
    updatemenus=[
        dict(
            active=12,
            buttons=list([
                dict(label="Action",
                     method="update",
                     args=[{"visible": [True, False, False, False,False, False, False,False, False, False,False, False]},
                           {"title": "Top 5 Games in Action Genre"}]),
                dict(label="Adventure",
                     method="update",
                     args=[{"visible": [False, True, False, False,False, False, False,False, False, False,False, False]},
                           {"title": "Top 5 Games in Adventure Genre"}]),
                dict(label="Fighting",
                     method="update",
                     args=[{"visible": [False, False, True, False,False, False, False,False, False, False,False, False]},
                           {"title": "Top 5 Games in Fighting Genre"}]),
                dict(label="Misc",
                     method="update",
                     args=[{"visible": [False, False, False, True,False, False, False,False, False, False,False, False]},
                           {"title": "Top 5 Games in Misc Genre"}]),
                dict(label="Platform",
                     method="update",
                     args=[{"visible": [False, False, False, False,True, False, False,False, False, False,False, False]},
                           {"title": "Top 5 Games in Platform Genre"}]),
                dict(label="Puzzle",
                     method="update",
                     args=[{"visible": [False, False, False, False,False, True, False,False, False, False,False, False]},
                           {"title": "Top 5 Games in Puzzle Genre"}]),
                dict(label="Racing",
                     method="update",
                     args=[{"visible": [False, False, False, False,False, False, True,False, False, False,False, False]},
                           {"title": "Top 5 Games in Racing Genre"}]),
                dict(label="Role-Playing",
                     method="update",
                     args=[{"visible": [False, False, False, False,False, False, False,True, False, False,False, False]},
                           {"title": "Top 5 Games in Role-Playing Genre"}]),
                dict(label="Shooter",
                     method="update",
                     args=[{"visible": [False, False, False, False,False, False, False,False, True, False,False, False]},
                           {"title": "Top 5 Games in Shooter Genre"}]),
                dict(label="Simulation",
                     method="update",
                     args=[{"visible": [False, False, False, False,False, False, False,False, False, True,False, False]},
                           {"title": "Top 5 Games in Simulation Genre"}]),
                dict(label="Sports",
                     method="update",
                     args=[{"visible": [False, False, False, False,False, False, False,False, False, False,True, False]},
                           {"title": "Top 5 Games in Sport Genre"}]),
                dict(label="Strategy",
                     method="update",
                     args=[{"visible": [False, False, False, False,False, False, False,False, False, False,False, True]},
                           {"title": "Top 5 Games in Strategy Genre"}]),
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, True, True,True, True, True,True, True, True,True, True]},
                           {"title": "Top 5 Games in All games Genres"}]),
                
            ]),
        )
    ])
fig_11.update_layout(title_text="Top 5 Games per each Genre")


# %% [markdown]
# #### Region Sales per Game

# %%
na_sales=[]
eu_sales=[]
jp_sales=[]
other_sales=[]
global_sales=[]
for i in genre_s:
    val=df[df.Genre==i]
    na_sales.append(val.NA_Sales.sum())
    eu_sales.append(val.EU_Sales.sum())
    jp_sales.append(val.JP_Sales.sum())
    other_sales.append(val.Other_Sales.sum())


# %%
fig_12 = go.Figure()
fig_12.add_trace(go.Bar(x=na_sales,
                     y=genre_s,
                     name='North America Sales',
                     marker_color='#83e6ab',
                     orientation='h'))
fig_12.add_trace(go.Bar(x=eu_sales,
                     y=genre_s,
                     name='Europe Sales',
                     marker_color='#42bda3',
                     orientation='h'))
fig_12.add_trace(go.Bar(x=jp_sales,
                     y=genre_s,
                     name='Japan Sales',
                     marker_color='#33a7a2',
                     orientation='h'))
fig_12.add_trace(go.Bar(x=other_sales,
                     y=genre_s,
                     name='Other Region Sales',
                     marker_color='#257d98',
                     orientation='h'))
fig_12.update_layout(title_text='Region Wise Game Sales by Genre',xaxis_title="Sales in $M",yaxis_title="Genre",
                  barmode='stack')

# %%
publisher_genre= data_df.groupby(['Genre','Publisher'])['Name'].count().reset_index()

# %%
# fig_13 = px.scatter(publisher_genre, x="Publisher", y="Name", color='Genre' , hover_name= 'Publisher')

# fig_13.update_layout(title='Genre wise Game count per Publisher',xaxis_title="Publisher",yaxis_title="Game Count")
# fig_13.update_xaxes(categoryorder='total descending')
# fig_13.show()

# %% [markdown]
# ### Global & Regional Sales

# %%
from plotly.subplots import make_subplots

# %%
# Top 5 Videos Generated by Global Sales
EU = data_df.pivot_table('EU_Sales', columns='Name', aggfunc='sum').T
EU = EU.sort_values(by='EU_Sales', ascending=False).iloc[0:5]
EU_games = EU.index

JP = data_df.pivot_table('JP_Sales', columns='Name', aggfunc='sum').T
JP = JP.sort_values(by='JP_Sales', ascending=False).iloc[0:5]
JP_games = JP.index

NA = data_df.pivot_table('NA_Sales', columns='Name', aggfunc='sum').T
NA = NA.sort_values(by='NA_Sales', ascending=False).iloc[0:5]
NA_games = NA.index

Other = data_df.pivot_table('Other_Sales', columns='Name', aggfunc='sum').T
Other = Other.sort_values(by='Other_Sales', ascending=False).iloc[0:5]
Other_games = Other.index

# %%
fig_14 = go.Figure()

fig_14.add_trace(
    go.Bar(y=NA['NA_Sales'],
           x=NA_games,
           name="North America",
          marker={'color': NA['NA_Sales'],'colorscale': 'tealgrn'})
         )
fig_14.add_trace(
    go.Bar(y=EU['EU_Sales'],
           x=EU_games,
           name="Europe",
           marker={'color': EU['EU_Sales'],'colorscale': 'tealgrn'},
           ))
fig_14.add_trace(
    go.Bar(y=JP['JP_Sales'],
           x=JP_games,
           name="Japan",
           marker={'color': JP['JP_Sales'],'colorscale': 'tealgrn'},
           ))

fig_14.add_trace(
    go.Bar(y=Other['Other_Sales'],
           x=Other_games,
           name="Other",
           marker={'color': Other['Other_Sales'],'colorscale': 'tealgrn'},
           ))

fig_14.update_layout(
title_text = 'Top Games Sales for each region' , 
updatemenus=[
        dict(
            type="dropdown",
            direction="down",
            active=0,
            x=0.9,
            y=1.25,
            buttons=list([
                dict(label="Worldwide",
                     method="update",
                     args=[{"visible": [True,True, True,True]},
                           {"title": "Top Games Sales for each region"}]),
                dict(label="North America",
                     method="update",
                     args=[{"visible": [True, False,False, False]},
                           {"title": "North America Best Games Sales"}]),
                dict(label="Europe",
                     method="update",
                     args=[{"visible": [False,True, False, False]},
                           {"title": "Europe Best Games Sales"}]),
                dict(label="Japan",
                     method="update",
                     args=[{"visible": [False,False, True,False]},
                           {"title": "Japan Best Games Sales"}]),
                dict(label="Rest of World",
                     method="update",
                     args=[{"visible": [False,False, False,True]},
                           {"title": "Rest of the world Top Games Sales"}]),
                
            ]),
        )
    ])

# %%
# # Initialize figure
# fig_14 = make_subplots(
#     rows=2, cols=2, subplot_titles=("North Americal", "Europe", "Japan","Other"),
#     column_widths=[0.5, 0.5],
#     row_heights=[0.5, 0.5],
#     specs=[[{"type": "bar"}, {"type": "bar"}],
#            [ {"type": "bar"}, {"type": "bar"}]])
# # Add Traces

# fig_14.add_trace(
#     go.Bar(y=NA['NA_Sales'],
#            x=NA_games,
#            name="North America",
#           marker={'color': NA['NA_Sales'],'colorscale': 'hot'})
#          ,row=1, col=1)
# fig_14.add_trace(
#     go.Bar(y=EU['EU_Sales'],
#            x=EU_games,
#            name="Europe",
#            marker={'color': EU['EU_Sales'],'colorscale': 'hot'},
#            ),row=1, col=2)
# fig_14.add_trace(
#     go.Bar(y=JP['JP_Sales'],
#            x=JP_games,
#            name="Japan",
#            marker={'color': JP['JP_Sales'],'colorscale': 'hot'},
#            ),row=2, col=1)

# fig_14.add_trace(
#     go.Bar(y=Other['Other_Sales'],
#            x=Other_games,
#            name="Other",
#            marker={'color': Other['Other_Sales'],'colorscale': 'hot'},
#            ),row=2, col=2)

# fig_14.show()

# %%
top_tdf = tdf.groupby(['Platform', 'Year']).agg({total_sales_column: 'count'}).reset_index()
top_tdf.columns = ['Platform', 'Year', 'Count']
top_tdf = top_tdf[top_tdf['Count'] > top_tdf['Count'].sum() * 0.01]
top_tdf['Year'] = top_tdf['Year'].astype(str)

# %%
fig_15 = px.bar(
    top_tdf,
    x='Platform',
    y='Count',
    color='Year',
    barmode="group",
    hover_name= 'Year'
)
fig_15.update_layout(title="Total released video-games by platform")
fig_15.update_xaxes(categoryorder='category ascending')

# %%
platform_tops = ['PS4', 'PSV', 'XOne', 'PC']

# %% [markdown]
# ## Sales Analysis

# %%
platform_tdf = tdf.groupby(['Platform', 'Year']).agg({total_sales_column: 'sum'}).reset_index()
platform_tdf = platform_tdf.sort_values('Year', ascending=True)
platform_tdf

# %% [markdown]
# ## aggregated sales analysis

# %%
platform_sum_tdf = platform_tdf.groupby(['Platform']).agg({total_sales_column: 'sum'}).reset_index()
platform_sum_tdf = platform_sum_tdf[platform_sum_tdf[total_sales_column] > platform_sum_tdf[total_sales_column].sum() * 0.03]
platform_sum_tdf

# %%
# all_time_fig = px.bar(
#     platform_sum_tdf,
#     x='Platform',
#     y=total_sales_column,
# )
# all_time_fig.update_layout(title="Total sales of all time in the most important platforms (Millions)")
# all_time_fig.update_xaxes(type='category')
# all_time_fig.update_xaxes(categoryorder='category ascending')
# all_time_fig.show()

# %%
platform_tmp_tdf = tdf.groupby(['Platform', 'Year']).agg({total_sales_column: ['sum', 'count']})


# %% [markdown]
# # Sales Distribution

# %%
if 'Total_Shipped' in data_df.columns:
    regions = ['NA', 'JP', 'PAL', 'Other']
else:
    regions = ['NA', 'JP', 'EU', 'Other']

region_sales_sufix = '_Sales'
regions_agg = {}

for region in regions:
    regions_agg[region + region_sales_sufix] = 'sum'

regions_agg[total_sales_column] = 'sum'
regions_agg

# %%
geo_tdf = tdf.groupby(['Year']).agg(regions_agg).reset_index()
geo_tdf = geo_tdf.sort_values('Year', ascending=True)
geo_tdf.head(10)

# %%
geo_tdf.head(1)

# %%
sales_region_figscatter = go.Figure()

for region in regions:
    
    sales_region_figscatter.add_trace(go.Scatter(
        x=geo_tdf['Year'], 
        y=geo_tdf[region + region_sales_sufix], 
        mode='lines',
        name=region,
    ))
sales_region_figscatter.update_layout(title="Total sales per year by region (Millions)")
sales_region_figscatter.update_xaxes(type='category')

# %%

year_geo_df = tdf[["Year",'NA_Sales','EU_Sales','JP_Sales','Other_Sales']]

year_geo_df[['NA_mean','EU_mean','JP_mean','Other_mean']] = year_geo_df.groupby('Year')[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].transform('sum')
year_geo_df = year_geo_df.drop(['NA_Sales','EU_Sales','JP_Sales','Other_Sales'], axis=1)
year_geo_df = year_geo_df.drop_duplicates()
year_geo_df = year_geo_df.sort_values("Year")

temp_df1 = pd.DataFrame({'Place': ['NA_Sales']*year_geo_df.shape[0], 'Year':year_geo_df['Year'], 'Sales': year_geo_df['NA_mean']})
temp_df2 = pd.DataFrame({'Place': ['EU_Sales']*year_geo_df.shape[0], 'Year': year_geo_df['Year'], 'Sales': year_geo_df['EU_mean']})
temp_df3 = pd.DataFrame({'Place': ['JP_Sales']*year_geo_df.shape[0], 'Year': year_geo_df['Year'], 'Sales': year_geo_df['JP_mean']})
temp_df4 = pd.DataFrame({'Place': ['Other_Sales']*year_geo_df.shape[0], 'Year': year_geo_df['Year'], 'Sales': year_geo_df['Other_mean']})

final = pd.concat([temp_df1,temp_df2,temp_df3,temp_df4], axis=0)
final = final.sort_values("Year")

distribution_region_fig=px.bar(
    final,
    x='Place', 
    y="Sales", 
    animation_frame="Year",
    animation_group="Place", 
    color="Place", 
    hover_name="Place",
    range_y=[0, 300]
)
distribution_region_fig.update_layout(title="Year sales distribution by region",title_x=0.5)


# %% [markdown]
# ## Distribution of sales by genre

# %%
genre_tdf = tdf.groupby(['Genre']).agg(regions_agg)
genre_tdf = genre_tdf.sort_values(total_sales_column, ascending=False)
genre_tdf.head()

# %%
# Reorder df to total genre scattewr plot
genre_total_tdf = genre_tdf.reset_index().sort_values(total_sales_column, ascending=False)

# %%
genre_tops = list(genre_total_tdf.loc[genre_total_tdf[total_sales_column] > genre_total_tdf[total_sales_column].sum() * 0.03, 'Genre'])
genre_tops

# %%
genre_tops_df = tdf[tdf['Genre'].isin(genre_tops)]

fig = px.pie(genre_tops_df,
             values=total_sales_column,
             names='Genre',
             title='Population of European continent',
             hover_data=['Genre'], 
             labels={'lifeExp':'Video Games Genres'},
             hole=0.3,
            )
fig.update_traces(textposition='inside', textinfo='percent+label')

# %%
pie_genre_fig  = go.Figure()
pie_genre_fig.add_trace(go.Pie(
    labels=genre_tops_df['Genre'], 
    values=genre_tops_df[total_sales_column], 
    pull=[0, 0, 0.1, 0.05, 0, 0, 0.05, 0, 0.05],
))
pie_genre_fig.update_traces(textposition='inside', textinfo='percent+label')
pie_genre_fig.update_layout(title="Percent of sales by Genre")

# %%
tdf = data_df.copy()
# tdf['Year'] = df['Year'].fillna(df['Year'].mean())
tdf = df[df['Year'].notna()] # Carefull about this
tdf = tdf.sort_values('Year', ascending=True)
tdf
if 'ESRB_Rating' in df.columns:
    esrb_tdf = tdf.groupby('ESRB_Rating').agg({total_sales_column: 'sum'}).reset_index()
    esrb_tdf.head(10)

# %%
# tdf = df.copy()
# # tdf['Year'] = df['Year'].fillna(df['Year'].mean())
# tdf = df[df['Year'].notna()] # Carefull about this
# tdf = tdf.sort_values('Year', ascending=True)
# tdf
# if 'ESRB_Rating' in df.columns:
#     esrb_tdf = tdf.groupby('ESRB_Rating').agg({total_sales_column: 'sum'}).reset_index()
#     esrb_tdf.head(10)

# %%
if 'ESRB_Rating' in data_df.columns:
    fig = px.bar(esrb_tdf, x='ESRB_Rating', y=total_sales_column)

# %% [markdown]
# ## Publisher analysis

# %%
df = pd.merge(data_df, region_df[['Developer', 'Country']], left_on='Publisher', right_on='Developer')
df

# %%
data_df

# %%
tdf = data_df
# tdf['Year'] = df['Year'].fillna(df['Year'].mean())
tdf = data_df[data_df['Year'].notna()] # Carefull about this
tdf = tdf.sort_values('Year', ascending=True)
tdf
if 'ESRB_Rating' in df.columns:
    esrb_tdf = tdf.groupby('ESRB_Rating').agg({total_sales_column: 'sum'}).reset_index()
    esrb_tdf.head(10)

# %%
data_genre = data_df.groupby(by=['Genre'])['Global_Sales'].sum()
data_genre = data_df.reset_index()
data_genre = data_df.sort_values(by=['Global_Sales'], ascending=False)
data_genre

# %%
# # Replace nana values in Country before groupby
# pub_tdf = tdf.copy()
# pub_tdf['Country'] = tdf['Country'].fillna(value='Unknown')

# # Groupby publisher and country
# pub_tdf = pub_tdf.groupby(['Publisher', 'Country']).agg({total_sales_column: ['sum', 'count']}).reset_index()
# pub_tdf.columns = ['Publisher', 'Country', 'Sales_Sum', 'Sales_Count']

# pub_tdf = pub_tdf[pub_tdf['Publisher'] != 'Unknown']

# pub_tdf.head()

# %%
# # Filter 5% over sales or 5% over games published
# pub_tdf = pub_tdf[(pub_tdf['Sales_Sum'] > pub_tdf['Sales_Sum'].sum() * 0.01) |
#                   (pub_tdf['Sales_Count'] > pub_tdf['Sales_Count'].sum() * 0.01)
#                  ]

# %% [markdown]
# # Publisher sales by year

# %%
top_publishers = [
    'Nintendo', 
    'Sony Computer Entertainment',
    'Microsoft Game Studios',
    'Konami Digital Entertainment',
    'Electronic Arts'
]

top_pub_tdf = tdf.loc[:,["Year","Publisher", total_sales_column]]
top_pub_tdf['total_sales'] = top_pub_tdf.groupby([top_pub_tdf.Publisher, top_pub_tdf.Year])[total_sales_column].transform('sum')
top_pub_tdf.drop(total_sales_column, axis=1, inplace=True)

top_pub_tdf = top_pub_tdf.drop_duplicates()
top_pub_tdf = top_pub_tdf[(top_pub_tdf['Year'] >= 2002)]
top_pub_tdf = top_pub_tdf.loc[top_pub_tdf['Publisher'].isin(top_publishers)]
top_pub_tdf = top_pub_tdf.sort_values("Year")

pubfig=px.bar(
    top_pub_tdf,
    x='Publisher', 
    y="total_sales", 
    animation_frame="Year", 
    animation_group="Publisher", 
    color="Publisher", 
    hover_name="Publisher",
    range_y=[0,250]
)
pubfig.update_layout(title_text="Top Publisher Game Sale by Year", xaxis_domain=[0.05, 1.0])


# %% [markdown]
# ## Publisher sales by region

# %%
tdf = df.copy
# tdf['Year'] = df['Year'].fillna(df['Year'].mean())
tdf = df[df['Year'].notna()] # Carefull about this
tdf = tdf.sort_values('Year', ascending=True)
tdf
if 'ESRB_Rating' in df.columns:
    esrb_tdf = tdf.groupby('ESRB_Rating').agg({total_sales_column: 'sum'}).reset_index()
    esrb_tdf.head(10)

# %%
# Replace nana values in Country before groupby
pub_tdf = tdf.copy()
pub_tdf['Country'] = tdf['Country'].fillna(value='Unknown')

# Groupby publisher and country
pub_tdf = pub_tdf.groupby(['Publisher', 'Country']).agg({total_sales_column: ['sum', 'count']}).reset_index()
pub_tdf.columns = ['Publisher', 'Country', 'Sales_Sum', 'Sales_Count']

pub_tdf = pub_tdf[pub_tdf['Publisher'] != 'Unknown']

pub_tdf.head()

# %%
# Filter 5% over sales or 5% over games published
pub_tdf = pub_tdf[(pub_tdf['Sales_Sum'] > pub_tdf['Sales_Sum'].sum() * 0.01) |
                  (pub_tdf['Sales_Count'] > pub_tdf['Sales_Count'].sum() * 0.01)
                 ]
tdf

# %%
# pub_tdf = pub_tdf.sort_values('Sales_Sum', ascending=False)
# pub_tdf.head()

# %%
publisher_tops = list(pub_tdf['Publisher'])
len(publisher_tops)

# %%
# fig_18.add_trace(scatter_populargenre_fig)
# fig_18.add_trace(box_sales_fig)
# fig_18.update_layout(
#     title_text="Top Platform Sales",
#     updatemenus=[
#         dict(
#             type="dropdown",
#             direction="down",
#             active=1,
#             x=0.8,
#             y=1.2,
#             buttons=list([
#                 dict(label="Top 5",
#                      method="update",
#                      args=[{"visible": [True, False]},
#                            {"title": "Top 5 Platforms Game Sales"}]),
#                 dict(label="Top 10",
#                      method="update",
#                      args=[{"visible": [False,True,]},
#                            {"title": "Top 10 Platforms Game Sales"}]),
#             ]),
#         )
#     ])


# %%
scatter_publisherregion_fig = px.scatter(
    pub_tdf,
    x='Publisher',
    y='Sales_Sum',
    size='Sales_Count',
    color='Country',
    hover_name = 'Publisher',
)
scatter_publisherregion_fig.update_xaxes(categoryorder='total descending')
scatter_publisherregion_fig.update_layout(title="Sales by publisher and region (Millions)")

# %%

EU = tdf.pivot_table('EU_Sales', columns='Publisher', aggfunc='sum').T
EU = EU.sort_values(by='EU_Sales', ascending=False).iloc[0:5]
EU_publishers = EU.index

JP = tdf.pivot_table('JP_Sales', columns='Publisher', aggfunc='sum').T
JP = JP.sort_values(by='JP_Sales', ascending=False).iloc[0:5]
JP_publishers = JP.index

NA = tdf.pivot_table('NA_Sales', columns='Publisher', aggfunc='sum').T
NA = NA.sort_values(by='NA_Sales', ascending=False).iloc[0:5]
NA_publishers = NA.index

Other = tdf.pivot_table('Other_Sales', columns='Publisher', aggfunc='sum').T
Other = Other.sort_values(by='Other_Sales', ascending=False).iloc[0:5]
Other_publishers = Other.index

Global = tdf.pivot_table('Global_Sales', columns='Publisher', aggfunc='sum').T
Global = Global.sort_values(by='Global_Sales', ascending=False).iloc[0:5]
Global_publishers = Global.index

# %%
# Initialize figure
bar_toppublishers_fig = go.Figure()

# Add Traces
bar_toppublishers_fig.add_trace(
    go.Bar(y=NA['NA_Sales'],
           x=NA_publishers,
           name="North America",
          marker={'color': NA['NA_Sales'],'colorscale': 'tealgrn'}))
bar_toppublishers_fig.add_trace(
    go.Bar(y=EU['EU_Sales'],
           x=EU_publishers,
           name="Europe",
           marker={'color': EU['EU_Sales'],'colorscale': 'tealgrn'},
           visible=False))
bar_toppublishers_fig.add_trace(
    go.Bar(y=JP['JP_Sales'],
           x=JP_publishers,
           name="Japan",
           marker={'color': JP['JP_Sales'],'colorscale': 'tealgrn'},
           visible=False))

bar_toppublishers_fig.add_trace(
    go.Bar(y=Other['Other_Sales'],
           x=Other_publishers,
           name="Others",
           marker={'color': Other['Other_Sales'],'colorscale': 'geyser'},
           visible=False))

bar_toppublishers_fig.add_trace(
    go.Bar(y=Global['Global_Sales'],
           x=Global_publishers,
           name="Global",
           marker={'color': Global['Global_Sales'],'colorscale': 'armyrose'},
               visible=False ))

buttons = []
countries = ['North America', 'Europe', 'Japan', 'Others', 'Global']
for i, country in enumerate(countries):
    buttons.append(dict(
        label=country,
        method="update",
        args=[{"visible": [False] * i + [True] + [False] * (3-i+1)},
              {"title": f"Top 5 Publishers for {country}"}]
    ))

bar_toppublishers_fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=0.57,
            y=1.2,
            buttons=buttons,
        )
    ])

# Set title
bar_toppublishers_fig.update_layout(
    title_text="Top 5 Publishers per region",
    xaxis_domain=[0.05, 1.0]
)


# %%
pub_genre_df = tdf.groupby(['Publisher', 'Genre']).agg(regions_agg).reset_index()
pub_genre_df = pub_genre_df[pub_genre_df['Publisher'].isin(publisher_tops)]
pub_genre_df = pub_genre_df[pub_genre_df['Genre'].isin(genre_tops)]
pub_genre_df.head()

# %%
scatter_populargenre_fig = px.scatter(
    pub_genre_df,
    x='Publisher',
    y=total_sales_column,
    color='Genre',
    hover_name = 'Publisher'
)
scatter_populargenre_fig.update_xaxes(categoryorder='total descending')
scatter_populargenre_fig.update_layout(title="Sales by publisher and genre (Millions)")

# %%
# Re-create the df to only select top 10 Publishers
pub_genre_df = tdf.groupby(['Publisher', 'Genre']).agg(regions_agg).reset_index()
pub_genre_df = pub_genre_df[pub_genre_df['Publisher'].isin(publisher_tops[:10])]
pub_genre_df = pub_genre_df[pub_genre_df['Genre'].isin(genre_tops)]
pub_genre_df.head()

pub_genre_pivot_df = pub_genre_df.pivot(index='Publisher', columns='Genre', values=total_sales_column)

z = pub_genre_pivot_df.values
x = pub_genre_pivot_df.columns.tolist()
y = pub_genre_pivot_df.index.tolist()

z_text = np.around(z)

# # Create heatmap
# publisherfig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale='viridis')
# publisherfig.update_xaxes(categoryorder='total descending')
# publisherfig.update_layout(title="Sales by publisher and genre (Millions)")
# publisherfig.show()

# %% [markdown]
# ## Lets evaluate competence

# %%
box_sales_fig = px.box(tdf[tdf['Genre'].isin(genre_tops)], 
             y=total_sales_column, 
             color='Genre',
             hover_name='Name',
            )
box_sales_fig.update_layout(title="Best Game Sells for each genre")

# %% [markdown]
# ## <p style="background-color:skyblue; font-family:newtimeroman; font-size:120%; text-align:center; border-radius: 15px 50px;">Sunburst platforms - genres - publishers</p>

# %%
# plat_genre_df = tdf[(tdf['Genre'].isin(genre_tops[:4])) & (tdf['Platform'].isin(platform_tops[:4]))]

# sunburst_platform_fig = px.sunburst(plat_genre_df, path=['Genre', 'Platform'], color = 'Genre' ,
#                                     template='ggplot2' , title="Top 5 Platforms for each genre" ,
#                                     values=total_sales_column)
# sunburst_platform_fig.show()

# %%
# genre_pub_df = tdf[(tdf['Genre'].isin(genre_tops[:4])) & (tdf['Publisher'].isin(publisher_tops[:5]))]

# sunburst_publisher_fig = px.sunburst(genre_pub_df, path=['Genre', 'Publisher'], values=total_sales_column , color = 'Genre' ,
#                                       template='ggplot2', title="Top 5 Publishers for each genre")
# sunburst_publisher_fig.show()

# %%
# plat_pub_df = tdf[(tdf['Platform'].isin(platform_tops[:4])) & (tdf['Publisher'].isin(publisher_tops[:5]))]

# sunburst_platpub_fig = px.sunburst(plat_pub_df, path=['Platform', 'Publisher'], values=total_sales_column , color = 'Platform' ,
#                                   template = 'ggplot2' , color_continuous_scale='tealgrn')
# sunburst_platpub_fig.update_layout(title="Top 5 Publishers for each Platform")
# sunburst_platpub_fig.show()

# %% [markdown]
# # All TOGETHER

# %%
# genre_pub_genre_df = tdf[(tdf['Genre'].isin(genre_tops[:4])) & 
#                          (tdf['Publisher'].isin(publisher_tops[:5])) & 
#                          (tdf['Platform'].isin(platform_tops[:4]))
#                         ]

# sunburst_all_fig = px.sunburst(genre_pub_genre_df, path=['Genre', 'Platform', 'Publisher'], values=total_sales_column ,
#                                template = 'ggplot2' ,color='Genre')
# sunburst_all_fig.update_layout(title="Top publishers & Platform for each genre")
# sunburst_all_fig.show()

# %% [markdown]
# ## Dashboard HTML

# %%
# https://dash.plotly.com/dash-core-components
#https://dash.plotly.com/dash-core-components/dropdown
import plotly.express as px
import pandas as pd

import dash_bootstrap_components as dbc


# %%
import base64

# Custom Style
NAVBAR_STYLE = {
    'height': "200px",
}

ROW_STYLE = {
    'height': "450px",
}

TITLE_STYLE={
    'height': '130px', 
    'flex':'0',
    'margin':'0 auto',
    'textAlign': 'center',
    'margin-bottom':'10px'
}




def drawFigure(figure=None, id=None, config={'displayModeBar': False, 'autosizable':True, 'responsive':True}):
    return dcc.Graph(
                    id=id,
                    figure=figure.update_layout(
                        template     = 'plotly_dark',
                        plot_bgcolor = 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        autosize=True,
                        margin=dict(l=20, r=20, t=40, b=20),
                    ),
                    config=config,
                    style={'background-color':'#205375', 'height':'100%'}
        #3d41a4
                )

def drawFigure2(figure=None, id=None, config={'displayModeBar': False, 'autosizable':True, 'responsive':True}):
    return dcc.Graph(
                    id=id,
                    figure=figure.update_layout(
                        template     = 'seaborn',
                        plot_bgcolor = 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        autosize=True,
                        margin=dict(l=20, r=20, t=40, b=20),
                    ),
                    config=config,
                    style={'background-color':'#205375', 'height':'100%'}
        #3d41a4
                )

# %%
app=Dash(__name__,external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css",dbc.themes.BOOTSTRAP])
server = app.server
server.static_folder="assets"

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([ 
            # ------------------------------------------ Bans Section  ------------------------------------------ #
            dbc.Row([
                dbc.Col([
                    html.Img(src='/assets/sony.png',width='50%', height='130px', style={'margin-bottom':'20px'}),
                    html.H1("Video Games Analysis", style={'font-size': '30px','color': '#00eaea'}),
                                    ], width=3, style={'text-align': 'center'}),
                #===========##===========##===========##===========##===========##===========##===========##===========##===========##===========#
               dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.H6("Games", style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' ,'font-size': '30px','color': 'white', 'font-family':'Sans-serif'}),
                            html.H1(len(games), id='gross', style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' , 'font-size': '45px','color': 'white'}),
                        ], width=3, style={"height": "180px", 'font-family': 'Cursive', "background-color": "#00c0c0", 'text-align':'center', 'justify':'center', 'align':'center', 'padding-top': '40px'}),

                        dbc.Col([
                            html.H6("Publishers", style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' ,'font-size': '30px','color': 'white', 'font-family':'Sans-serif'}),
                            html.H1(len(publisher), style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' ,'font-size': '45px','color': 'white'}),
                        ], width=3, style={"height": "180px", 'font-family': 'Cursive', "background-color": "#00aaaa", 'text-align':'center', 'justify':'center', 'align':'center', 'padding-top': '40px'}),
                        
                        dbc.Col([
                            html.H6("Platforms", style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' ,'font-size': '30px','color': 'white', 'font-family':'Sans-serif'}),
                            html.H1(len(platforms), style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' ,'font-size': '45px','color': 'white'}),
                        ], width=3, style={"height": "180px", 'font-family': 'Cursive', "background-color": "#009595",
                                           'text-align':'center', 'justify':'center', 'align':'center', 
                                           'padding-top': '40px'}),
                        dbc.Col([
                            html.H6("Genres", style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' ,'font-size': '30px','color': 'white', 'font-family':'Sans-serif'}),
                            html.H1(len(genres), style={'-webkit-text-stroke-width': '0.5px',
                                  '-webkit-text-stroke-color': 'black' ,'font-size': '45px','color': 'white'}),
                        ], width=3, style={"height": "180px", 'font-family': 'Cursive', "background-color": "#008080",
                                           'text-align':'center', 'justify':'center', 'align':'center', 
                                           'padding-top': '40px'}),
                        
                    ]),
                ], width=9),                
                
            ##=========================================================================#
#                
            ], align='center', style= NAVBAR_STYLE),

            html.Br(),
            # ------------------------------------------ Graph Section 1  ------------------------------------------ #
            dbc.Row([
                dbc.Col([ 
                      dcc.Dropdown(
                        ['Global Sales', 'Count Games'],
                        id= 'drop-down-bar',
                        value= 'Count Games',
                        multi = False,
                        placeholder='Choose value' ,style = {'width' : '100%' , 'color': '#03369c' , 
                                                                'font-size' : '14px','font-family' : 'Monospace'}),
                    dcc.Graph(id='bar_graph' , )
                ], width=6,  style={"height": "100%" , }),
                #===========##===========##===========##===========##===========#
                
                
                dbc.Col([
                          dcc.Dropdown(
                        ['Global Sales', 'Count Games'],
                        id= 'drop-down-pie',
                        value= 'Count Games',
                        multi = False,
                        placeholder='Choose a value' , style = {'width' : '100%' , 'color': '#03369c' , 
                                                                'font-size' : '14px','font-family' : 'Monospace'}),
                    dcc.Graph(id='pie_graph' , )   
                ], width=6,  style={"height": "100%"}),
            ], align='center', style={'height' : '100%'}),
            html.Br(),
            html.Br(),
            html.Br(),

            # ------------------------------------------ Graph Section 2  ------------------------------------------ #
            dbc.Row([

                #===========##===========##===========##===========##===========#
            dbc.Col([ 
                  dcc.Dropdown(
                        ['Top Publishers', 'Top Platforms' , 'Top Publishers Vs Platform' , 'All Figures'],
                        id= 'drop-down-sun',
                        value= 'Top Publishers',
                        multi = False,
                        placeholder='Choose a value' , style = {'width' : '100%' , 'color': '#03369c' , 
                                                                'font-size' : '14px','font-family' : 'Monospace'}),
                    dcc.Graph(id='sun_graph' ,  )

                ], width=6,  style={"height": "100%"}),
              #===========##===========##===========##===========##===========#
                dbc.Col([
                     dcc.Dropdown(
                        ['Developers', 'Game Studios'],
                        id= 'drop-down-world',
                        value= 'Game Studios',
                        multi = False,
                        placeholder='Choose the value' , style = {'width' : '100%' , 'color': '#03369c' , 
                                                                'font-size' : '14px','font-family' : 'Monospace'}),
                    dcc.Graph(id='world_graph' , )
                 ], width=6,  style={"height": "100%"}),
            ], align='center', style={'height' : '150%'}),
            
            html.Br(),
                     # ------------------------------------------ Graph Section 3  ------------------------------------------ #   
            dbc.Row([

                 dbc.Col([
                    drawFigure(id='scatter_publisherregion_fig' ,figure=scatter_publisherregion_fig)
                ], width=6,  style={"height": "100%" , 'position' : 'center'}),
                
                dbc.Col([
                    drawFigure(id='pubfig' ,figure=pubfig)
                ], width=6,  style={"height": "100%" , 'position' : 'center'}),
                 ], align='center', style=ROW_STYLE),
            html.Br(),
                            # ------------------------------------------ Graph Section 4  ------------------------------------------ #
            dbc.Row([
                 dbc.Col([
                    drawFigure(id='fig_15' ,figure=fig_15)
                ], width=12,  style={"height": "100%" , 'position' : 'center'}),
            
                #===========##===========##===========##===========##===========#
               ], align='center', style={'height' : '150%'}),

            html.Br(),   
            
              # ------------------------------------------ Graph Section 5 ------------------------------------------ #
            dbc.Row([
               dbc.Col([ 
                drawFigure(id='fig_14', figure=fig_14)   
                ], width=6,style={"height": "50%" , 'position' : 'center'}  ),

                
                dbc.Col([
                    drawFigure(id='fig_8' ,figure=fig_8)
                ], width=6,  style={"height": "50%" , 'position' : 'center'}),

                #===========##===========##===========##===========##===========#
                            #===========##===========##===========##===========##===========#
               ], align='center', style={'height' : '150%'}),

            html.Br(),  
            html.Br(),  
                      # ------------------------------------------ Graph Section 6  ------------------------------------------ #
            dbc.Row([
               dbc.Col([
                          dcc.Dropdown(
                        ['Best Games Sales', 'Best Publisher Sales'],
                        id= 'drop-down-boxplot',
                        value= 'Best Games Sales',
                        multi = False,
                        placeholder='Choose a graph' , style = {'width' : '100%' , 'color': '#03369c' , 
                                                                'font-size' : '14px','font-family' : 'Monospace'}),
                    dcc.Graph(id='boxplot_graph' , )   
                ], width=6,  style={"height": "100%" ,'width' : '50%'}),
                
                
                dbc.Col([ dcc.Dropdown(
                        ['Regional Sales for each genre', 'Regional Sales per year'],
                        id= 'drop-down-regional',
                        value= 'Regional Sales for each genre',
                        multi = False,
                        placeholder='Choose a graph' , style = {'width' : '100%' , 'color': '#03369c' , 
                                                                'font-size' : '14px','font-family' : 'Monospace'}),
                    dcc.Graph(id='regional_graph' , )   
                ], width=6,  style={"height": "100%" , 'position' : 'center'}),

                #===========##===========##===========##===========##===========#
                            #===========##===========##===========##===========##===========#
               ], align='center', style={'height'  : '100%'}),

            html.Br(),
            html.Br(),
            
            # ------------------------------------------ Graph Section 7  ------------------------------------------ #
            dbc.Row([
               dbc.Col([
                drawFigure(id='fig_20' ,figure=fig_20)
                ], width=6,  style={"height": "100%" , 'position' : 'center'}),

                dbc.Col([
                   drawFigure(id = 'fig_5' , figure= fig_5)
                ], width=6,),

                #===========##===========##===========##===========##===========#
                            #===========##===========##===========##===========##===========#
               ], align='center', style={'height'  : '150%'}),

            html.Br(),   
            html.Br(),
            html.Br(),
            html.Br(),   
            
        
            # ------------------------------------------ Graph Section 8  ------------------------------------------ #
              dbc.Row([

                 dbc.Col([
                    drawFigure(id='fig_11' ,figure=fig_11)
                ], width=12, style={"height": "100%" , 'position' : 'center'}),
                #===========##===========##===========##===========##===========#
               ], align='start', style=ROW_STYLE),
            html.Br(),
            html.Br(),
                #===========##===========##===========##===========##===========#
#             # ------------------------------------------ About Section   ------------------------------------------ #
#             dbc.Row([
#                 dbc.Col([
#                 ], width=4,  style={"height": "100%", }),
#                 dbc.Col([
                    
#                     html.H4("This Dashboard is made by", style={'font-size': '30px','color': 'yellow', 'font-family':'Sans-serif'}),
#                 ], width=4,  style={"height": "150px", 'font-family': 'Cursive', 'text-align':'center', 
#                                     'justify':'center', 'align':'center', 'padding-top': '40px'}),
                
#                 dbc.Col([
#                 ], width=4,  style={"height": "100%", }),
                
#                 #===========##===========##===========##===========##===========#
#             ], align='center',  style={"height": "200px"}),
#             dbc.Row([
#                 dbc.Col([
#                 ], width=2,  style={"height": "100%", }),
#                 dbc.Col([
#                     html.A(['Mohamed Ibrahem'], href='https://www.linkedin.com/in/mohamed-ibrahemm/',target='_blank', 
#                            style={'font-size': '20px','color': 'white', 'font-family':'Sans-serif'}),
               
#                 ], width=4,  style={"height": "100%", }),
#                 dbc.Col([
#                     html.A(['Tareq Refaat'], href='https://www.facebook.com/tariq.ghoorab',target='_blank', 
#                            style={'font-size': '20px','color': 'white', 'font-family':'Sans-serif'}),
                
#                 ], width=4,  style={"height": "100%", }),
#                 #===========##===========##===========##===========##===========#
#             ], align='center',  style={"height": "130px"}),
            
          
         ]), color = '#112B3C' 
                #20447d
            ) 
] )

# %%
@app.callback(
    Output(component_id='bar_graph', component_property='figure'),
    Input(component_id='drop-down-bar', component_property='value')
)
def update_bar_graph(dropdownvalue):

   

    if dropdownvalue == 'Global Sales':
        # Video Game Sales by Year
        yearwisesale =  df.groupby('Year')['Global_Sales'].sum().reset_index()
        # Yearwise Total Game Sales
        fig = go.Figure(go.Bar(x=yearwisesale['Year'],y=yearwisesale['Global_Sales'],
                               marker={'color': yearwisesale['Global_Sales'],'colorscale': 'tealgrn'}))
        fig.update_layout(title_text='Video-Games Global Sales by Year',xaxis_title="Year",yaxis_title="Sum of Sales")
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    elif dropdownvalue == 'Count Games':
           # Yearwise Total Game Published
        yearwisegame =  df.groupby('Year')['Name'].count().reset_index()
        fig = go.Figure(go.Bar(x=yearwisegame['Year'],y=yearwisegame['Name'],
                               marker={'color': yearwisegame['Name'],'colorscale': 'tealgrn'}))
        fig.update_layout(title_text='Video-Games Released Count by Year',xaxis_title="Year",yaxis_title="Number of Games Released")
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    return fig

@app.callback(
    Output(component_id='world_graph', component_property='figure'),
    Input(component_id='drop-down-world', component_property='value')
)
def update_bar_graph(dropdowncompany):
    fig= px.choropleth(df_country, locations="country_code",
                    projection='natural earth',
                    color="Count", 
                    hover_data = ['Country' , 'Count'],
                    hover_name = 'Count',
                    color_continuous_scale=px.colors.sequential.Viridis_r ,title = 'Number of Game Studios around the world'  , template = 'plotly_dark')
    fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                      font=dict(
                          
    family="sans-serif",
    size=14,
    color="beige"
    ))
    
    if dropdowncompany == 'Game Studios':
        fig = px.choropleth(df_country, locations="country_code",
                    color="Count", 
                    projection='natural earth',
                    hover_data = ['Country' , 'Count'],
                    hover_name = 'Count',
                    color_continuous_scale=px.colors.sequential.Viridis_r ,title = 'Number of Game Studios around the world' ,
                   )
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' ,
                  font=dict(
                            family="sans-serif",
                            size=14,
                            color="beige"
                            ))
        fig.update_geos(

        bgcolor="#205375",
        resolution=50,
        showcoastlines=True, coastlinecolor="#205375",
        showocean=True, oceancolor="#205375",
        showlakes=True, lakecolor="#205375",
        showrivers=False, rivercolor="#205375"
        )
        fig.update_traces(marker_line_width=0)
        
    elif dropdowncompany == 'Developers':
        fig = px.choropleth(region_country, locations="country_code",
                    projection='natural earth',
                    color="count", 
                    hover_name = 'count',
                    color_continuous_scale=px.colors.sequential.Viridis_r ,title = 'Number of Developers around the world')
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
                    ))
        fig.update_geos(

        bgcolor="#205375",
        resolution=50,
        showcoastlines=True, coastlinecolor="#205375",
        showocean=True, oceancolor="#205375",
        showlakes=True, lakecolor="#205375",
        showrivers=False, rivercolor="#205375"
        )
        fig.update_traces(marker_line_width=0)
        
    return fig





@app.callback(
    Output(component_id='pie_graph', component_property='figure'),
    Input(component_id='drop-down-pie', component_property='value')
)
def update_piegraph(dropdownpie):

    if dropdownpie == 'Global Sales':
        genre = df.loc[:,['Genre','Global_Sales']]
        genre['total_sales'] = genre.groupby('Genre')['Global_Sales'].transform('sum')
        genre.drop('Global_Sales', axis=1, inplace=True)
        genre = genre.drop_duplicates()

        fig = px.pie(genre, names='Genre', values='total_sales' , template='seaborn')
        fig.update_traces(rotation=90, pull=[0.2,0.06,0.06,0.06,0.06])
        fig.update_layout(title="Each Genre's Game Sales",title_x=0.5)
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    elif dropdownpie == 'Count Games':
    # Yearwise Total Game Published
        genre_wise_game =  df.groupby('Genre')['Name'].count().reset_index().sort_values("Name",ascending=False)
        genre_wise_game = genre_wise_game.reset_index()
        genre_wise_game.drop("index",axis = 1,inplace=True)
        
        fig = px.pie(genre_wise_game , names='Genre', 
                            values='Name',
                            hole=0.3 , template='seaborn') 
        
        fig.update_traces(hoverinfo='label+percent+value', 
                      textinfo='percent', 
                      textfont_size=15)
        fig.update_traces(rotation=90, pull=[0.2,0.06,0.06,0.06,0.06])
        fig.update_layout(title="Genre Game Released Count",title_x=0.5)
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    return fig

@app.callback(
    Output(component_id='sun_graph', component_property='figure'),
    Input(component_id='drop-down-sun', component_property='value')
)
def update_sungraph(dropdownsun):
    if dropdownsun == 'Top Platforms':
        plat_genre_df = tdf[(tdf['Genre'].isin(genre_tops[:4])) & (tdf['Platform'].isin(platform_tops[:4]))]

        fig = px.sunburst(plat_genre_df, path=['Genre', 'Platform'], color = 'Genre' ,
                                    color_continuous_scale='virvids' , title="Top 5 Platforms for each genre" ,
                                    values=total_sales_column , template = 'seaborn' )   
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
          font=dict(
        family="sans-serif",
        size=14,
        color="beige"))
    elif dropdownsun == 'Top Publishers':
        genre_pub_df = tdf[(tdf['Genre'].isin(genre_tops[:4])) & (tdf['Publisher'].isin(publisher_tops[:5]))]

        fig = px.sunburst(genre_pub_df, path=['Genre', 'Publisher'], values=total_sales_column , 
                                             color = 'Genre' ,  template = 'seaborn' 
                                             , title="Top 5 Publishers for each genre")
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))

        
    elif dropdownsun == 'Top Publishers Vs Platform':
        plat_pub_df = tdf[(tdf['Platform'].isin(platform_tops[:4])) & (tdf['Publisher'].isin(publisher_tops[:5]))]

        fig = px.sunburst(plat_pub_df, path=['Platform', 'Publisher'], values=total_sales_column ,
                                           color = 'Platform' , template = 'seaborn' )
        fig.update_layout(title="Top 5 Publishers for each Platform")
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    elif dropdownsun == 'All Figures':
        genre_pub_genre_df = tdf[(tdf['Genre'].isin(genre_tops[:4])) & 
                                 (tdf['Publisher'].isin(publisher_tops[:5])) & 
                                 (tdf['Platform'].isin(platform_tops[:4]))
                                ]
        fig = px.sunburst(genre_pub_genre_df, path=['Genre', 'Platform', 'Publisher'], values=total_sales_column
                        , color = 'Genre' , template = 'seaborn' )
        fig.update_layout(title="Top publishers & Platform for each genre")
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    return fig

@app.callback(
    Output(component_id='boxplot_graph', component_property='figure'),
    Input(component_id='drop-down-boxplot', component_property='value')
)
def update_bar_graph(dropdownboxplot):

   

    if dropdownboxplot == 'Best Games Sales':
        fig = px.box(tdf[tdf['Genre'].isin(genre_tops)], 
                     y=total_sales_column, 
                     color='Genre',
                     hover_name='Name',
                    )
        fig.update_layout(title="Best Game Sales for each genre")
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    elif dropdownboxplot == 'Best Publisher Sales':
        fig = px.scatter(
            pub_genre_df,
            x='Publisher',
            y=total_sales_column,
            color='Genre',
            hover_name = 'Publisher'
        )
        fig.update_xaxes(categoryorder='total descending')
        fig.update_layout(title="Game Sales by publisher for each genre (Millions)")
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    return fig

@app.callback(
    Output(component_id='regional_graph', component_property='figure'),
    Input(component_id='drop-down-regional', component_property='value')
)
def update_bar_graph(dropdownvalue):

    if dropdownvalue == 'Regional Sales for each genre':
        fig = go.Figure()
        fig.add_trace(go.Bar(x=na_sales,
                 y=genre_s,
                 name='North America Sales',
                 marker_color='#83e6ab',
                 orientation='h'))
        fig.add_trace(go.Bar(x=eu_sales,
                 y=genre_s,
                 name='Europe Sales',
                 marker_color='#42bda3',
                 orientation='h'))
        fig.add_trace(go.Bar(x=jp_sales,
                 y=genre_s,
                 name='Japan Sales',
                 marker_color='#33a7a2',
                 orientation='h'))
        fig.add_trace(go.Bar(x=other_sales,
                 y=genre_s,
                 name='Other Region Sales',
                 marker_color='#257d98',
                 orientation='h'))
        fig.update_layout(title_text='Regional Wise Game Sales by Genre',xaxis_title="Sales in $M",yaxis_title="Genre",
              barmode='stack')
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    elif dropdownvalue == 'Regional Sales per year':
        fig = go.Figure()
        for region in regions:

            fig.add_trace(go.Scatter(
            x=geo_tdf['Year'], 
            y=geo_tdf[region + region_sales_sufix], 
            mode='lines',
            name=region,
            ))
        fig.update_layout(title="Total sales per year by region (Millions)")
        fig.update_xaxes(type='category')
        fig.update_layout(paper_bgcolor="#205375" , plot_bgcolor = '#205375' , 
                          font=dict(
        family="sans-serif",
        size=14,
        color="beige"
    ))
    return fig



# %%
if __name__ == '__main__':
    app.run_server(debug=True)