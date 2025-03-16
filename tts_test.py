import pyttsx3
import time

def test_tts(language='fr'):
    # Initialiser le moteur TTS
    print("Initialisation du moteur Text-to-Speech...")
    engine = pyttsx3.init()
    
    # Afficher les voix disponibles
    voices = engine.getProperty('voices')
    print(f"Nombre de voix disponibles: {len(voices)}")
    
    # Afficher toutes les voix disponibles et leurs propriétés
    french_voices = []
    english_voices = []
    
    for i, voice in enumerate(voices):
        print(f"Voix {i}: {voice.name} ({voice.id})")
        print(f"   Langues: {voice.languages}")
        # La détection précise dépend du système, recherche basique par nom de voix
        if 'fr' in voice.id.lower() or 'french' in voice.name.lower():
            french_voices.append(voice)
        if 'en' in voice.id.lower() or 'english' in voice.name.lower():
            english_voices.append(voice)
    
    # Sélectionner la voix selon la langue choisie
    selected_voice = None
    if language.lower() == 'fr':
        print("\nSélection d'une voix française...")
        if french_voices:
            selected_voice = french_voices[0]
        else:
            print("Aucune voix française détectée, recherche d'une voix avec 'fr' dans l'ID...")
            for voice in voices:
                if 'fr' in str(voice.id).lower():
                    selected_voice = voice
                    break
    elif language.lower() == 'en':
        print("\nSélection d'une voix anglaise...")
        if english_voices:
            selected_voice = english_voices[0]
        else:
            # Sur Windows, la voix 0 est souvent anglaise
            selected_voice = voices[0]
    
    # Appliquer la voix sélectionnée
    if selected_voice:
        print(f"Voix sélectionnée: {selected_voice.name}")
        engine.setProperty('voice', selected_voice.id)
    else:
        print("Impossible de trouver une voix appropriée. Utilisation de la voix par défaut.")
    
    # Configurer les propriétés
    engine.setProperty('rate', 150)  # Vitesse de parole (défaut: 200)
    engine.setProperty('volume', 1.0)  # Volume (défaut: 1.0)
    
    # Phrases de test en français et en anglais
    if language.lower() == 'fr':
        phrases = [
            "Bonjour, je suis votre assistant pour personnes aveugles.",
            "Il y a une chaise devant vous.",
            "Attention, escalier à deux mètres.",
            "Porte à votre droite."
        ]
    else:  # English
        phrases = [
            "Hello, I am your assistant for visually impaired people.",
            "There is a chair in front of you.",
            "Caution, stairs two meters ahead.",
            "Door on your right."
        ]
    
    # Tester chaque phrase
    for i, phrase in enumerate(phrases):
        print(f"\nTest {i+1}: '{phrase}'")
        engine.say(phrase)
        engine.runAndWait()
        time.sleep(0.5)  # Pause entre les phrases
    
    print("\nTest TTS terminé avec succès.")

if __name__ == "__main__":
    # Pour tester le français:
    print("=== TEST EN FRANÇAIS ===")
    test_tts('fr')
    
    # Pour tester l'anglais:
    print("\n\n=== TEST EN ANGLAIS ===")
    test_tts('en')
    
    # Vous pouvez aussi le rendre interactif:
    """
    language = input("Choisissez une langue (fr/en): ").strip().lower()
    if language in ['fr', 'en']:
        test_tts(language)
    else:
        print("Langue non reconnue. Utilisation du français par défaut.")
        test_tts('fr')
    """