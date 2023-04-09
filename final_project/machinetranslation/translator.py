"""This is the practice for using API with IBM-Watson Language Translator"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-04-09',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)




def englishToFrench(englishText):
    """This is the method for translate english to french."""
    #write the code here
    translation = language_translator.translate(
    text = englishText,
    model_id = 'en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """This is the method for translate french to english."""
    #write the code here
    translation = language_translator.translate(
    text = frenchText,
    model_id = 'fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    englishText = translation['translations'][0]['translation']
    return englishText
