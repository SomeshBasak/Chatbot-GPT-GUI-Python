import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_resources(self, user_input):
        response = openai.Completion.create(
            model="text-davinci-003",
            promt=user_input,
            max_tokens=100,
            temperature=1
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds?")
    print(response)
