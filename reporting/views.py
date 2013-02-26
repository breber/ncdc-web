import datetime
import flask_login
import logging
import time

from flask import render_template, request, redirect, url_for, session, abort, send_file
from flask.views import MethodView
from models import User, TimeRecord

class UserAwareView(MethodView):
    """
    A base view class to extend.
    """

    @property
    def session(self):
        """
        Adds the session property to the view.
        """
        return session

    @property
    def user(self):
        """
        Adds the user property to the view.

        :returns: The currently logged in user if one exists, else None
        """
        if not flask_login.current_user.is_anonymous():
            return flask_login.current_user._get_current_object()
        else:
            return None

    def get_context(self, extra_ctx=None, **kwargs):
        """
        Adds a helper function to the view to get the context.

        :returns: The current context with the user set.
        """
        if self.user and self.user.is_admin:
            ctx = {
                'user': self.user,
            }
            if extra_ctx:
                ctx.update(extra_ctx)
            ctx.update(kwargs)
            return ctx
        else:
            return {}

class Home(UserAwareView):
    """
    The view for the home page.
    """
    def get(self):
        context = self.get_context()
        
        users = User.objects(is_team_admin=False)
        context = {
            'users': users,
            'user': self.user,
            'time': datetime.datetime.now().strftime('%I:%M:%S %p'),
            'datetime': datetime.datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
        }
        return render_template('admin.html', **context)

class Export(UserAwareView):
    """
    The REST API endpoint for getting payroll info about a user.
    """
    
    def get(self, username):
        return redirect('http://www.site2.cdc.com/export/%s' % username)
