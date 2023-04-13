import openai
import utils

def gpt3_chat(message: str)-> str:
    '''This function returns GPT's response to the input message'''
    messages.append({"role": "user", "content": message})
    # ChatGPT is powered by gpt-3.5-turbo, OpenAI’s most advanced language model.
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": response})
    return str(response)

def run_alexa():
    command = utils.take_command()
    print('- ', command)
    if not command:
        return True
    response = gpt3_chat(command)
    print('- ', response)
    utils.talk(response)
    return False

if __name__ == '__main__':
    
    openai.api_key = utils.open_file('openai_api_key.txt')
    messages=[{"role": "system", "content": "You are a helpful assistant."}]

    stop = False
    utils.talk("Hey, I'm Alexa, ask me anything.")
    while not stop:
        stop = run_alexa()