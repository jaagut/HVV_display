import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.single_ticket_optimizer_request_route_extra_fare_type import (
    SingleTicketOptimizerRequestRouteExtraFareType,
)
from ..models.single_ticket_optimizer_request_trip import (
    SingleTicketOptimizerRequestTrip,
)
from ..models.tariff_optimizer_regions import TariffOptimizerRegions
from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleTicketOptimizerRequestRoute")


@attr.s(auto_attribs=True)
class SingleTicketOptimizerRequestRoute:
    """
    Attributes:
        trip (List[SingleTicketOptimizerRequestTrip]):
        departure (datetime.datetime):
        arrival (datetime.datetime):
        tariff_regions (TariffOptimizerRegions):
        extra_fare_type (SingleTicketOptimizerRequestRouteExtraFareType):
        single_ticket_tariff_level_id (Union[Unset, int]):
    """

    trip: List[SingleTicketOptimizerRequestTrip]
    departure: datetime.datetime
    arrival: datetime.datetime
    tariff_regions: TariffOptimizerRegions
    extra_fare_type: SingleTicketOptimizerRequestRouteExtraFareType
    single_ticket_tariff_level_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trip = []
        for trip_item_data in self.trip:
            trip_item = trip_item_data.to_dict()

            trip.append(trip_item)

        departure = self.departure.isoformat()

        arrival = self.arrival.isoformat()

        tariff_regions = self.tariff_regions.to_dict()

        extra_fare_type = self.extra_fare_type.value

        single_ticket_tariff_level_id = self.single_ticket_tariff_level_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trip": trip,
                "departure": departure,
                "arrival": arrival,
                "tariffRegions": tariff_regions,
                "extraFareType": extra_fare_type,
            }
        )
        if single_ticket_tariff_level_id is not UNSET:
            field_dict["singleTicketTariffLevelId"] = single_ticket_tariff_level_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trip = []
        _trip = d.pop("trip")
        for trip_item_data in _trip:
            trip_item = SingleTicketOptimizerRequestTrip.from_dict(trip_item_data)

            trip.append(trip_item)

        departure = isoparse(d.pop("departure"))

        arrival = isoparse(d.pop("arrival"))

        tariff_regions = TariffOptimizerRegions.from_dict(d.pop("tariffRegions"))

        extra_fare_type = SingleTicketOptimizerRequestRouteExtraFareType(
            d.pop("extraFareType")
        )

        single_ticket_tariff_level_id = d.pop("singleTicketTariffLevelId", UNSET)

        single_ticket_optimizer_request_route = cls(
            trip=trip,
            departure=departure,
            arrival=arrival,
            tariff_regions=tariff_regions,
            extra_fare_type=extra_fare_type,
            single_ticket_tariff_level_id=single_ticket_tariff_level_id,
        )

        single_ticket_optimizer_request_route.additional_properties = d
        return single_ticket_optimizer_request_route

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
