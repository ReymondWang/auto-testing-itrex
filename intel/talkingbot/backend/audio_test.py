# from intel_extension_for_transformers.neural_chat.pipeline.plugins.audio.tts import TextToSpeech
# tts = TextToSpeech()
# text_to_speak = "Hello, this is a sample text."  # Replace with your text
# output_audio_path = "./output.wav"  # Replace with the desired output audio path
# voice = "default"  # You can choose between "default," "pat," or a custom voice
# tts.text2speech(text_to_speak, output_audio_path, voice)

from intel_extension_for_transformers.neural_chat.pipeline.plugins.audio.tts_multilang import MultilangTextToSpeech
# Initialize the TTS module
tts = MultilangTextToSpeech(stream_mode=True)
# Define the text you want to convert to speech
text_to_speak = "欢迎来到英特尔，welcome to Intel。こんにちは！"  # Replace with your multi-language text
# Specify the output audio path
output_audio_path = "./output.wav"  # Replace with your desired output audio path
# Perform text-to-speech conversion
tts.text2speech(text_to_speak, output_audio_path)