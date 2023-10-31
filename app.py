import sys
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

if len(sys.argv) < 2:
    print("Usage: python script_name.py input.csv")
    sys.exit(1)

input_csv = sys.argv[1]

# Load CSV data into a DataFrame
df = pd.read_csv(input_csv)

def generate_sankey_figure(selected_role, selected_user, selected_object_type):
    if selected_role:
        filtered_df = df[df['RoleDefinitionName'] == selected_role]
    elif selected_user:
        filtered_df = df[df['DisplayName'] == selected_user]
    elif selected_object_type:
        filtered_df = df[df['ObjectType'] == selected_object_type]
    else:
        filtered_df = df.copy()

    filtered_df['Scope'] = filtered_df['Scope'].str.replace(r'^/subscriptions/[^/]+/', '', regex=True)

    nodes_role = filtered_df['RoleDefinitionName'].unique().tolist()
    nodes_display_signin = filtered_df.apply(lambda row: f"{row['DisplayName']} ({row['SignInName']})", axis=1).unique().tolist()
    nodes_scope = filtered_df['Scope'].unique().tolist()

    node_indices = {node: index for index, node in enumerate(nodes_role + nodes_display_signin + nodes_scope)}

    source_indices_role = filtered_df['RoleDefinitionName'].apply(lambda x: node_indices[x])
    source_indices_display_signin = filtered_df.apply(lambda row: node_indices[f"{row['DisplayName']} ({row['SignInName']})"], axis=1)
    source_indices_scope = filtered_df['Scope'].apply(lambda x: node_indices[x])
    values = [1] * len(filtered_df)

    link_sources = source_indices_role.tolist() + source_indices_display_signin.tolist()
    link_targets = source_indices_display_signin.tolist() + source_indices_scope.tolist()
    link_values = values + values

    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes_role + nodes_display_signin + nodes_scope
        ),
        link=dict(
            source=link_sources,
            target=link_targets,
            value=link_values
        )
    ))

    fig.update_layout(title_text="Azure IAM Relationships")

    return fig

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Select a Role"),
                dbc.CardBody(
                    dcc.Dropdown(
                        id='role-dropdown',
                        options=[{'label': role, 'value': role} for role in df['RoleDefinitionName'].unique()],
                        value=None,
                        placeholder="Select a role",
                        className="mb-3",
                        style={'color': 'black'}
                    )
                )
            ]),
            width=4
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Select a User"),
                dbc.CardBody(
                    dcc.Dropdown(
                        id='user-dropdown',
                        options=[{'label': user, 'value': user} for user in df['DisplayName'].unique()],
                        value=None,
                        placeholder="Select a user",
                        className="mb-3",
                        style={'color': 'black'}
                    )
                )
            ]),
            width=4
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Select an Object Type"),
                dbc.CardBody(
                    dcc.Dropdown(
                        id='object-type-dropdown',
                        options=[{'label': obj_type, 'value': obj_type} for obj_type in df['ObjectType'].unique()],
                        value=None,
                        placeholder="Select an object type",
                        className="mb-3",
                        style={'color': 'black'}
                    )
                )
            ]),
            width=4
        )
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='sankey-graph', style={'height': 'calc(100vh - 200px)'}))
    ], style={'margin': 0, 'padding': 0})  # Remove any unwanted margin and padding
], fluid=True)

@app.callback(
    Output('sankey-graph', 'figure'),
    Input('role-dropdown', 'value'),
    Input('user-dropdown', 'value'),
    Input('object-type-dropdown', 'value')
)
def update_sankey(selected_role, selected_user, selected_object_type):
    return generate_sankey_figure(selected_role, selected_user, selected_object_type)

if __name__ == '__main__':
    app.run_server(debug=True)
