import dash_bootstrap_components as dbc
from dash import html

error = "assets/img/error.png"

layout = html.Div(
    children = [
        html.Div(
            children = [
                html.H2("Página não encontrada"),
                html.P("A página que você procura mudou de endereço ou não existe mais."),
                html.P("Verifique também se você digitou o endereço corretamente."),
            ]  
        ),
        html.Div(
            children = [html.Img(src = error, style = {'height': '10em'})],
            style = {"margin-left": "10em"}
        )
    ],
    className = 'content-blocks'
)