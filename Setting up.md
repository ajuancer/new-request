# Before stating
You should have installed all the described in `Needed tools.md`. The items there are:
- [ ] Python (if possible the latest version).
- [ ] Selenium browser automation kit for Python.
- [ ] Google Chrome Browser.
- [ ] Chrome Driver.
- [ ] Telegram app.

If you don't have any of the items listed, read `Needed tools.md` before proceding this tutorial.

# Step 1: Downloading the desired version bot.
Currently, there're two variants of the bot. `main.py` is the python file that can do all the process automatized. In order to achieve this goal, you must write your Google password in a variable. Also note that you need to disable the 2-step verification.
The other variant is the `without-password.py`. This needs your pressence for the login step. When you ejecute the bot, it'll type your mail account, but you will have to type your password. Also, as you need to do this step, you don't need to disable the 2-step verification.

# Step 2: Creating a Telegram bot.
## 2.1: Talk to father bot.
If you have never created bots in Telegram, you need to know what FatherBot is. Hopeffully, at the end of this contest, you'll get some time to explore this incredible and funny world.
FatherBot is the mannager of all the bots linked to your account. Normally, it doesn't appear in your chats. 

1. Find it by searching `@botfather`. Enter in the chat.
2. Type `/newbot` and press sent. Then 'he' will request you a name. This name it's like the name of any other contact. After that, you need to give a username. Normally, it's based in the name of the bot, but keep in mind that it must not contain spaces (use underscores if you want to separate text), and use only lower case letter.
3. Now, fatherBot tells you that all the process is done. Before closing the chat, copy the HTTP API token (the long set of characters and numbers). Keep in mind that this token is like a password and you shouldn't share it with anyone.

## 2.2: Open the bot you have just created.
Go to the chats page and click on the bot you created. Send `/start` or press the start button. Nothing is going to happen, because the bot doesn't know anything, not even talk. But you will initialize  the conversation, in order to get the chat ID.

## 2.3: Obtain the chat ID. 
In another tab of the browser, open this web, `https://api.telegram.org/bot<TOKEN>/getUpdates` , replacing `TOKEN` with the token we obtained in step 2.1.
Copy it.

# Step 3: Edit the python file.
Open with an editor the version you selected. We're going to insert our private information.
## 3.1: Changing variables.
- Change the value of variable `usernameStr` to your Google mail. Here is a tip: if your mail is something like `thisisnotmymail@gmail.com` you just need to write `thisisnotmymail`.
- Change the value of the variable `passwordStr` to your password. This variable only appears in the `main.py` file.

## 3.2: Insert your bot's token.
- In the `telegram_bot_sendtext()` function, insert the token you got in step 2.1 in the variable `bot_token` and the ID you got in step 2.3 in the `bot_chatID` variable.

## 3.3: Save the changes.
Normally, the shortcut ctrl+s do the work.

# Step 4: Checking.
Congratulations! Your bot is finished. You can execute  it by typing `pyhon main.py` (or `python without-password.py` depending on the variant) before **changing the directory of the CMD to the one in which the python file is**.
Don't doubt in opening an issue if you get in any trouble.
