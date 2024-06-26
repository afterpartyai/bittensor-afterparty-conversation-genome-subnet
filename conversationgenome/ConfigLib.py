import os

from conversationgenome.utils.Utils import Utils

from dotenv import load_dotenv
load_dotenv()


class c:
    state = {
        "validator" : {
            "miners_per_window": 3,
        },
        "system" : {
            "mode": 'test',
            "scoring_version": 0.1,
        },
        "llm" : {
            #"type": 'spacy',
            #"type": os.environ.get("LLM_TYPE"),
            "type": 'openai',
        },

    }

    @staticmethod
    def get(section, key, default=None):
        out = default
        if section == "env":
            #print("env", os.environ.get(key))
            val = os.environ.get(key)
            if val:
                out = val
        else:
            out = Utils.get(c.state, "%s.%s" % (section, key), default)
        return out


    @staticmethod
    def set(section, key, val):
        if not section in c.state:
            c.state[section] = {}
        c.state[section][key] = val

