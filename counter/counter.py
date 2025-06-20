from flask import Flask, Response
from counter import status


def create_counter_container() -> dict:
    return {}


def create_app() -> Flask:
    app = Flask( __name__, instance_relative_config=True )
    counters = create_counter_container()

    @app.route( "/counters/<name>", methods=[ "POST" ])
    def create_counter( name: str ) -> Response:
        """Creates a counter"""
        app.logger.info( f"Request to create counter: {name}" )

        if name in counters:
            return (
                { "message": f"Counter {name} already exists" },
                status.HTTP_409_CONFLICT,
            )

        counters[ name ] = 0
        return ({ name: counters[ name ]}, status.HTTP_201_CREATED )

    @app.route( "/counters/<name>", methods=[ "GET" ])
    def read_counter( name: str ) -> Response:
        """Reads a counts"""
        app.logger.info( f"Request to get counter: {name}" )
        return (
            { "message": f"Counter '{name}' not found" },
            status.HTTP_204_NO_CONTENT,
        )

    @app.route( "/counters/<name>", methods=[ "PUT" ])
    def update_counter( name: str ) -> Response:
        """Updates a counter"""
        app.logger.info( f"Request to update counter: {name}" )

        if name not in counters:
            return (
                { "messge": f"Counter '{name}' not found" },
                status.HTTP_204_NO_CONTENT,
            )

        counters[ name ] += 1
        return ({ name: counters[ name ]}, status.HTTP_200_OK )

    return app
