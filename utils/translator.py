from googletrans import Translator

translator = Translator()

def translate_text(text, target_language):
    """
    Translate text to target language.
    
    Args:
        text: Text to translate
        target_language: Language code ('hi' for Hindi, 'bn' for Bengali)
        
    Returns:
        str: Translated text
    """
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    
    except Exception as e:
        print(f"Translation error: {str(e)}")
        if target_language == 'hi':
            return "अनुवाद में त्रुटि हुई।"  
        elif target_language == 'bn':
            return "অনুবাদে ত্রুটি হয়েছে।" 
        else:
            return "Translation error occurred."
