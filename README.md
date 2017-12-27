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

* Make a responsive and aesthetic GUI (Sean)
* Include win-checking in existing "move" server endpoint (Linch)
* Handle move validation client-side, not server-side (Linch)
* Add game ID feature that allows remote multiplayer (Linch)
  * Add "create room" button and associated JS and flask functions
  * Generates random URL, which is passed back to the client and displayed for sharing
  * Create new instance of connect4 python class with unique ID associated with URL
  * Modify /move endpoint to link game URL with connect4 object ID
* Add support for spectators and player1/2 selection
* Implement text box for game messages as well as user chat (Sean)
* Figure out hosting



:christmas_tree: