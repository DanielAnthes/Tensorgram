from tensorbot import Tensorbot
import time

bot = Tensorbot()

var = bot.register_variable("test", "", autoupdate=True)
for i in range(10):
    time.sleep(2)
    print(i)
    var.update(f"iteration {i}")
print("done testing")