from enum import Enum


class ApplicationVariables(Enum):
    """
    Client variables
    """
    # Running client's status value.
    CLIENT_RUNNING_STATUS = 1
    # Paused client's status value.
    CLIENT_PAUSED_STATUS = 2

    """
    Server variables
    """
    # Running server's status value.
    SERVER_RUNNING_STATUS = 1
    # Stopped server's status value.
    SERVER_STOPPED_STATUS = 2

    """
    Shared variables
    """
    # The host name for the connection.
    HOST = ""
    # The port's number used for the connection.
    PORT = 53000
    # The buffer's size value used to store incoming messages.
    BUFFER_SIZE = 4096

    """
    Command variables
    """
    # The quit command which close the client's communication with the serve.
    QUIT_MESSAGE = "!quit"
    # The command to set client's status on pause.
    CLIENT_PAUSED_MESSAGE = "!pause"
    # The command to set client's status on running.
    CLIENT_RUNNING_MESSAGE = "!run"