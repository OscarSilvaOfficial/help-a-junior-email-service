from api.middlewares.application import ApplicationManager
from api import urls

app = ApplicationManager().get_app()

if __name__ == '__main__':
    app.run(debug=True)