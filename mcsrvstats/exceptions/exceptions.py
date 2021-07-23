"""All exceptions for mcsrvstats."""
from typing import Optional


class ApiError(Exception):
    """Raised when a error occurs on the api side."""

    def __init__(self, error: str, source: Optional[str] = "unknown source") -> None:
        """Error raised when api is not succesful.

        Args:
            error (str): Error message
            source (str, optional): Source of the error. Defaults to "unknown source".
        """
        self.message = f"The {source}API had {error}"
        super().__init__(self.message)

    def __str__(self) -> str:
        """Return error in readable format.

        Returns:
            str: string version of error
        """
        return self.message

class PlayerNotFound(Exception):
    """ Raised when a player is not found."""

    def __init__(self, username: str) -> None:
        """Erorr raised when player is not found

        Args:
            username (str): The username of the player.
        """
        self.message = f"The player {username} could not be found."
    
    def __str__(self) -> str:
        """Return error in readable format.

        Returns:
            str: string version of error.
        """

        return self.message