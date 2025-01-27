import pickle

class response:
    def __init__(self, responseText: str, nextConversation: str):
        if not isinstance(responseText, str):
           raise TypeError("responseText must be a string")
        if not isinstance(nextConversation, str):
           raise TypeError("next_conversation must be a string")
        self.responseText = responseText
        self.nextConversation = nextConversation


class conversation:
    def __init__(self, name: str, text: str, responses: list = []):
        if not isinstance(name, str):
            raise TypeError("conversationName must be a string")
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if not isinstance(responses, list):
            raise TypeError("responses must be a list")
        self.name = name
        self.text = text
        self.responses = responses
    
    @classmethod
    def automateMakingConversation(cls):
        conversationName = input("Enter the name of the conversation:\n")
        text = input("Enter what the NPC first says:\n")

        responses = []
        responsesCount = int(input("How many responses does your conversation have?\n"))

        if responsesCount != 0:
            for i in range(responsesCount):
                print("")
                print("Response No." + str(i+1))
                responseText = input("Enter what the user can reply with:\n")
                nextConversation = input("Enter what the name of the following conversation:\n")
                new_response = response(responseText, nextConversation)
                responses.append(new_response)

        new_conversation = conversation(conversationName, text, responses)
        return new_conversation
    
class NPC:
    def __init__(self, name: str, conversations: list = []):
        self.name = name
        self.conversations = conversations
        self.screen = None

    @classmethod
    def automateMakingNPC(cls):
        npcName = input("Enter the name of the NPC:\n")
        moreConversationsPlease = True
        conversations = []
        while moreConversationsPlease == True:
            ask = input("Do you want to add a conversation. Yes or no? ")
            if ask.lower()[0] == 'n':
                moreConversationsPlease = False
            if moreConversationsPlease == True:
                new_conversation = conversation.automateMakingConversation()
                conversations.append(new_conversation)

        newNPC = NPC(npcName, conversations)
        return newNPC
    
    
        
    def getConversation(self, conversationName):
        for x in self.conversations:
            if x.name == conversationName:
                return x
                
    
    

    @classmethod
    def fetchNpcData(cls):
        with open("NPCs.pkl", "rb") as npcFile:
            npcDatabase = pickle.load(npcFile)
                                
        return npcDatabase


