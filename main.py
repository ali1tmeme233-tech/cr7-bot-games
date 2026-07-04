import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# قائمة نكت واسئلة
JOKES = [
    "محشش سألوه شنو اصعب شي؟ كال انك تقنع بنية انك ما خنتها وانت خنتها 😂",
    "واحد كسلان تزوج وحدة كسلانة جابو ولد مكسول يقوم يرضع",
    "محشش راح للمطعم كال للجرسون: عندكم عشاء؟ كاله اي، كاله لعد ليش ما تتعشون؟"
]

RIDDLES = [
    "شي يطير بلا جناح ويبكي بلا عيون؟ - السحاب",
    "شي اذا اكلته كله تستفيد واذا اكلت نصه تموت؟ - سمسم",
    "ما هو الشي الذي كلما اخذت منه كبر؟ - الحفرة"
]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا بيك بوت علوش 🎮\nعندي 50 لعبة\nاكتب /games تشوفهن كلهن")

# /games - القائمة
async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """🎮 قائمة 50 لعبة:
    
1-10: /dice /rps /num /coin /8ball /joke /riddle /love /luck /color
11-20: /animal /food /country /emoji /math /pass /name /age /mood /song
21-30: /movie /job /car /fruit /drink /city /weather /time /date /quote
31-40: /fact /advice /pickup /insult /compliment /truth /dare /would /never /rate
41-50: /ship /kill /marry /gift /dream /fear /superpower /zodiac /fortune /magic

اكتب اي امر وجرب 😎"""
    await update.message.reply_text(text)

# الالعاب 1-10
async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🎲 طلعلك: {random.randint(1, 6)}")

async def rps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✂️ انا اختاريت: {random.choice(['حجر 🪨', 'ورقة 📄', 'مقص ✂️'])}")

async def num(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔢 الرقم السري: {random.randint(1, 100)}")

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🪙 طلعلك: {random.choice(['صورة 🖼️', 'كتابة ✍️'])}")

async def ball8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answers = ["اي اكيد", "مستحيل", "يمكن", "اسأل بعدين", "لا تسألني", "طبعاً لا", "اكيد اي"]
    await update.message.reply_text(f"🎱 {random.choice(answers)}")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"😂 {random.choice(JOKES)}")

async def riddle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🤔 {random.choice(RIDDLES)}")

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"❤️ نسبة الحب وياك: {random.randint(0, 100)}%")

async def luck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🍀 نسبة حظك اليوم: {random.randint(0, 100)}%")

async def color(update: Update, context: ContextTypes.DEFAULT_TYPE):
    colors = ["احمر ❤️", "ازرق 💙", "اخضر 💚", "اصفر 💛", "بنفسجي 💜", "اسود 🖤"]
    await update.message.reply_text(f"🎨 لونك اليوم: {random.choice(colors)}")

# الالعاب 11-20
async def animal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🐾 حيوانك اليوم: {random.choice(['اسد 🦁', 'نمر 🐅', 'ذيب 🐺', 'صقر 🦅', 'دلفين 🐬', 'نسر 🦅'])}")

async def food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🍔 اكلتك اليوم: {random.choice(['بيتزا 🍕', 'بركر 🍔', 'شاورما 🌯', 'كباب 🍖', 'دولمة 🍲', 'باجة 😂'])}")

async def country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🌍 تسافر لـ: {random.choice(['دبي 🇦🇪', 'تركيا 🇹🇷', 'مصر 🇪🇬', 'المغرب 🇲🇦', 'مالديف 🏝️', 'سويسرا 🇨🇭'])}")

async def emoji(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{random.choice(['😂', '😍', '🔥', '😎', '🤔', '😭', '🥺', '💀', '👑', '⚡'])}")

async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    a, b = random.randint(1, 20), random.randint(1, 20)
    await update.message.reply_text(f"➕ حلها: {a} + {b} = ؟")

async def password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chars = "abcdefghijk123456!@#"
    pwd = ''.join(random.choice(chars) for _ in range(8))
    await update.message.reply_text(f"🔐 باسوورد قوي: {pwd}")

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📛 اسمك الجديد: {random.choice(['علوش', 'حمودي', 'عبود', 'كرار', 'مصطفى', 'سلطان'])}")

async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🎂 عمرك: {random.randint(18, 40)} سنة")

async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"😊 مودك: {random.choice(['سعيد', 'حزين', 'معصب', 'رايق', 'طفشان', 'متحمس'])}")

async def song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🎵 تسمع: {random.choice(['راشد الماجد', 'ماجد المهندس', 'حسين الجسمي', 'عمرو دياب', 'تامر حسني'])}")

# الالعاب 21-30
async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🎬 تشوف فلم: {random.choice(['Fast X', 'Avengers', 'Joker', 'Spider-Man', 'Batman'])}")

async def job(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💼 شغلتك: {random.choice(['دكتور', 'مهندس', 'طيار', 'مبرمج', 'تاجر', 'لاعب كرة'])}")

async def car(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🚗 سيارتك: {random.choice(['كامري', 'لاندكروزر', 'مرسيدس', 'BMW', 'فيراري', 'تاهو'])}")

async def fruit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🍎 فاكهتك: {random.choice(['تفاح', 'موز', 'مانجا', 'برتقال', 'عنب', 'رمان'])}")

async def drink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🥤 شرابك: {random.choice(['بيبسي', 'سفن', 'عصير برتقال', 'قهوة', 'شاي', 'حليب'])}")

async def city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🏙️ مدينتك: {random.choice(['بغداد', 'اربيل', 'البصرة', 'كربلاء', 'النجف', 'السليمانية'])}")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🌤️ الجو: {random.choice(['مشمس', 'غائم', 'ممطر', 'حار', 'بارد', 'ترابي 😂'])}")

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import datetime
    await update.message.reply_text(f"⏰ الوقت: {datetime.now().strftime('%H:%M:%S')}")

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import datetime
    await update.message.reply_text(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d')}")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = ["الحياة حلوة", "اضحك للدنيا تضحكلك", "لا تيأس", "انت كدها", "اليوم احلى من باجر"]
    await update.message.reply_text(f"💬 {random.choice(quotes)}")

# الالعاب 31-40
async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    facts = ["الاخطبوط عنده 3 قلوب", "النملة ما تنام", "الزرافة ما لها صوت", "الدلفين ينام وعين مفتوحة"]
    await update.message.reply_text(f"🧠 معلومة: {random.choice(facts)}")

async def advice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    adv = ["نام زين", "اشرب ماي", "لا تسهر", "العب رياضة", "ابتسم", "صلي"]
    await update.message.reply_text(f"💡 نصيحة: {random.choice(adv)}")

async def pickup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lines = ["انت من السما لو نازل؟", "ضايع ولا ادور عليك؟", "عيونك GPS؟ لان ضيعت طريقي"]
    await update.message.reply_text(f"😏 {random.choice(lines)}")

async def insult(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🤬 {random.choice(['وجهك وجه نوم', 'ذكائك خارق... خارق للنازل 😂', 'انت سالب بالحياة'])}")

async def compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🥰 {random.choice(['انت ملك', 'عيونك تجنن', 'ضحكتك حلوة', 'انت ذهب'])}")

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = ["تحب منو؟", "شنو اكبر كذبة كذبتها؟", "تبجي اخر مرة شوكت؟", "شنو تخاف منه؟"]
    await update.message.reply_text(f"🤥 صراحة: {random.choice(q)}")

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    d = ["ارسل صوتك", "غير اسمك", "نزل ستوري", "اعترف لشخص تحبه"]
    await update.message.reply_text(f"😈 تحدي: {random.choice(d)}")

async def would(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🤔 لو خيروك: {random.choice(['تطير لو تختفي؟', 'مليون دولار لو حب حياتك؟', 'تعيش بالماضي لو المستقبل؟'])}")

async def never(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🙅 ما عمري: {random.choice(['سافرت', 'بجيت كدام الناس', 'كذبت على امي', 'سرقت'])}")

async def rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"⭐ اقيمك: {random.randint(1, 10)}/10")

# الالعاب 41-50
async def ship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💑 تنزوج: {random.choice(['ما ادري', 'بنت الجيران', 'المشهورة', 'صديقتك', 'ولا وحدة 😂'])}")

async def kill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔪 تقتل: {random.choice(['الناموس', 'الصرصور', 'البرد', 'الحر', 'الملل'])}")

async def marry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💍 تتزوج: {random.choice(['باجر', 'بعد سنة', 'بعد 10 سنين', 'ما تتزوج 😂'])}")

async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🎁 هديتك: {random.choice(['ايفون', 'سيارة', 'سفرة', 'فلوس', 'بلوك 😂'])}")

async def dream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💭 حلمك: {random.choice(['تصير مليونير', 'تسافر للفضاء', 'تتزوج', 'تشتري بيت', 'تصير مشهور'])}")

async def fear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"😱 تخاف من: {random.choice(['الظلام', 'المرتفعات', 'العنكبوت', 'الفشل', 'الوحدة'])}")

async def superpower(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"⚡ قوتك الخارقة: {random.choice(['الطيران', 'الاختفاء', 'قراءة الافكار', 'السفر بالزمن', 'القوة الخارقة'])}")

async def zodiac(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"♈ برجك: {random.choice(['الحمل', 'الثور', 'الجوزاء', 'السرطان', 'الاسد', 'العذراء', 'الميزان', 'العقرب', 'القوس', 'الجدي', 'الدلو', 'الحوت'])}")

async def fortune(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔮 حظك: {random.choice(['راح تصير غني', 'راح تحب', 'راح تسافر', 'راح تنجح', 'راح تنصدم 😂'])}")

async def magic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✨ سحر: {random.choice(['اختفيت', 'صرت مليونير', 'رجعت طفل', 'طرت', 'ولا شي صار 😂'])}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    # اضافة كل الاوامر
    commands = [
        ("start", start), ("games", games), ("dice", dice), ("rps", rps), ("num", num),
        ("coin", coin), ("8ball", ball8), ("joke", joke), ("riddle", riddle), ("love", love),
        ("luck", luck), ("color", color), ("animal", animal), ("food", food), ("country", country),
        ("emoji", emoji), ("math", math), ("pass", password), ("name", name), ("age", age),
        ("mood", mood), ("song", song), ("movie", movie), ("job", job), ("car", car),
        ("fruit", fruit), ("drink", drink), ("city", city), ("weather", weather), ("time", time),
        ("date", date), ("quote", quote), ("fact", fact), ("advice", advice), ("pickup", pickup),
        ("insult", insult), ("compliment", compliment), ("truth", truth), ("dare", dare), ("would", would),
        ("never", never), ("rate", rate), ("ship", ship), ("kill", kill), ("marry", marry),
        ("gift", gift), ("dream", dream), ("fear", fear), ("superpower", superpower), ("zodiac", zodiac),
        ("fortune", fortune), ("magic", magic), ("ping", ping)
    ]
    
    for cmd, func in commands:
        app.add_handler(CommandHandler(cmd, func))
    
    print("Bot is running with 50 games...")
    app.run_polling()

if __name__ == "__main__":
    main()
