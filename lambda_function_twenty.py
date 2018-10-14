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

def computer_number(comp_numb):
    return {"ComputerNumber": comp_numb}

def set_number(intent, session):

    card_title = "Number Select"
    session_attributes = {}
    should_end_session = False
    intNumber=0
    

    if 'num' in intent['slots']:
        user_num = intent['slots']['num']['value']
        if user_num == "1":
            
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                        "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                            "You can tell me your number by saying, " \
                            "my number is one."
        elif user_num== "2":
            
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "3":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "4":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "5":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                "You can tell me your number by saying, " \
                                "my number is one."
        
        elif user_num == "6":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                "You can tell me your number by saying, " \
                                "my number is one."
        elif user_num == "7":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "8":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "9":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "10":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "11":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "12":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "13":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "14":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "15":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "16":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "17":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        elif user_num == "18":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num=random.randint(intNumber+1,intNumber+2)
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
        
        elif user_num == "19":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                intNumber=int(user_num)
                comp_num= 20
                comp_num=str(comp_num)
                session_attributes = computer_number(comp_num)
                speech_output = "My number is " + \
                                comp_num + " Your turn! " \
                                "Say your number by saying my number is two"
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
       
        elif user_num == "20":
            if session.get('attributes', {}) and "ComputerNumber" in session.get('attributes', {}):
                comp_old_num = session['attributes']['ComputerNumber']
            else:
                comp_old_num="0"
            n1=int(user_num)
            c1=int(comp_old_num)
            if n1 == c1+1 or n1 == c1+2:
            
                speech_output = "Congratulations, You have won the game! " 
                reprompt_text = "You can say your number by saying, " \
                                "my number is one"
            else:
                speech_output = "Sorry, You said a wrong number " \
                               "Please try again."
                reprompt_text = "I'm not sure what your number is. " \
                                    "You can tell me your number by saying, " \
                                    "my number is one."
            speech_output = "Congratulations, You have won the game! " 
            reprompt_text = "You can say your number by saying, " \
                            "my number is one"
        else:
            speech_output = "Say a valid number " \
                            "Please try again."
            reprompt_text = "I'm not sure what your number is. " \
                            "You can tell me your number by saying, " \
                            "my number is one."
    else:
        speech_output = "Sorry, I'm not sure what your number is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your number is. " \
                            "You can tell me your number by saying, " \
                            "my number is one."
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
