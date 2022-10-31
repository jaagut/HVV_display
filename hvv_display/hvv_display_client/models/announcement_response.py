import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.announcement import Announcement
from ..models.announcement_response_return_code import AnnouncementResponseReturnCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnouncementResponse")


@attr.s(auto_attribs=True)
class AnnouncementResponse:
    """
    Attributes:
        return_code (AnnouncementResponseReturnCode):
        last_update (datetime.datetime):
        error_text (Union[Unset, str]):
        error_dev_info (Union[Unset, str]):
        announcements (Union[Unset, List[Announcement]]):
    """

    return_code: AnnouncementResponseReturnCode
    last_update: datetime.datetime
    error_text: Union[Unset, str] = UNSET
    error_dev_info: Union[Unset, str] = UNSET
    announcements: Union[Unset, List[Announcement]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_code = self.return_code.value

        last_update = self.last_update.isoformat()

        error_text = self.error_text
        error_dev_info = self.error_dev_info
        announcements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.announcements, Unset):
            announcements = []
            for announcements_item_data in self.announcements:
                announcements_item = announcements_item_data.to_dict()

                announcements.append(announcements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnCode": return_code,
                "lastUpdate": last_update,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if error_dev_info is not UNSET:
            field_dict["errorDevInfo"] = error_dev_info
        if announcements is not UNSET:
            field_dict["announcements"] = announcements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        return_code = AnnouncementResponseReturnCode(d.pop("returnCode"))

        last_update = isoparse(d.pop("lastUpdate"))

        error_text = d.pop("errorText", UNSET)

        error_dev_info = d.pop("errorDevInfo", UNSET)

        announcements = []
        _announcements = d.pop("announcements", UNSET)
        for announcements_item_data in _announcements or []:
            announcements_item = Announcement.from_dict(announcements_item_data)

            announcements.append(announcements_item)

        announcement_response = cls(
            return_code=return_code,
            last_update=last_update,
            error_text=error_text,
            error_dev_info=error_dev_info,
            announcements=announcements,
        )

        announcement_response.additional_properties = d
        return announcement_response

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
