# connect4

## Usage

Clone the repo by navigating to an appropriate directory and typing

```
git clone https://github.com/srblum/connect4.git
```

To run the server, first enter the connect4 directory using 

```
cd connect4
```

And then run the flask server using

```
./flaskTest.py
```

This requires that you have python 2.7 as well as the flask module installed.

The server should now be listening on port 5000.  Just navigate to localhost:5000 in your browser.

## ToDo

* Make a responsive and aesthetic GUI
* Include win-checking in existing "move" server endpoint
* Handle move validation client-side, not server-side
* Add game ID feature that allows remote multiplayer
* Implement text box for game messages as well as user chat