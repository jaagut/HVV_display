from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.individual_route_service_type import IndividualRouteServiceType
from ..models.path import Path
from ..models.sd_name import SDName
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualRoute")


@attr.s(auto_attribs=True)
class IndividualRoute:
    """
    Attributes:
        start (SDName):
        dest (SDName):
        service_type (IndividualRouteServiceType):  Default: IndividualRouteServiceType.FOOTPATH.
        path (Union[Unset, Path]):
        paths (Union[Unset, List[Path]]):
        length (Union[Unset, int]):
        time (Union[Unset, int]):
    """

    start: SDName
    dest: SDName
    service_type: IndividualRouteServiceType = IndividualRouteServiceType.FOOTPATH
    path: Union[Unset, Path] = UNSET
    paths: Union[Unset, List[Path]] = UNSET
    length: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.to_dict()

        dest = self.dest.to_dict()

        service_type = self.service_type.value

        path: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        paths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = []
            for paths_item_data in self.paths:
                paths_item = paths_item_data.to_dict()

                paths.append(paths_item)

        length = self.length
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "dest": dest,
                "serviceType": service_type,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if paths is not UNSET:
            field_dict["paths"] = paths
        if length is not UNSET:
            field_dict["length"] = length
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = SDName.from_dict(d.pop("start"))

        dest = SDName.from_dict(d.pop("dest"))

        service_type = IndividualRouteServiceType(d.pop("serviceType"))

        _path = d.pop("path", UNSET)
        path: Union[Unset, Path]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = Path.from_dict(_path)

        paths = []
        _paths = d.pop("paths", UNSET)
        for paths_item_data in _paths or []:
            paths_item = Path.from_dict(paths_item_data)

            paths.append(paths_item)

        length = d.pop("length", UNSET)

        time = d.pop("time", UNSET)

        individual_route = cls(
            start=start,
            dest=dest,
            service_type=service_type,
            path=path,
            paths=paths,
            length=length,
            time=time,
        )

        individual_route.additional_properties = d
        return individual_route

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
