from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.coordinate import Coordinate
from ..models.map_entry import MapEntry
from ..types import UNSET, Unset

T = TypeVar("T", bound="Path")


@attr.s(auto_attribs=True)
class Path:
    """
    Attributes:
        track (List[Coordinate]):
        attributes (Union[Unset, List[str]]):
        tags (Union[Unset, List[MapEntry]]):
    """

    track: List[Coordinate]
    attributes: Union[Unset, List[str]] = UNSET
    tags: Union[Unset, List[MapEntry]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        track = []
        for track_item_data in self.track:
            track_item = track_item_data.to_dict()

            track.append(track_item)

        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "track": track,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        track = []
        _track = d.pop("track")
        for track_item_data in _track:
            track_item = Coordinate.from_dict(track_item_data)

            track.append(track_item)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = MapEntry.from_dict(tags_item_data)

            tags.append(tags_item)

        path = cls(
            track=track,
            attributes=attributes,
            tags=tags,
        )

        path.additional_properties = d
        return path

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
