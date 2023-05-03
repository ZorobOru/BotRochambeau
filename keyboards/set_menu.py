from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon_ru import LEXICON_COMMAND_RU


async def set_start_menu(bot: Bot):
    main_menu_commands: list[BotCommand] = [BotCommand(command=command, description=description)
                            for command, description in LEXICON_COMMAND_RU.items()]
    await bot.set_my_commands(main_menu_commands)