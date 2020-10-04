"""All exceptions for asyncpixel."""


class ApiError(Exception):
    """Raised when a error occurs on the api side."""

    def __init__(self, error: str, source: str = "unknown source") -> None:
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
