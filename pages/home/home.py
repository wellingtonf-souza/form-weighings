import dash_bootstrap_components as dbc
from dash import html, dcc
from components import get_button_submit

plant_id = html.Div([
        dbc.Label("plant_id", html_for="input-plant_id"),
        dbc.Input(type="number", id="input-plant_id", placeholder="Digite o identificador da planta"),
    ],
    className="mb-3",
)

weight = html.Div([
        dbc.Label("Peso", html_for="input-weight"),
        dbc.Input(type="number",id="input-weight",placeholder="Digite o peso em gramas da planta"),
    ],
    className="mb-3",
)

modal = dbc.Modal([
    dbc.ModalBody(children = [
        html.Img(src = "assets/img/icons8-erro-96.png"),
        html.Br(),
        html.H3("Oops..."),
        html.Span("Usuário e/ou senha incorretos")
    ]),
    dbc.ModalFooter(
        get_button_submit(_id = "close-modal-unauthenticated", text="CLOSE")
    )],
    id="modal-unauthenticated",
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
                    get_button_submit(_id = 'login-button', text = "ENTRAR")
                ], style = {'padding':'50px'})
            ], className = 'form-login'
        ),
        modal
    ], 
    className = 'back-login'
)