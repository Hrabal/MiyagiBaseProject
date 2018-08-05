from Miyagi import App

from app import frontend

if __name__ == "__main__":
    app = App(config='config.yml', for_web=True, blueprints=[frontend, ])
    app.run()
