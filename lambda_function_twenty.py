from __future__ import print_function
import random


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Twenty Twenty. " \
                    "Please tell me your number by saying, " \
                    "my number is one"
    reprompt_text = "Please tell me your number by saying, " \
                    "my option is one."
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for playing Twenty Twenty. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def computer_number(comp_number):
    return {"ComputerNumber": comp_number}

def set_number(intent, session):

    card_title = "Number Select"
    session_attributes = {}
    should_end_session = False

    if 'num' in intent['slots']:
        user_num = intent['slots']['num']['value']
        if user_num == "1":
            num1 = 1
            comp_num=random.randint(num1+1,num1+2)
            session_attributes = computer_number(comp_number)
            speech_output = "My number is " + \
                            comp_num + " Your turn! " \
                            "Say your number by saying my number is two"
            reprompt_text = "You can say your number by saying, " \
                            "my number is one"
        elif user_num== "2":
            speech_output = "I now know your number is " + \
                            user_num + \
                            ". You can ask me about animal by saying, " \
                            "tell me about animal name?"
            reprompt_text = "You can ask me about animal by saying, " \
                            "tell me about animal name?"
        elif user_num == "3":
            speech_output = "I now know your number is " + \
                            user_num + \
                            ". You can ask me about ngos by saying, " \
                            "tell me about ngos name?"
            reprompt_text = "You can ask me about ngos by saying, " \
                            "tell me about ngos name?"
        else:
            speech_output = "Say a valid number " \
                            "Please try again."
            reprompt_text = "I'm not sure what your choice is. " \
                            "You can tell me your choice by saying, " \
                            "my option is one."
    else:
        speech_output = "Sorry, I'm not sure what your number is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your choice is. " \
                            "You can tell me your choice by saying, " \
                            "my option is one."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
'''

def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

'''
# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "WhatIsNumber":
        return set_number(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])