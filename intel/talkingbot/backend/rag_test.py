from intel_extension_for_transformers.neural_chat import PipelineConfig
from intel_extension_for_transformers.neural_chat import plugins
plugins.retrieval.enable=True
plugins.retrieval.args['embedding_model'] = "hkunlp/instructor-large" 
plugins.retrieval.args["input_path"]="../story/sample.jsonl"
config = PipelineConfig(plugins=plugins)

from intel_extension_for_transformers.neural_chat import build_chatbot
chatbot = build_chatbot(config)
response = chatbot.predict("请讲一个太公钓鱼的故事")
