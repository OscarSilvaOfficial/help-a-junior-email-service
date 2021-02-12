from api.middlewares.application import ApplicationManager
from api import urls

app = ApplicationManager().app

if __name__ == '__main__':
    app.run(debug=True)