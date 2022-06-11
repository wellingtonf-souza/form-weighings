from dash import Input, Output, State, html
from server import app
import time
from pages.home.aws import Dynamodb

bad_request = [
    html.Img(src = "assets/img/icons8-erro-96.png"),
    html.Br(),
    html.H3("Oops..."),
    html.Span("Formato de dados incorreto")
]

success = [
    html.Img(src = "assets/img/icons8-check-64.png"),
    html.Br(),
    html.H3("Ok"),
    html.Span("Dados enviados corretamente")
]

interval_error = [
    html.Img(src = "assets/img/icons8-erro-96.png"),
    html.Br(),
    html.H3("Oops..."),
    html.Span("Ocorreu algum erro inesperado no envio dos dados")
]

@app.callback(
    Output("modal-result", "is_open"),
    Output("message-modal", "children"),
    Input("button-input", "n_clicks"), 
    Input("close-modal-result", "n_clicks"),
    [State("modal-result", "is_open"),
    State("input-plant-id","value"),
    State("input-weight","value")]
)
def toggle_modal(button_input, button_close, is_open, plant_id, weight):
    time.sleep(1)
    if plant_id is None and weight is None and not is_open:
        return False, None
    elif type(plant_id) != int or type(weight) != int:
        return not is_open, bad_request
    elif type(plant_id) == int and type(weight) == int:
        status_code = Dynamodb().send(plant_id = plant_id, weight = weight)
        if status_code == 200:
            return not is_open, success
        else: 
            return not is_open, interval_error 
    elif button_input or button_close:
        return not is_open, None