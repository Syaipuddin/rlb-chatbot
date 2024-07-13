import nltk.chat.util as util
import jaro
import random

class ChatExtended(util.Chat):
    pass

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # count the match for each response
        percentage = {}
        # store the pairs sequence
        sequence = 0

        # check each pattern
        for (pattern, response) in self._pairs:
            # store similirity value
            sim_value = 0

            # split rule into words
            keysentence = pattern.pattern.replace("(", "").replace(")", "").replace("|", " ").split()

            # split prompt into words
            str_words = str.split()

            for word in str_words:
                for key in keysentence:
                    # count the similiarity of each word from rule and prompt using jaro winkler fuzzy string methods
                    similiarity = jaro.jaro_winkler_metric(word, key)
                    if similiarity >= 1:
                        sim_value += 1

            percentage[f"{sequence}"] = sim_value
            sequence += 1

        # sort the percentage dict into the highest one first
        sorted_sim = dict(sorted(percentage.items(), key=lambda x: x[1], reverse=True))
        listed_sorted_key_sim = list(sorted_sim)
        highest_sim_key = listed_sorted_key_sim[0]

        # if the highest similiarty value bigger than n return response
        if percentage[highest_sim_key] > 1:
            pattern = self._pairs[int(highest_sim_key)][0]
            response = self._pairs[int(highest_sim_key)][1]


            resp = random.choice(response)  # pick a random response
            resp = self._wildcards(resp, pattern)  # process wildcards

            # fix munged punctuation at the end
            if resp[-2:] == "?.":
                resp = resp[:-2] + "."
            if resp[-2:] == "??":
                resp = resp[:-2] + "?"
            return resp
