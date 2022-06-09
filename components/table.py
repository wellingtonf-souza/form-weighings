from dash import dash_table, html

def get_table(
    _id,
    data,
    page_size = 50,
    virtualization = False,
    fixed_rows = True,
    height_table = 500,
    skip_line = False,
    all_border = False
    ):
    style_table = {
        'height': f'{height_table}px', 
        'overflowY': 'auto',
        'borderCollapse': 'collapse'
    }
    style_header = {'textAlign':'left'}
    style_cell = {'textAlign':'left', 'lineHeight': '15px'}
    if fixed_rows:
        style_cell.update({'minWidth': 95, 'maxWidth': 95, 'width': 95})
    if skip_line:
        style_cell.update({'whiteSpace':'normal'})
    if all_border:
        style_cell.update({'border': '1px solid #ddd'})
        style_header.update({'border': '1px solid #ddd'})
    else:
        style_cell.update({
            'borderBottom': '1px solid #ddd',
            'borderTop': '0px',
            'borderRight': '0px',
            'borderLeft': '0px'
        })
        style_header.update({
            'borderBottom': '1px solid #ddd',
            'borderTop': '0px',
            'borderRight': '0px',
            'borderLeft': '0px'
        })
    return dash_table.DataTable(
            id = _id,
            data = data.to_dict('records'), 
            columns = [{"name": i, "id": i} for i in data.columns],
            page_size=page_size,
            virtualization=virtualization,
            fixed_rows={'headers': fixed_rows},
            style_table = style_table,
            style_header = style_header,
            style_cell = style_cell
        )