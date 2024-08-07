import os

import parcels


def create_fieldset(indices=None):
    file = os.path.join(os.path.dirname(__file__), "CROCO_idealized.nc")

    variables = {"U": "u", "V": "v", "W": "w", "h": "h"}
    dimensions = {
        "U": {"lon": "x_rho", "lat": "y_rho", "depth": "s_w", "time": "time"},
        "V": {"lon": "x_rho", "lat": "y_rho", "depth": "s_w", "time": "time"},
        "W": {"lon": "x_rho", "lat": "y_rho", "depth": "s_w", "time": "time"},
        "h": {"lon": "x_rho", "lat": "y_rho"},
    }
    fieldset = parcels.FieldSet.from_croco(
        file,
        variables,
        dimensions,
        allow_time_extrapolation=True,
        indices=indices,
        mesh="flat",
    )

    return fieldset
