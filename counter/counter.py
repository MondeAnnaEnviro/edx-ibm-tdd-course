from flask import Flask
from counter import status


app = Flask( __name__ )
COUNTERS = {}


@app.route( "/counters/<name>", methods=[ "POST" ])
def create_counter( name, counters=COUNTERS ):
    """Creates a counter"""
    app.logger.info( f"Request to create counter: {name}" )

    if name in counters:
        return { "message": f"Counter {name} already exists" }, status.HTTP_409_CONFLICT

    counters[name] = 0
    return { name: counters[ name ]}, status.HTTP_201_CREATED


