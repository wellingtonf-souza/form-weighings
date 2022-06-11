import dash_bootstrap_components as dbc

def get_col(label, _id = 'id', _type = 'number', width = 4, placeholder = ''):
    return dbc.Col(
        children = [
            dbc.Label(label, html_for=_id),
            dbc.Input(
                type=_type,
                id=_id,
                placeholder=placeholder,
            ),
        ],
        width=width,
        style = {'margin-top': '10px','margin-bottom': '10px'}
        )