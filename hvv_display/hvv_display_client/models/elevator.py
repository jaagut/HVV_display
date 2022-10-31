from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.elevator_button_type import ElevatorButtonType
from ..models.elevator_state import ElevatorState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Elevator")


@attr.s(auto_attribs=True)
class Elevator:
    """
    Attributes:
        lines (Union[Unset, List[str]]):
        label (Union[Unset, str]):
        cabin_width (Union[Unset, int]):
        cabin_length (Union[Unset, int]):
        door_width (Union[Unset, int]):
        description (Union[Unset, str]):
        elevator_type (Union[Unset, str]):
        button_type (Union[Unset, ElevatorButtonType]):
        state (Union[Unset, ElevatorState]):
        cause (Union[Unset, str]):
    """

    lines: Union[Unset, List[str]] = UNSET
    label: Union[Unset, str] = UNSET
    cabin_width: Union[Unset, int] = UNSET
    cabin_length: Union[Unset, int] = UNSET
    door_width: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    elevator_type: Union[Unset, str] = UNSET
    button_type: Union[Unset, ElevatorButtonType] = UNSET
    state: Union[Unset, ElevatorState] = UNSET
    cause: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lines: Union[Unset, List[str]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines

        label = self.label
        cabin_width = self.cabin_width
        cabin_length = self.cabin_length
        door_width = self.door_width
        description = self.description
        elevator_type = self.elevator_type
        button_type: Union[Unset, str] = UNSET
        if not isinstance(self.button_type, Unset):
            button_type = self.button_type.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        cause = self.cause

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lines is not UNSET:
            field_dict["lines"] = lines
        if label is not UNSET:
            field_dict["label"] = label
        if cabin_width is not UNSET:
            field_dict["cabinWidth"] = cabin_width
        if cabin_length is not UNSET:
            field_dict["cabinLength"] = cabin_length
        if door_width is not UNSET:
            field_dict["doorWidth"] = door_width
        if description is not UNSET:
            field_dict["description"] = description
        if elevator_type is not UNSET:
            field_dict["elevatorType"] = elevator_type
        if button_type is not UNSET:
            field_dict["buttonType"] = button_type
        if state is not UNSET:
            field_dict["state"] = state
        if cause is not UNSET:
            field_dict["cause"] = cause

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lines = cast(List[str], d.pop("lines", UNSET))

        label = d.pop("label", UNSET)

        cabin_width = d.pop("cabinWidth", UNSET)

        cabin_length = d.pop("cabinLength", UNSET)

        door_width = d.pop("doorWidth", UNSET)

        description = d.pop("description", UNSET)

        elevator_type = d.pop("elevatorType", UNSET)

        _button_type = d.pop("buttonType", UNSET)
        button_type: Union[Unset, ElevatorButtonType]
        if isinstance(_button_type, Unset):
            button_type = UNSET
        else:
            button_type = ElevatorButtonType(_button_type)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ElevatorState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ElevatorState(_state)

        cause = d.pop("cause", UNSET)

        elevator = cls(
            lines=lines,
            label=label,
            cabin_width=cabin_width,
            cabin_length=cabin_length,
            door_width=door_width,
            description=description,
            elevator_type=elevator_type,
            button_type=button_type,
            state=state,
            cause=cause,
        )

        elevator.additional_properties = d
        return elevator

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
