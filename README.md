# HVV Display

This tool queries the [HVV Geofox API](https://gti.geofox.de/) for departures at stations and displays the results on a LED Matrix display via GPIO on a RaspberryPi (or equivalent device).

The file structure was created using the following command: (For more info refer to [this documentation](https://github.com/openapi-generators/openapi-python-client))

```bash
openapi-python-client update --url https://gti.geofox.de/v3/api-docs/public --config <path/to/config.yaml>
```

With this `config.yaml`:

```yaml
project_name_override: hvv_display
package_name_override: hvv_display_client
```


## TODOs

- [ ] Use client
- [ ] Request and cache line icons
- [ ] Generate image
- [ ] Display image
