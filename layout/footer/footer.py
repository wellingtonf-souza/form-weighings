from dash import html

leaf = "assets/img/hydroponic.png"
footer = html.Div(
    className = 'rodape-login',
    children = [
        html.Footer(
            children = [
                html.Div(
                    children = [
                        html.Span("© 2021-2022 ITI MBA UFSCar. Todos os direitos reservados.")
                    ], style={'padding': 10, 'flex': 3}
                ),
                html.Div(
                    children = [
                        html.Span("Desenvolvido pelo Grupo 5"),
                        html.Img(src=leaf, style = {'padding-left': '5%'})
                    ],
                    style={'padding': 10, 'flex': 1, 'text-align': 'right'}
                )
            ],style = {'display': 'flex', 'flex-direction': 'row'})
    ]
)