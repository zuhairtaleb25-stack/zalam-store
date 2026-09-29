import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن البوت الحقيقي والحي الخاص بك والمجرب بنجاح 
TOKEN = "8678868704:AAHmbqL68xBcJFEcEZQRi4cwDCniVnu3q3k"
bot = telebot.TeleBot(TOKEN)

# 1. القائمة الرئيسية الاحترافية (تظهر عند إرسال /start)
def get_main_keyboard():
    markup = InlineKeyboardMarkup(row_width=1) # ترتيب الأزرار تحت بعضها بشكل احترافي
    
    btn_services = InlineKeyboardButton("🛍️ الخدمات والأسعار", callback_data="view_services")
    btn_wallet = InlineKeyboardButton("💰 محفظتي لشحن الرصيد", callback_data="view_wallet")
    btn_account = InlineKeyboardButton("📝 حسابي الشخصي", callback_data="view_account")
    btn_orders = InlineKeyboardButton("📦 طلباتي السابقة", callback_data="view_orders")
    btn_support = InlineKeyboardButton("📞 تواصل مع الإدارة", callback_data="view_support")
    
    markup.add(btn_services, btn_wallet, btn_account, btn_orders, btn_support)
    return markup

# 2. قائمة الخدمات الفرعية المخصصة لشحن الألعاب
def get_services_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    btn_ff = InlineKeyboardButton("💎 شحن جواهر فري فاير (Free Fire)", callback_data="buy_ff")
    btn_pubg = InlineKeyboardButton("🪙 شحن شدات ببجي موبايل (PUBG UC)", callback_data="buy_pubg")
    btn_back = InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="go_main")
    markup.add(btn_ff, btn_pubg, btn_back)
    return markup

# استقبال أمر البداية /start وتوليد الواجهة التفاعلية
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "🎯 **أهلاً بك في Taleb Digital المطور!**\n\nاختر من القائمة في الأسفل لبدء الطلب أو مراجعة حسابك المحفوظ:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_keyboard(), parse_mode="Markdown")

# معالجة الضغطات الذكية على الأزرار التفاعلية وتحويل القوائم بلمحة بصر
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    if call.data == "view_services":
        bot.edit_message_text("🛍️ **قائمة الخدمات المتوفرة للتسليم الفوري:**\nاختر اللعبة المراد شحنها الآن:", 
                              call.message.chat.id, call.message.message_id, reply_markup=get_services_keyboard(), parse_mode="Markdown")
        
    elif call.data == "go_main":
        bot.edit_message_text("🎯 **أهلاً بك في Taleb Digital المطور!**\n\nاختر من القائمة في الأسفل لبدء الطلب أو مراجعة حسابك المحفوظ:", 
                              call.message.chat.id, call.message.message_id, reply_markup=get_main_keyboard(), parse_mode="Markdown")
        
    elif call.data == "view_wallet":
        wallet_text = "💰 **قسم محفظتك المالية:**\n───────────────────\n💳 رصيدك الحالي: `$0.00`\n\n⚠️ لشحن رصيد محفظتك لتتمكن من الشراء التلقائي، يرجى تحويل المبلغ إلى الحساب التالي:\n👉 `94046e6860d4ba8897e918b5e9fed55e`\nثم أرسل صورة الإيصال للإدارة لتفعيل الرصيد فوراً!"
        bot.edit_message_text(wallet_text, call.message.chat.id, call.message.message_id, 
                              reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🔙 عودة", callback_data="go_main")), parse_mode="Markdown")
        
    elif call.data == "view_account":
        account_text = f"📝 **تفاصيل حسابك الرقمي:**\n───────────────────\n👤 الاسم: {call.from_user.first_name}\n🆔 معرف التليجرام: `{call.from_user.id}`\n🌐 رتبة الحساب: زبون دائم وعضو نشط 🟢"
        bot.edit_message_text(account_text, call.message.chat.id, call.message.message_id, 
                              reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🔙 عودة", callback_data="go_main")), parse_mode="Markdown")
        
    elif call.data == "view_orders":
        bot.edit_message_text("📦 **قائمة طلباتك:**\n───────────────────\n📭 ليس لديك أي طلبات سابقة قيد الانتظار حالياً.", 
                              call.message.chat.id, call.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🔙 عودة", callback_data="go_main")), parse_mode="Markdown")
        
    elif call.data == "view_support":
        bot.edit_message_text("📞 **الدعم الفني المباشر للإدارة:**\n───────────────────\n👨‍💻 لطلب دعم فني أو الإبلاغ عن مشكلة بشحن الـ ID، تفضل بمراسلة المدير المسؤول مباشرة عبر المعرّف: @zuhair_taleb", 
                              call.message.chat.id, call.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🔙 عودة", callback_data="go_main")), parse_mode="Markdown")
        
    elif call.data in ["buy_ff", "buy_pubg"]:
        bot.answer_callback_query(call.id, "🚧 جاري تجهيز حقول كميات الشحن الفورية لهذا القسم...", show_alert=True)

# تفعيل عمل البوت بأعلى كفاءة مستقرة
bot.infinity_polling()
