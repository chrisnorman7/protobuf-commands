"""protobuf_commands.

A module for creating commands based on Google's Protocol Buffer technology.
"""

from typing import Callable, Dict, Type, TypeVar, Generic

from attr import Factory, attrib, attrs
from google.protobuf.message import Message

from .command_pb2 import Command

T = TypeVar('T')
CommandType = Callable[[T, Message], None]
MessageType = Type[Message]


@attrs(auto_attribs=True, repr=False, str=False)
class CommandFactory(Generic[T]):
    """A factory to hold the commands."""

    classes: Dict[str, MessageType] = attrib(default=Factory(dict), init=False)

    commands: Dict[MessageType, CommandType] = attrib(
        default=Factory(dict), init=False
    )

    def command(
        self, type_: MessageType
    ) -> Callable[[CommandType], CommandType]:
        """Add a new command.

        :param type_: The type this command will work with.
        """

        def inner(func: CommandType) -> CommandType:
            """Add the command."""
            self.classes[type_.__name__] = type_
            self.commands[type_] = func
            return func

        return inner

    def make_command(self, message: Message) -> Command:
        """Make a command instance from the given message."""
        return Command(
            name=type(message).__name__,
            data=message.SerializeToString()
        )

    def load_command(self, cmd: Command) -> Message:
        """Load the intended object from a Command instance."""
        cls: MessageType = self.classes[cmd.name]
        return cls.FromString(cmd.data)  # type:ignore[attr-defined]

    def build_command(self, buffer: bytes) -> Command:
        """Load a ``1Command`` instance from a buffer."""
        return Command.FromString(buffer)

    def get_function(self, cls: MessageType) -> CommandType:
        """Return the appropriate function."""
        return self.commands[cls]

    def run_function(
        self, func: CommandType, context: T, obj: Message
    ) -> None:
        """Run the provided function with the provided context and object."""
        return func(context, obj)

    def handle_string(self, context: T, buffer: bytes) -> None:
        """Handle the provided string."""
        cmd: Command = self.build_command(buffer)
        obj: Message = self.load_command(cmd)
        cls: MessageType = type(obj)
        func: CommandType = self.get_function(cls)
        return self.run_function(func, context, obj)
