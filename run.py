from Miyagi import App

from app import frontend

if __name__ == "__main__":
    app = App(config='config.yml', custom_pages=[frontend, ])
    app.run()
