## Tournament Results ##

## What's included: ##

##Quickstart
##Install
*Install [Vagrant](https://www.vagrantup.com/)
*Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

**tournament.py**
This is a python file, it has all the modules defined. One that handles the swiss pairings, another that reports matches winners and losers, registers players of the match, deletes matches and players and counts all the players for a tournament.

**tournament.sql**
This is a sql file. Its code deletes and creates a new tournament database. This file also creates the tables for players and matches.
It also connects to the database and creates a view for the player standings.

**tournament_test.py**
This is a test python file that run against all the modules of tournament.py. This makes sure there are no buds in the program.

## How to Run this Program: ##
Before you can run your code or create your tables, you'll need to use the create database command in psql to create the database. Use the name tournament for your database.

Then you can connect psql to your new database and create your tables from the statements you've written in tournament.sql. You can do this in either of two ways:

Paste each statement in to psql.
 * Use the command \i tournament.sql to import the whole file into psql at once.
 * To deploy this app in google app engine load this program in google app engine and click on deploy.

