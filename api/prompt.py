import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh-TW")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 7))
LANGUAGE_TABLE = {
  "zh-TW": "哈囉！",
  "en": "Hello!"
}

AI_GUIDELINES = '你是一個Pokemon Go大師，專門是寶可夢飛行領航員，對於寶可夢飛行的方法無所不知，可以協助幫忙轉換寶可夢100IV相關怪的資料'

class Prompt:
    """
    A class representing a prompt for a chatbot conversation.

    Attributes:
    - msg_list (list): a list of messages in the prompt
    """

    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "system", 
                "content": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             })    
    def add_msg(self, new_msg):
        """
        Adds a new message to the prompt.

        Args:
        - new_msg (str): the new message to be added
        """
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(0)
        self.msg_list.append({"role": "user", "content": new_msg})

    def generate_prompt(self):
        """
        Generates the prompt.

        Returns:
        - msg_list (list): the list of messages in the prompt
        """
        return self.msg_list
