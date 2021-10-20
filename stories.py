"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, key, title, words, text):
        """Create story with words and template text."""

        self.key = key
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story_1 = Story(
    "one",
    "Once upon a time",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# ans = {"place": "Antarctica", "noun": "coconut clusters", "verb": "sled", "adjective": "velvety", "plural_noun": "cats"}

story_2 = Story(
    "two",
    "Afternoon Baking",
    ["noun", "baking_ingredient", "adjective", "emotion", "verb_past"],
    """Today I baked a {noun}. I put so much {baking_ingredient} that it came out a little {adjective}. That's okay though, I was still {emotion} because my friends {verb_past} all of it."""
)

story_3 = Story(
    "three",
    "A Sports Affair",
    ["sport", "number", "country", "adjective"],
    """On my spare time I like to play {sport}. I have been playing since I was {number} years old. Last year I played in {country}. It was super {adjective}!"""
)

story_4 = Story(
    "four",
    "Quarantine",
    ["number", "emotion", "verb", "adverb", "name", "place"],
    """Yesterday was day {number} of quarantine. I was feeling so {emotion} that I stormed into the kitchen where I {verb} {adverb}. After I did I called {name} to tell them what I had done. They couldn't believe it! I said, "What else am I supposed to do?! If this continues for a few more weeks, I might just fly away to {place}!" """
)

story_5 = Story(
    "five",
    "Pet Adventure",
    ["animal", "verb", "adjective", "plural_noun", "place", "emotion"],
    """I have always wanted a {animal} to {verb} with and love. I would pet its {adjective} head and give them lots of {plural_noun}. We would go on walks in the {place} and make everybody {emotion}"""
)


stories = { 
    "one": story_1,
    "two": story_2,
    "three": story_3,
    "four": story_4,
    "five": story_5
}