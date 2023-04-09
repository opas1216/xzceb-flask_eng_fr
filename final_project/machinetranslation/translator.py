
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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
    #write the code here
    frenchText = ""
    translation = language_translator.translate(
    text = englishText,
    model_id = 'en-es').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    print(f"translation= {translation}")
    # frenchText = translation[]
    return frenchText


# def frenchToEnglish(frenchText):
#     #write the code here
#     return englishText