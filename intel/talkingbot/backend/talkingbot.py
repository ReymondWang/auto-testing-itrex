from intel_extension_for_transformers.neural_chat import NeuralChatServerExecutor

def main():
    server_executor = NeuralChatServerExecutor()
    server_executor(config_file="./talkingbot.yaml", log_file="./talkingbot.log")

if __name__ == "__main__":
    main()