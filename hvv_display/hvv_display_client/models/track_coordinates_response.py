from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.track_coordinates_response_return_code import (
    TrackCoordinatesResponseReturnCode,
)
from ..models.vehicle_map_path import VehicleMapPath
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackCoordinatesResponse")


@attr.s(auto_attribs=True)
class TrackCoordinatesResponse:
    """
    Attributes:
        return_code (TrackCoordinatesResponseReturnCode):
        track_i_ds (List[str]):
        tracks (List[VehicleMapPath]):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
    """

    return_code: TrackCoordinatesResponseReturnCode
    track_i_ds: List[str]
    tracks: List[VehicleMapPath]
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        track_i_ds = self.track_i_ds

        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()

            tracks.append(tracks_item)

        error_text = self.error_text
        error_dev_info = self.error_dev_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "trackIDs": track_i_ds,
                "tracks": tracks,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = TrackCoordinatesResponseReturnCode(d.pop("returnCode"))

        track_i_ds = cast(List[str], d.pop("trackIDs"))

        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = VehicleMapPath.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        track_coordinates_response = cls(
            return_code=return_code,
            track_i_ds=track_i_ds,
            tracks=tracks,
            error_text=error_text,
            error_dev_info=error_dev_info,
        )

        track_coordinates_response.additional_properties = d
        return track_coordinates_response

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
