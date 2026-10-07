import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

launch_sites = sorted(spacex_df['Launch Site'].unique())
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [{'label': site, 'value': site} for site in launch_sites]

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    dcc.Dropdown(id='site-dropdown',
                 options=site_options,
                 value='ALL',
                 placeholder='Select a Launch Site here',
                 searchable=True),
    html.Br(),

    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),

    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df[spacex_df['class'] == 1],
                     names='Launch Site',
                     title='Total Successful Launches by Site')
    else:
        site_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        outcome_counts = site_df['class'].value_counts().rename(index={1: 'Success', 0: 'Failure'}).reset_index()
        outcome_counts.columns = ['Outcome', 'Count']
        fig = px.pie(outcome_counts,
                     values='Count',
                     names='Outcome',
                     color='Outcome',
                     color_discrete_map={'Success': '#2ca02c', 'Failure': '#d62728'},
                     title='Total Success vs. Failure Launches for site ' + entered_site)
    return fig


@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    if entered_site == 'ALL':
        title = 'Correlation between Payload and Success for All Sites'
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        title = 'Correlation between Payload and Success for site ' + entered_site
    fig = px.scatter(filtered_df,
                     x='Payload Mass (kg)',
                     y='class',
                     color='Booster Version Category',
                     title=title)
    return fig


if __name__ == '__main__':
    app.run()
