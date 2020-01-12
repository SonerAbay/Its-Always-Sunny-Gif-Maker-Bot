# TV Show Telegram Bot

This program creates a TV Show script database(sqlite) with timestamps using .srt files. If you order your .srt files by episode number **subtitle_to_database.py** will create a 2-table relational database for you. The name of the .srt files will be inserted into *episode_id* table.

Then you can create your own Telegram bot using this database. All telegram bot source code is in the /telegram folder. Don't forget to create your own telegram bot token via [BotFater](https://telegram.me/BotFather)

You can also use the english .srt [database](/db) created for my favorite show [It's Always Sunny in Philadelphia](https://www.imdb.com/title/tt0472954/). 

When a user types `/line [Line from the show]` the bot will find that line in the show and it will return with season, episode number, episode name, exact time from the discussion and a url to stream that particular episode.  
  
If you woud like to use sqlite **FTS5** features such as full-text search use the *lines* virtual table. Otherwise you can use the *subtitle* table.

You are all set after you add your token [here](/telegram.config.cfg).

### Required Packages
**For SQlite FTS5 features:**  
`pip install peewee`


### Command List:
  
**/line** - Enter a line from the show to find the episode.  
Usage: /line your line  
  
**/episodes** - Get the list of episodes from a season.  
Usage: /episodes season_number  
  
**/random** - Get a random episode from the show.  
Usage: /random  

**/help** - Returns the commands list  

**Extra Features**:
- If you add the bot to a group it will welcome the newcomer with an [ocular pat down](https://www.urbandictionary.com/define.php?term=ocular%20pat%20down)  


  
Please feel free to change and use it in any way you would like to!
