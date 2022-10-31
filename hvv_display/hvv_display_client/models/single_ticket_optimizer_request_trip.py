from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.single_ticket_optimizer_request_line import (
    SingleTicketOptimizerRequestLine,
)
from ..models.single_ticket_optimizer_request_station import (
    SingleTicketOptimizerRequestStation,
)

T = TypeVar("T", bound="SingleTicketOptimizerRequestTrip")


@attr.s(auto_attribs=True)
class SingleTicketOptimizerRequestTrip:
    """
    Attributes:
        start (SingleTicketOptimizerRequestStation):
        destination (SingleTicketOptimizerRequestStation):
        line (SingleTicketOptimizerRequestLine):
        vehicle_type (str):
    """

    start: SingleTicketOptimizerRequestStation
    destination: SingleTicketOptimizerRequestStation
    line: SingleTicketOptimizerRequestLine
    vehicle_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.to_dict()

        destination = self.destination.to_dict()

        line = self.line.to_dict()

        vehicle_type = self.vehicle_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "destination": destination,
                "line": line,
                "vehicleType": vehicle_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = SingleTicketOptimizerRequestStation.from_dict(d.pop("start"))

        destination = SingleTicketOptimizerRequestStation.from_dict(
            d.pop("destination")
        )

        line = SingleTicketOptimizerRequestLine.from_dict(d.pop("line"))

        vehicle_type = d.pop("vehicleType")

        single_ticket_optimizer_request_trip = cls(
            start=start,
            destination=destination,
            line=line,
            vehicle_type=vehicle_type,
        )

        single_ticket_optimizer_request_trip.additional_properties = d
        return single_ticket_optimizer_request_trip

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
