#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


# Connect to tournament database
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


# Delete all matches
def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM MATCHES;"
    cursor.execute(query)
    db.commit()
    db.close()


# Delete all players
def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM PLAYERS;"
    cursor.execute(query)
    db.commit()
    db.close()


# Counts all the players in the tournament
def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    query = "SELECT count(*) AS total FROM PLAYERS"
    cursor.execute(query)
    total = cursor.fetchone()
    db.close()
    return total[0]


# Register all the players
def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO players (name) VALUES ('%s')" % name
    cursor.execute(query)
    db.commit()
    db.close()


# Returns all player standings in the tournament
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    query = ("SELECT * FROM standings;")
    cursor.execute(query)
    matches = cursor.fetchall()
    db.commit()
    db.close()
    return matches


# Reports all the winners and losers
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    query = ("INSERT INTO matches (match_id, winner, loser) \
             VALUES (default, %s, %s);")
    cursor.execute(query, (winner, loser,))
    db.commit()
    db.close()


# Defines the swiss pairings in the tournament
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    number = int(countPlayers())
    pairings = []
    if (number > 0):
        for i in range(number):
            if (i % 2 == 0):
                id1 = standings[i][0]
                name1 = standings[i][1]
                id2 = standings[i+1][0]
                name2 = standings[i+1][1]
                pair = (id1, name1, id2, name2)
                pairings.append(pair)
    return pairings
