from app.settings import bot, secrets  
from app import views  


async def start_bot():  
    await bot.send_message(secrets.admin_id, views.start_bot_message())  


async def stop_bot():  
    await bot.send_message(secrets.admin_id, views.stop_bot_message())