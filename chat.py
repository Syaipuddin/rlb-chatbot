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
        for (pattern, responses) in self._pairs:
            keysentence = pattern.pattern.replace("(", "").replace(")", "").replace("|", " ")

            similiarity = jaro.jaro_winkler_metric(str, keysentence)

            percentage[f"{sequence}"] = similiarity if similiarity else 0
            sequence += 1

        # sort the percentage dict into the highest one first
        sorted_sim = dict(sorted(percentage.items(), key=lambda x: x[1], reverse=True))
        listed_sorted_key_sim = list(sorted_sim)
        highest_sim_key = listed_sorted_key_sim[0]

        # print(sorted_sim)

        # if the highest similiarty value bigger than n return response
        # if percentage[highest_sim_key] > 0.70:
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
