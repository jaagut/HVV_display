import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.link import Link
from ..models.location import Location
from ..models.time_range import TimeRange
from ..types import UNSET, Unset

T = TypeVar("T", bound="Announcement")


@attr.s(auto_attribs=True)
class Announcement:
    """
    Attributes:
        description (str):
        publication (TimeRange):
        validities (List[TimeRange]):
        last_modified (datetime.datetime):
        id (Union[Unset, str]):
        version (Union[Unset, int]):
        summary (Union[Unset, str]):
        locations (Union[Unset, List[Location]]):
        links (Union[Unset, List[Link]]):
        planned (Union[Unset, bool]):
        reason (Union[Unset, str]):
        broadcast_relevant (Union[Unset, bool]):
    """

    description: str
    publication: TimeRange
    validities: List[TimeRange]
    last_modified: datetime.datetime
    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    summary: Union[Unset, str] = UNSET
    locations: Union[Unset, List[Location]] = UNSET
    links: Union[Unset, List[Link]] = UNSET
    planned: Union[Unset, bool] = UNSET
    reason: Union[Unset, str] = UNSET
    broadcast_relevant: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        publication = self.publication.to_dict()

        validities = []
        for validities_item_data in self.validities:
            validities_item = validities_item_data.to_dict()

            validities.append(validities_item)

        last_modified = self.last_modified.isoformat()

        id = self.id
        version = self.version
        summary = self.summary
        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()

                locations.append(locations_item)

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                links.append(links_item)

        planned = self.planned
        reason = self.reason
        broadcast_relevant = self.broadcast_relevant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "publication": publication,
                "validities": validities,
                "lastModified": last_modified,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if summary is not UNSET:
            field_dict["summary"] = summary
        if locations is not UNSET:
            field_dict["locations"] = locations
        if links is not UNSET:
            field_dict["links"] = links
        if planned is not UNSET:
            field_dict["planned"] = planned
        if reason is not UNSET:
            field_dict["reason"] = reason
        if broadcast_relevant is not UNSET:
            field_dict["broadcastRelevant"] = broadcast_relevant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        publication = TimeRange.from_dict(d.pop("publication"))

        validities = []
        _validities = d.pop("validities")
        for validities_item_data in _validities:
            validities_item = TimeRange.from_dict(validities_item_data)

            validities.append(validities_item)

        last_modified = isoparse(d.pop("lastModified"))

        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        summary = d.pop("summary", UNSET)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = Location.from_dict(locations_item_data)

            locations.append(locations_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        planned = d.pop("planned", UNSET)

        reason = d.pop("reason", UNSET)

        broadcast_relevant = d.pop("broadcastRelevant", UNSET)

        announcement = cls(
            description=description,
            publication=publication,
            validities=validities,
            last_modified=last_modified,
            id=id,
            version=version,
            summary=summary,
            locations=locations,
            links=links,
            planned=planned,
            reason=reason,
            broadcast_relevant=broadcast_relevant,
        )

        announcement.additional_properties = d
        return announcement

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
