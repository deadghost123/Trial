from google_trans_new import google_translator
def translate(text,lang):
    translator = google_translator()
    translate_text = translator.translate(text,lang_src='en',lang_tgt='hi')
    return translate_text