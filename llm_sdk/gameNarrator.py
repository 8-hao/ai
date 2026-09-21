from . import Small_LLM_Model


class GameNarrator:
    def __init__(self):
        self.model = Small_LLM_Model()
        self.result = ""


    def generate(self):
        prompt = self._build_prompt()
        # while '^' not in self.result:
        input_ids = self.model.encode(prompt)
        print(input_ids)




    def _build_prompt(self, won: bool, score: int) -> str:
        if won:
            return (
                f"The player just won the pacman game with a score of {score}. "
                "Write one short, upbeat congratulatory sentence, in character "
                "as a playful Pac-Man narrator.end you senten with doule ^"
            )
        return (
            f"The player just lost the pacman game with a score of {score}. "
            "Write one short, encouraging sentence telling them to try again, "
            "in character as a playful Pac-Man narrator. end you senten with doule ^"
        )
