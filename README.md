# Anti AFK

A script for logging in/out in WoW for Windows.

## Dependencies
!!! Be sure to be in the repository directory. !!!

Use [venv](https://virtualenv.pypa.io/en/latest/) (or not, if you can't be bothered).

Dependencies:
1. Python 3 (ex. 3.8 works)
2. pywin32: Type into CMD:
   
   ```pip install -r requirements.txt``` 
   
   or

   ```pip install pywin32``` 
   
## How it works
After a few seconds the script will automatically focus the wow window (works only with one window open) and type /logout into the chat.
After that, it will again wait for a while and press ENTER to log in.
Then, it waits for a much longer time to repeat the process.

These time values are all defined in [config.json](./config.json) and can be edited. If you screw something up, delete the config file, it will be created automatically on script start.

## Usage
!!! Be sure to be in the repository directory. !!!

To run the script, type into CMD:

```python3 main.py```

## Recommendations
1. Use a stealth character, you can log in/out without breaking stealth and it reduces report risk if someone notices you.
2. The default values are 5s logout, 10s login and 8 minutes wait time. Use them or change them to something you think makes sense.
