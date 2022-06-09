from dash import html

def get_button_submit(_id, text):
    return html.Button(
        id=_id,
        children = text,
        n_clicks = 0,
        type='submit',
        className="bt-submit"
    )