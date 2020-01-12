# TV Show Telegram Bot

This program creates a TV Show script database(sqlite) with timestamps using .srt files. If you order your .srt files by episode number **subtitle_to_database.py** will create a 2-table relational database for you. 

Then you can create your own Telegram bot using this database. All telegram bot source code is in the /telegram folder. Don't forget to create your own telegram bot token via https://telegram.me/BotFather

You are all set if you add your token here.

### Command List:
  
**/line** - Enter a line from the show to find the episode.  
Usage: /line your line  
  
**/episodes** - Get the list of episodes from a season.  
Usage: /episodes season_number  
  
**/random** - Get a random episode from the show.  
Usage: /random  
