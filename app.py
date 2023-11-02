import dash
from dash import html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("你好，Vercel!"),
    html.Div("這是在Vercel上的Dash應用。")
])

if __name__ == '__main__':
    app.run_server(debug=True)
