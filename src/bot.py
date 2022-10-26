from vkbottle import load_blueprints_from_package
from vkbottle import Bot

from config import VK_API_KEY

bot = Bot(
    token=VK_API_KEY,
)

for bp in load_blueprints_from_package("blueprints"):
    bp.load(bot)

bot.run_forever()
