import views


def add_urls(app):
    """
    Helper function for adding url rules to the application.  Any url answered by the application
    has to be mapped to a view function here.

    :param app: The Flask app running the application.
    """
    app.add_url_rule('/', view_func=views.Home.as_view('home'))
    app.add_url_rule('/export/<username>/', view_func=views.Export.as_view('export'))
