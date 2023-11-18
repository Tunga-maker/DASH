import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Step 2: Load Data
df = pd.read_csv(r'C:\Users\Augustine\Desktop\Data Files\ZAPPS\Digit Pref\Birthweights.csv')
# Step 3: Data Transformation (if needed)

# Step 4: Create Dash App
app = dash.Dash(__name__)

# Calculate count of rounded birthweights by staff and status for Baby A and Baby B
rounded_counts_A = df.groupby(['Staff', 'BabyA_Rounding', 'BabyA_Status']).size().reset_index(name='Count')
rounded_counts_B = df.groupby(['Staff', 'BabyB_Rounding', 'BabyB_Status']).size().reset_index(name='Count')

# Define layout with additional styling
app.layout = html.Div(children=[
    html.H1(children='Baby Weight Dashboard', style={'textAlign': 'center', 'color': '#2e3d49', 'padding': '20px', 'backgroundColor': '#f0f8ff'}),


    

    dcc.Tab(label='Baby A', value='babyA', children=[
        dcc.Graph(
            id='rounded-birthweights-chart-A',
            figure=px.bar(rounded_counts_A, x='Staff', y='Count', color='BabyA_Rounding',
                          facet_col='BabyA_Status',
                          labels={'Count': 'Total Number of Birthweights'},
                          title='Total Number for Baby A',
                          template='plotly_dark')
        ),

        dcc.Graph(
            id='source-babyA-pie-chart',
            figure=px.pie(df, names='Source_BabyA', title='Distribution of Source for Baby A',
                          template='plotly_dark')
        ),
    ]),

    dcc.Tab(label='Baby B', value='babyB', children=[
        dcc.Graph(
            id='rounded-birthweights-chart-B',
            figure=px.bar(rounded_counts_B, x='Staff', y='Count', color='BabyB_Rounding',
                          facet_col='BabyB_Status',
                          labels={'Count': ' Total Number of Birthweights '},
                          title='Total Number for Baby B',
                          template='plotly_dark')
        ),

        dcc.Graph(
            id='source-babyB-pie-chart',
            figure=px.pie(df, names='Source_BabyB', title='Distribution of Source for Baby B',
                          template='plotly_dark')
        ),
    ]),
], style={'width': '100%', 'height': '100vh', 'max-width': '1200px', 'margin': 'auto'})

# Step 5: Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
