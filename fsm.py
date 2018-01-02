from transitions.extensions import GraphMachine
import vlc


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
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

    def is_going_to_eng8(self, update):
        text = update.message.text
        return text.lower() == '8'

    def is_going_to_eng9(self, update):
        text = update.message.text
        return text.lower() == '9'

    def is_going_to_eng10(self, update):
        text = update.message.text
        return text.lower() == '10'
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
        update.message.reply_text("How about Ri-Thi(gen dien fan)?")

    def on_exit_rice(self, update):
        print('Leaving rice')

    def on_enter_ricelocation(self, update):
        update.message.reply_text("It's on Yu Le street no.238")
        self.go_back(update)

    def on_exit_ricelocation(self, update):
        print('Leaving ricelocation')

    #noodle

    def on_enter_noodle(self, update):
        update.message.reply_text("How about Tien Men Wu?")

    def on_exit_noodle(self, update):
        print('Leaving noodle')

    def on_enter_noodlelocation(self, update):
        update.message.reply_text("It's on Yu Le street no.79")
        self.go_back(update)

    def on_exit_noodlelocation(self, update):
        print('Leaving noodlelocation')

    #fastfood

    def on_enter_fastfood(self, update):
        update.message.reply_text("How about Rainbow Castle?")

    def on_exit_fastfood(self, update):
        print('Leaving fastfood')

    def on_enter_fastfoodlocation(self, update):
        update.message.reply_text("It's on Da Chua road 22 aglley no.19-1")
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
        update.message.reply_text("1.Against The Current - Something You Need\n2.Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat\n3.Don Omar-Danza Kuduro Lyrics\n4.From Ashes To New - Same Old Story\n5.Linkin Park - Leave Out All The Rest\n6.OneRepublic-Secrets\n7.Phillip Phillips - Gone, Gone, Gone\n8.Simple Plan - Jet Lag ft. Marie-Mai\n9.Simple Plan - Shut Up!\n10.The Cab - Angel With A Shotgun")

    def on_exit_eng(self, update):
        print('Leaving eng')

    #1.Against The Current - Something You Need
    def on_enter_eng1(self, update):
        p = vlc.MediaPlayer('music/Eng/Against The Current - Something You Need.mp3')
        p.play()

        update.message.reply_text("Against The Current - Something You Need")
        self.go_back(update)

    def on_exit_eng1(self, update):
        print('Leaving eng1')

    #2.Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat
    def on_enter_eng2(self, update):
        p = vlc.MediaPlayer('music/Eng/Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat.mp3')
        p.play()

        update.message.reply_text("Alex Goot, Kurt Schneider, and Chrissy Costanza - Beauty and Beat")
        self.go_back(update)

    def on_exit_eng2(self, update):
        print('Leaving eng2')

    #3.Don Omar-Danza Kuduro Lyrics
    def on_enter_eng3(self, update):
        p = vlc.MediaPlayer('music/Eng/Don Omar-Danza Kuduro.mp3')
        p.play()

        update.message.reply_text("Don Omar-Danza Kuduro")
        self.go_back(update)

    def on_exit_eng3(self, update):
        print('Leaving eng3')

    #4.From Ashes To New - Same Old Story
    def on_enter_eng4(self, update):
        p = vlc.MediaPlayer('music/Eng/From Ashes To New - Same Old Story.mp3')
        p.play()

        update.message.reply_text("From Ashes To New - Same Old Story")
        self.go_back(update)

    def on_exit_eng4(self, update):
        print('Leaving eng4')

    #5.Linkin Park - Leave Out All The Rest
    def on_enter_eng5(self, update):
        p = vlc.MediaPlayer('music/Eng/Linkin Park - Leave Out All The Rest.mp3')
        p.play()

        update.message.reply_text("Linkin Park - Leave Out All The Rest")
        self.go_back(update)

    def on_exit_eng5(self, update):
        print('Leaving eng5')

    #6.OneRepublic-Secrets
    def on_enter_eng6(self, update):
        p = vlc.MediaPlayer('music/Eng/OneRepublic-Secrets.mp3')
        p.play()

        update.message.reply_text("OneRepublic-Secrets")
        self.go_back(update)

    def on_exit_eng6(self, update):
        print('Leaving eng6')

    #7.Phillip Phillips - Gone, Gone, Gone
    def on_enter_eng7(self, update):
        p = vlc.MediaPlayer('music/Eng/Phillip Phillips - Gone, Gone, Gone.mp3')
        p.play()

        update.message.reply_text("Phillip Phillips - Gone, Gone, Gone")
        self.go_back(update)

    def on_exit_eng7(self, update):
        print('Leaving eng7')

    #8.Simple Plan - Jet Lag ft. Marie-Mai
    def on_enter_eng8(self, update):
        p = vlc.MediaPlayer('music/Eng/Simple Plan - Jet Lag ft. Marie-Mai.mp3')
        p.play()

        update.message.reply_text("Simple Plan - Jet Lag ft. Marie-Mai")
        self.go_back(update)

    def on_exit_eng8(self, update):
        print('Leaving eng8')

    #9.Simple Plan - Shut Up!
    def on_enter_eng9(self, update):
        p = vlc.MediaPlayer('music/Eng/Simple Plan - Shut Up!.mp3')
        p.play()

        update.message.reply_text("Simple Plan - Shut Up!")
        self.go_back(update)

    def on_exit_eng9(self, update):
        print('Leaving eng9')

    #10.The Cab - Angel With A Shotgun
    def on_enter_eng10(self, update):
        p = vlc.MediaPlayer('music/Eng/The Cab - Angel With A Shotgun.mp3')
        p.play()

        update.message.reply_text("The Cab - Angel With A Shotgun")
        self.go_back(update)

    def on_exit_eng10(self, update):
        print('Leaving eng10')
