from tkinter import TRUE
from dash import html, dcc
from layout import footer
from server import app, server
from utils import urls
from environment import APP_HOST, USER, PASSWORD
from dash import Input, Output, html
from flask_login import current_user
from users import Database

CONTENT_STYLE = {
    "margin-left": "13rem"
}

app.layout = html.Div(
    id="page-content",
    children = [
        dcc.Location(id="url", refresh = False)
    ]
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"))
def render_page(pathname):
    if pathname == '/':
        return html.Div(
            children = [
                urls.get(pathname).layout,
                footer
            ]
        )
    elif pathname not in urls:
        return html.Div(
            children = [
                urls.get('/404').layout,
                footer
            ]
        )
    elif pathname in urls and current_user.is_authenticated:
        return html.Div(
            children = [
                    urls.get(pathname).layout,
                    footer
            ]
        )
    else:
        return html.Div(
            children = [
                urls.get("/").layout,
                footer
        ]
    )

if __name__=='__main__':
    Database(user = USER, password = PASSWORD).start()
    server.run(
        host=APP_HOST,
        port=8085,
        debug=True
    ) 