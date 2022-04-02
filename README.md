# Tensorgram

A simple Telegram Bot designed to alleviate the urge to repeatedly check training progress on Tensorboard.
Importing the bot into the training script and subscribing to the Telegram bot allows the user to track variables of interest.

Tracked variables can be set to either automatically send a Telegram message whenever their value is updated, or can be polled by the user via a message sent to the bot.

## Disclaimer

Work in progress use with care. Think twice before using this script on a machine that is not your own, or when working with sensitive data.
In principle, every Telegram user that knows the handle of the bot you create will be able to subscribe to updates about your model.
I make no claims about whether using this is a good idea and did not test security. This is intended as a fun project only (feel free to contribute and fix it though!).

## ToDo

- it would be nice to implement tracking of variables through a Tensorflow callback for better integration with Tensorflow training loops.
