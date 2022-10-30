import telebot
import scraping
import time
API_KEY = '2001832124:AAHUUlwWz9gK51O8JB_8__3SeaNegFZKvk4'
bot = telebot.TeleBot(API_KEY)
k = 'xyz'
l = 'abc'
@bot.message_handler(commands=['start', 'hello', 'hi'])
def greet(message):
  bot.reply_to(message, "Hi! How can i Help you ?\n1.seek\nreply with / for all the messages")
  @bot.message_handler(commands=['1', 'seek'])
  def seek(message):
    bot.send_message(message.chat.id, "What job are you looking for ?\nsearch by company name:\nAccenture\ngenpact\nibm\ney\noracle\nwipro\nust\ninfosys\nvirtusa\nhcl\n\nsearch by job title:\nsoftware_engineer\napplication_developer\njavascript_developer\nsenior_software_engineer\njava_software_engineer\nfull_stack_engineer\ndotnet_developer\nphp_developer\nbusiness_development_manager\nbusiness_development_executive\n\nsearch by job function:\ninformation_technology\nengineering\nsales\nbusiness_development\nmarketing\nother\nmanagement\nmanufacturing\nhuman_resources\ndesign")
    @bot.message_handler(commands=['Accenture', 'genpact', 'ibm', 'ey', 'oracle', 'wipro', 'ust', 'infosys', 'virtusa', 'hcl', 'software_engineer', 'application_developer', 'javascript_developer', 'senior_software_engineer', 'java_software_engineer', 'full_stack_engineer', 'dotnet_developer', 'php_developer', 'business_development_manager', 'business_development_executive', 'information_technology', 'engineering', 'sales', 'business_development', 'marketing', 'other', 'management', 'manufacturing', 'human_resources', 'design'])
    def job(message):
      keyword = message.text.split()
      global k
      k = keyword[0]
      k = k[1:]
      bot.send_message(message.chat.id, "where do you want to work ?\nlocations:\nindia\nbengaluru\nmumbai\nhyderabad\npune\ngurgaon\nchennai\nkolkata\nnoida\nchennai\nahmedabad")
      @bot.message_handler(commands=['india', 'bengaluru', 'mumbai', 'hyderabad', 'pune', 'gurgaon', 'kolkata', 'chennai', 'noida', 'ahmedabad', 'delhi'])
      def loc(message):
        location = message.text.split()
        global l
        l = location[0]
        l = l[1:]
        bot.send_message(message.chat.id, "please wait till we collect the data you asked for.")
        scraping.linkedin(k, l)
        time.sleep(7)
        for i in range(len(scraping.job_link)):
          bot.send_message(message.chat.id, scraping.job_link[i])
      

bot.polling()
