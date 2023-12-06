from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler,filters,ContextTypes

TOKEN:Final= '6773621260:AAFth75rPfpN7gpKQCA1wbk0DjV2q183cy4'
BOT_USERNAME:Final ='@your_number1_bot'



async def start_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello! Thanks for chatting with me! i am helper!')
    
    
    
async def help_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' i am a helper! please type something so I can respond!')
    
 
 
async def custom_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')   
    
    
    
    
def handle_response(text:str)-> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'hey there!'
    
    if 'how are you' in processed:
        return 'i am good!,how about you?'
    
    if 'i am good too' in processed:
        return 'good to hear👉 '
    
    
    return 'i do not understand what you wrote ...'


async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    
    message_type: str = update.message.chat.type
    text:str = update.message.text
    
    print(f'User({update.message.chat.id})in {message_type}:"{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').srtip()
            response:str= handle_response(new_text)
            
        else:
            return
    else:
        response:str = handle_response(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)
    
    
async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print (f'update {update} caused error {context.error}')
    
    
if __name__ =='__main__':
    
    print('starting bot ...')
    app = Application.builder().token(TOKEN).build()
    
    
    app.add_handler(CommandHandler('start',start_command))    
    app.add_handler(CommandHandler('help',help_command))    
    app.add_handler(CommandHandler('custom',custom_command))
    
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    
    app.add_error_handler(error)  
    
    
    print('polling ...')
    app.run_polling(poll_interval=3)  
    