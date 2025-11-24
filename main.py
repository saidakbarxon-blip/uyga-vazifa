from telegram import Update
from telegram.ext import ContextTypes,CommandHandler,filters,Application,ConversationHandler,MessageHandler
import sqlite3



Q1,Q2,Q3 = range(3)

async def start(updade:Update,contect:ContextTypes.DEFAULT_TYPE):
    await updade.message.reply_text("salom siz mini quiz botga hush kelibsiz!")
    return Q1

async def start_quiz(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("1 - savol: O'zbekiston poytaxti qayer?")
    return Q1

async def answer_q1(update:Update,context:ContextTypes.DEFAULT_TYPE):
    javob = update.message.text.lower()

    if javob == "toshkent":
        await update.message.reply_text("to'g'ri 2 - savol")
    else:
        await update.message.reply_text("noto'g'ri javob")

    await update.message.reply_text("paythonda list qanday yoziladi")
    return Q2
 
async def answer_q2(update:Update,context:ContextTypes.DEFAULT_TYPE):
    javob = update.message.text.lower()

    if javob == "[] ichida yoziladi":
        await update.message.reply_text("to'g'ri javob.   3 - savol")
    else:
        await update.message.reply_text("noto'g'ri javob!")

    await update.message.reply_text("AI so'zi nimani qisqartmasi?")
    return Q3

async def answer_q3(update:Update,context:ContextTypes.DEFAULT_TYPE):
    javob = update.message.text.lower()

    if javob == "artificial intelligence":
        await update.message.reply_text("to'g'ri javob")
    else:
        await update.message.reply_text("noto'g'ri")

    await update.message.reply_text("Savollar tugadi")
    return ConversationHandler.END    
        
conv_hendler = ConversationHandler(
    entry_points=[CommandHandler("quiz",start_quiz)],
    states={
        Q1: [MessageHandler(filters.TEXT & ~filters.COMMAND,answer_q1)],
        Q2: [MessageHandler(filters.TEXT & ~filters.COMMAND,answer_q2)],
        Q3: [MessageHandler(filters.TEXT & ~filters.COMMAND,answer_q3)]

    },
    fallbacks=[]
)

if __name__=="__main__":
    TOKEN = "8375949175:AAFYrOEQvM-eTsdiAitaFTG2TLRKfAA2lFA"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(conv_hendler)
    app.add_handler(CommandHandler("start",start))
    print("bot ishga tushdi ... ")
    app.run_polling()
    
