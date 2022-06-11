from dash import Input, Output, State
from server import app, User
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash
import time

@app.callback(
    Output("url-login", "pathname"),
    [Input("login-button", "n_clicks")],
    [State("input-username","value"),State("input-password","value")]
)
def check_login(n_clicks, username, password):
    user = User.query.filter_by(username=username).first()
    if n_clicks == 0:
        return "/"
    elif user:
        if check_password_hash(user.password, password):
           login_user(user) 
           return "/home"
        else:
            pass
    else:
        pass

@app.callback(
    Output("modal-unauthenticated", "is_open"),
    Input("login-button", "n_clicks"), 
    Input("close-modal-unauthenticated", "n_clicks"),
    State("modal-unauthenticated", "is_open")
)
def toggle_modal(button_login, button_close, is_open):
    time.sleep(1)
    if current_user.is_authenticated:
        return False
    if button_login or button_close:
        return not is_open
    return is_open