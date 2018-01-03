from transitions.extensions import GraphMachine
import vlc
import time
import socket
import ssl


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        socket.setdefaulttimeout(60 * 60)
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    #is_going_to

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    #eating

    def is_going_to_eating(self, update):
        text = update.message.text
        return text.lower() == 'eating'

    def is_going_to_rice(self, update):
        text = update.message.text
        return text.lower() == 'rice'

    def is_going_to_ricelocation(self, update):
        text = update.message.text
        return text.lower() == 'where'

    def is_going_to_noodle(self, update):
        text = update.message.text
        return text.lower() == 'noodle'

    def is_going_to_noodlelocation(self, update):
        text = update.message.text
        return text.lower() == 'where'

    def is_going_to_fastfood(self, update):
        text = update.message.text
        return text.lower() == 'fastfood'

    def is_going_to_fastfoodlocation(self, update):
        text = update.message.text
        return text.lower() == 'where'

    #music

    def is_going_to_music(self, update):
        text = update.message.text
        return text.lower() == 'music'

    def is_going_to_eng(self, update):
        text = update.message.text
        return text.lower() == 'eng'

    def is_going_to_eng1(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_eng2(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_eng3(self, update):
        text = update.message.text
        return text.lower() == '3'

    def is_going_to_eng4(self, update):
        text = update.message.text
        return text.lower() == '4'

    def is_going_to_eng5(self, update):
        text = update.message.text
        return text.lower() == '5'

    def is_going_to_eng6(self, update):
        text = update.message.text
        return text.lower() == '6'

    def is_going_to_eng7(self, update):
        text = update.message.text
        return text.lower() == '7'

    #chinese
    def is_going_to_chi(self, update):
        text = update.message.text
        return text.lower() == 'chi'

    def is_going_to_chi1(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_chi2(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_chi3(self, update):
        text = update.message.text
        return text.lower() == '3'

    def is_going_to_chi4(self, update):
        text = update.message.text
        return text.lower() == '4'

    def is_going_to_chi5(self, update):
        text = update.message.text
        return text.lower() == '5'

    def is_going_to_chi6(self, update):
        text = update.message.text
        return text.lower() == '6'

    def is_going_to_chi7(self, update):
        text = update.message.text
        return text.lower() == '7'

    #state1

    def on_enter_state1(self, update):
        update.message.reply_text("I'm entering state1")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    #state2

    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    #Eating

    def on_enter_eating(self, update):
        update.message.reply_text("Waht do you prefer rice ,noodle ,fastfood?")

    def on_exit_eating(self, update):
        print('Leaving eating')

    #rice

    def on_enter_rice(self, update):
        update.message.reply_text("那要吃日喜(蒸蛋飯)嗎?")
        update.message.reply_photo(open("pic/1.jpg","rb"))
        update.message.reply_photo(open("pic/2.jpg","rb"))

    def on_exit_rice(self, update):
        print('Leaving rice')

    def on_enter_ricelocation(self, update):
        update.message.reply_photo(open("pic/3.PNG","rb"))
        update.message.reply_text("他在台南市東區育樂街238號")
        #update.message.reply_photo(open("pic/3.png","rb"))
        self.go_back(update)

    def on_exit_ricelocation(self, update):
        print('Leaving ricelocation')

    #noodle

    def on_enter_noodle(self, update):
        update.message.reply_text("那要吃甜麵屋嗎?")
        update.message.reply_photo(open("pic/4.jpg","rb"))
        update.message.reply_photo(open("pic/5.jpg","rb"))

    def on_exit_noodle(self, update):
        print('Leaving noodle')

    def on_enter_noodlelocation(self, update):
        update.message.reply_photo(open("pic/6.PNG","rb"))
        update.message.reply_text("他在台南市東區育樂街79號")
        self.go_back(update)

    def on_exit_noodlelocation(self, update):
        print('Leaving noodlelocation')

    #fastfood

    def on_enter_fastfood(self, update):
        update.message.reply_text("那要吃彩虹城堡嗎?")
        update.message.reply_photo(open("pic/7.jpg","rb"))
        update.message.reply_photo(open("pic/8.jpg","rb"))

    def on_exit_fastfood(self, update):
        print('Leaving fastfood')

    def on_enter_fastfoodlocation(self, update):
        update.message.reply_photo(open("pic/9.PNG","rb"))
        update.message.reply_text("他在台南市東區大學路22巷19－１號")
        self.go_back(update)

    def on_exit_fastfoodlocation(self, update):
        print('Leaving noodlelocation')

    #music

    def on_enter_music(self, update):
        update.message.reply_text("Waht do you prefer chinese ,english ,japanese?")

    def on_exit_music(self, update):
        print('Leaving music')

    #english
    def on_enter_eng(self, update):
        update.message.reply_text("1.Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat\n2.Don Omar-Danza Kuduro Lyrics\n3.Linkin Park - Leave Out All The Rest\n4.OneRepublic-Secrets\n5.Phillip Phillips - Gone, Gone, Gone\n6.Simple Plan - Jet Lag ft. Marie-Mai\n7.The Cab - Angel With A Shotgun")

    def on_exit_eng(self, update):
        print('Leaving eng')


    #1.Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat
    def on_enter_eng1(self, update):

        update.message.reply_audio(open("music/Eng/Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat.mp3","rb"))
        update.message.reply_text("Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat")
        self.go_back(update)

    def on_exit_eng1(self, update):
        print('Leaving eng1')

    #2.Don Omar-Danza Kuduro Lyrics
    def on_enter_eng2(self, update):

        update.message.reply_audio(open("music/Eng/Don Omar-Danza Kuduro.mp3","rb"))
        update.message.reply_text("Don Omar-Danza Kuduro")
        self.go_back(update)

    def on_exit_eng2(self, update):
        print('Leaving eng2')


    #3.Linkin Park - Leave Out All The Rest
    def on_enter_eng3(self, update):

        update.message.reply_audio(open("music/Eng/Linkin Park - Leave Out All The Rest.mp3","rb"))
        update.message.reply_text("Linkin Park - Leave Out All The Rest")
        self.go_back(update)

    def on_exit_eng3(self, update):
        print('Leaving eng3')

    #4.OneRepublic-Secrets
    def on_enter_eng4(self, update):

        update.message.reply_audio(open("music/Eng/OneRepublic-Secrets.mp3","rb"))
        update.message.reply_text("OneRepublic-Secrets")
        self.go_back(update)

    def on_exit_eng4(self, update):
        print('Leaving eng4')

    #5.Phillip Phillips - Gone, Gone, Gone
    def on_enter_eng5(self, update):

        update.message.reply_audio(open("music/Eng/Phillip Phillips - Gone, Gone, Gone.mp3","rb"))
        update.message.reply_text("Phillip Phillips - Gone, Gone, Gone")
        self.go_back(update)

    def on_exit_eng5(self, update):
        print('Leaving eng5')

    #6.Simple Plan - Jet Lag ft. Marie-Mai
    def on_enter_eng6(self, update):

        update.message.reply_audio(open("music/Eng/Simple Plan - Jet Lag ft. Marie-Mai.mp3","rb"))
        time.sleep(10)
        update.message.reply_text("Simple Plan - Jet Lag ft. Marie-Mai")
        self.go_back(update)

    def on_exit_eng6(self, update):
        print('Leaving eng6')

    #7.The Cab - Angel With A Shotgun
    def on_enter_eng7(self, update):

        socket.setdefaulttimeout(0.0)
        update.message.reply_audio(open("music/Eng/The Cab - Angel With A Shotgun.mp3","rb"))
        update.message.reply_text("The Cab - Angel With A Shotgun")
        self.go_back(update)

    def on_exit_eng7(self, update):
        print('Leaving eng7')

    #chinese
    def on_enter_chi(self, update):
        update.message.reply_text("1.DANCE FLOW-戀愛小動作\n2.F.I.R.-我要飛\n3.io樂團 - Pati pati\n4.io樂團 - 回到17歲\n5.棒棒堂+黑澀會美眉 - 黑糖秀\n6.河仁傑 - 接不接受\n7.黑澀會美眉 - Hello愛情風")

    def on_exit_chi(self, update):
        print('Leaving chi')

    #1.DANCE FLOW-戀愛小動作
    def on_enter_chi1(self, update):

        update.message.reply_audio(open("music/Chi/DANCE FLOW-戀愛小動作.mp3","rb"))
        #update.message.reply_text("https://www.youtube.com/watch?v=u0xrRyJFlgA")
        update.message.reply_text("DANCE FLOW-戀愛小動作")
        self.go_back(update)

    def on_exit_chi1(self, update):
        print('Leaving chi1')

    #2.F.I.R.-我要飛
    def on_enter_chi2(self, update):

        update.message.reply_audio(open("music/Chi/F.I.R.-我要飛.mp3","rb"))
        update.message.reply_text("F.I.R.-我要飛")
        self.go_back(update)

    def on_exit_chi2(self, update):
        print('Leaving chi2')

    #3.io樂團 - Pati pati
    def on_enter_chi3(self, update):

        update.message.reply_audio(open("music/Chi/io樂團 - Pati pati.mp3","rb"))
        update.message.reply_text("io樂團 - Pati pati")
        self.go_back(update)

    def on_exit_chi3(self, update):
        print('Leaving chi3')

    #4.io樂團 - 回到17歲
    def on_enter_chi4(self, update):

        update.message.reply_audio(open("music/Chi/io樂團 - 回到17歲.mp3","rb"))
        update.message.reply_text("io樂團 - 回到17歲")
        self.go_back(update)

    def on_exit_chi4(self, update):
        print('Leaving chi4')

    #5.棒棒堂+黑澀會美眉 - 黑糖秀
    def on_enter_chi5(self, update):

        update.message.reply_audio(open("music/Chi/棒棒堂+黑澀會美眉 - 黑糖秀.mp3","rb"))
        update.message.reply_text("棒棒堂+黑澀會美眉 - 黑糖秀")
        self.go_back(update)

    def on_exit_chi5(self, update):
        print('Leaving chi5')

    #6.河仁傑 - 接不接受
    def on_enter_chi6(self, update):

        update.message.reply_document(open("music/Chi/河仁傑 - 接不接受.mp3","rb"))
        update.message.reply_text("河仁傑 - 接不接受")
        self.go_back(update)

    def on_exit_chi6(self, update):
        print('Leaving chi6')

    #7.黑澀會美眉 - Hello愛情風
    def on_enter_chi7(self, update):

        #sendAudio(open("music/Chi/黑澀會美眉 - Hello愛情風.mp3","rb"))
        update.message.reply_audio(open("music/Chi/黑澀會美眉 - Hello愛情風.mp3","rb"))
        update.message.reply_text("黑澀會美眉 - Hello愛情風")
        self.go_back(update)

    def on_exit_chi7(self, update):
        print('Leaving chi7')
