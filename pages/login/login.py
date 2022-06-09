import dash_bootstrap_components as dbc
from dash import html, dcc
from components import get_button_submit

username = html.Div([
        dbc.Label("Usuário", html_for="input-username"),
        dbc.Input(type="text", id="input-username", placeholder="Digite o user"),
    ],
    className="mb-3",
)

password = html.Div([
        dbc.Label("Senha", html_for="input-password"),
        dbc.Input(
            type="password",
            id="input-password",
            placeholder="Digite a senha",
        ),
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
    is_open=False
)

layout = html.Div(
    children = [
        dcc.Location(id='url-login', refresh=True),
        dbc.Form(
            children = [
                html.Div(children = [
                    username, 
                    password, 
                    get_button_submit(_id = 'login-button', text = "ENTRAR")
                ], style = {'padding':'50px'})
            ], className = 'form-login'
        ),
        modal
    ], 
    className = 'back-login'
)