#!usr/bin/env python3
"""Babel Flask app"""
from flask import Flask, request, render_template
from flask_babel import Babel


babel = Babel()


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        """Select the best match language for the user"""
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    @app.route('/')
    def index():
        """Index route"""
        return render_template('1-index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
