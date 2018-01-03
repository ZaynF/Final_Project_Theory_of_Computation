import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '470645006:AAFr8l_KiuLp4DMREMvpfHotHunWoUiht9o'
WEBHOOK_URL = 'https://d11507c5.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'eating',
        'rice',
        'ricelocation',
        'noodle',
        'noodlelocation',
        'fastfood',
        'fastfoodlocation',
        'music',
        'eng',
        'eng1',
        'eng2',
        'eng3',
        'eng4',
        'eng5',
        'eng6',
        'eng7',
        'eng8',
        'eng9',
        'eng10',
        'chi',
        'chi1',
        'chi2',
        'chi3',
        'chi4',
        'chi5',
        'chi6',
        'chi7',
        'chi8',
        'chi9',
        'chi10'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'eating',
            'conditions': 'is_going_to_eating'
        },
        {
            'trigger': 'advance',
            'source': 'eating',
            'dest': 'rice',
            'conditions': 'is_going_to_rice'
        },
        {
            'trigger': 'advance',
            'source': 'rice',
            'dest': 'ricelocation',
            'conditions': 'is_going_to_ricelocation'
        },
        {
            'trigger': 'advance',
            'source': 'eating',
            'dest': 'noodle',
            'conditions': 'is_going_to_noodle'
        },
        {
            'trigger': 'advance',
            'source': 'noodle',
            'dest': 'noodlelocation',
            'conditions': 'is_going_to_noodlelocation'
        },
        {
            'trigger': 'advance',
            'source': 'eating',
            'dest': 'fastfood',
            'conditions': 'is_going_to_fastfood'
        },
        {
            'trigger': 'advance',
            'source': 'fastfood',
            'dest': 'fastfoodlocation',
            'conditions': 'is_going_to_fastfoodlocation'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'music',
            'conditions': 'is_going_to_music'
        },
        {
            'trigger': 'advance',
            'source': 'music',
            'dest': 'eng',
            'conditions': 'is_going_to_eng'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng1',
            'conditions': 'is_going_to_eng1'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng2',
            'conditions': 'is_going_to_eng2'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng3',
            'conditions': 'is_going_to_eng3'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng4',
            'conditions': 'is_going_to_eng4'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng5',
            'conditions': 'is_going_to_eng5'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng6',
            'conditions': 'is_going_to_eng6'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng7',
            'conditions': 'is_going_to_eng7'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng8',
            'conditions': 'is_going_to_eng8'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng9',
            'conditions': 'is_going_to_eng9'
        },
        {
            'trigger': 'advance',
            'source': 'eng',
            'dest': 'eng10',
            'conditions': 'is_going_to_eng10'
        },
        {
            'trigger': 'advance',
            'source': 'music',
            'dest': 'chi',
            'conditions': 'is_going_to_chi'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi1',
            'conditions': 'is_going_to_chi1'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi2',
            'conditions': 'is_going_to_chi2'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi3',
            'conditions': 'is_going_to_chi3'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi4',
            'conditions': 'is_going_to_chi4'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi5',
            'conditions': 'is_going_to_chi5'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi6',
            'conditions': 'is_going_to_chi6'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi7',
            'conditions': 'is_going_to_chi7'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi8',
            'conditions': 'is_going_to_chi8'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi9',
            'conditions': 'is_going_to_chi9'
        },
        {
            'trigger': 'advance',
            'source': 'chi',
            'dest': 'chi10',
            'conditions': 'is_going_to_chi10'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'ricelocation',
                'noodlelocation',
                'fastfoodlocation',
                'eng1',
                'eng2',
                'eng3',
                'eng4',
                'eng5',
                'eng6',
                'eng7',
                'eng8',
                'eng9',
                'eng10',
                'chi1',
                'chi2',
                'chi3',
                'chi4',
                'chi5',
                'chi6',
                'chi7',
                'chi8',
                'chi9',
                'chi10'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    machine.get_graph().draw("state.png",prog="dot")
    app.run()
