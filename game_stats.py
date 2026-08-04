import os
from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        # High scores should never be reset
        self.highscore = 0

        self.path = self._get_path()  # get file path to get A.T. highscore
        self.alltime_highscore = self._get_alltime_highscore(self.path)

    @staticmethod
    def _get_path():
        """Get path of all-time highscore TXT file."""
        home_dir = os.path.expanduser('~')

        if os.name == 'nt':  # Windows
            username = home_dir.split('\\')[-1]
        else:  # macOS/Linux
            username = home_dir.split('/')[-1]

        return Path(f"{username}_alltime_highscores.txt")

    @staticmethod
    def _get_alltime_highscore(path: Path):
        """Return all-time highscore int from TXT file.

        Create file and return 0 if it doesn't exist.
        """
        if path.exists():
            try:
                saved_score = int(path.read_text().strip())
            except ValueError:
                saved_score = 0
        else:
            saved_score = 0
            path.write_text('0')
        return saved_score

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
