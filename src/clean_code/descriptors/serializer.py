"""Classes for field transformations and a dataclass representing a login event."""

from datetime import datetime, timezone
from typing import Callable, Union, Any, Optional, cast
from functools import partial
from dataclasses import dataclass


class BaseFieldTransformation(object):
    """Base class for field transformations."""

    def __init__(self, transformation_func: Callable[[Any], str]) -> None:
        """Initialize BaseFieldTransformation.

        Parameters
        ----------
        transformation_func : callable
            A function for transforming field values.
        """
        self.transformation_func = transformation_func
        self._name: Optional[str] = None

    def __set_name__(self, owner: Any, name: str) -> None:
        """Set the name of the field being transformed."""
        self._name = name

    def __get__(
        self,
        instance: Optional[Any],
        owner: Any,
    ) -> Union[Any, "BaseFieldTransformation"]:
        """Get the transformed value of the field."""
        if instance is None:
            return self
        raw_data = instance.__dict__[self._name]
        return self.transformation_func(raw_data)

    def __set__(self, instance: Any, value: Any) -> None:
        """Set the value of the field."""
        instance.__dict__[self._name] = value


ShowOriginal = partial(BaseFieldTransformation, transformation_func=lambda value: value)
HideField = partial(BaseFieldTransformation, transformation_func=lambda value: "***")
FormatTime = partial(
    BaseFieldTransformation,
    transformation_func=lambda ft: cast(str, ft.strftime("%Y-%m-%d %H:%M")),
)


@dataclass
class LoginEvent:
    """Dataclass representing a login event."""

    username: str = cast(str, ShowOriginal())
    password: str = cast(str, HideField())
    ip: str = cast(str, ShowOriginal())
    timestamp: Union[str, datetime] = cast(Union[str, datetime], FormatTime())

    def serialize(self) -> dict[str, str]:
        """Serialize the login event data into a dictionary."""
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,  # type: ignore
        }


if __name__ == "__main__":
    login_event = LoginEvent(
        "john", "secret password", "1.1.1.1", datetime.now(timezone.utc)
    )
    print(vars(login_event))
    print(login_event.serialize())
    print(login_event.password)
