import dash_bootstrap_components as dbc
from dash import html, dcc
from components import get_button_submit

plant_id = html.Div([
        dbc.Label("ID", html_for="input-plant-id"),
        dbc.Input(
            type="number", 
            id="input-plant-id", 
            placeholder="Digite o identificador da planta"
        ),
    ],
    className="mb-3",
)

weight = html.Div([
        dbc.Label("Peso", html_for="input-weight"),
        dbc.Input(
            type="number",
            id="input-weight",
            placeholder="Digite o peso em gramas da planta"
        ),
    ],
    className="mb-3",
)

modal = dbc.Modal([
    dbc.ModalBody(id = 'message-modal'),
    dbc.ModalFooter(
        get_button_submit(_id = "close-modal-result", text="FECHAR")
    )],
    id="modal-result",
    is_open=False,
)

layout = html.Div(
    children = [
        dcc.Location(id='url-login', refresh=True),
        dbc.Form(
            children = [
                html.Div(children = [
                    plant_id, 
                    weight, 
                    get_button_submit(_id = 'button-input', text = "ENVIAR")
                ], style = {'padding':'50px'})
            ], className = 'form-login'
        ),
        modal
    ], 
    className = 'back-login'
)