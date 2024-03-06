from src.app import App


def lambda_handler(event, context):
    App(event, context).run()
