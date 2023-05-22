from __init__ import create_app
from controllers.login import login_blueprint
from controllers.homePage import homePage_blueprint
from controllers.articlePage import articlePage_blueprint

app = create_app()
app.register_blueprint(articlePage_blueprint)
app.register_blueprint(homePage_blueprint)
app.register_blueprint(login_blueprint)
app.run(host='0.0.0.0', port=8099, debug=True)