from flask import Flask
from blue.api.routes import mod
from blue.site.routes import mod

app=Flask(__name__)

app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod,url_prefix='/api')