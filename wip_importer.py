"""Developed by Alan Oliveira & Victor Gualberto - 2017

This package contains serialization, birthing and batch association
functions to serial numbers in MES.

The MES DB entry is done by the COM+ Data Importer.
"""


def panel_birth(customer,
               serials,
               mask,
               panel_type,
               assembly,
               equipment,
               factory_ma_route):

    """Serializes and births a panel in MES

    :param customer: CUSTOMER / DIVISION. ex.: "INGENICO / INGENICO"
    :param serials: list with all serial numbers to the panel
    :param mask: MES serial number mask for the assembly (serials
    are going to be checked against it
    :param panel_type: MES panel type field. ex.: "4*4 (16 UN)"
    :param assembly: ASSEMBLY / REVISION / VERSION
    :param equipment: equipment associated to the birth step
    of the route
    :param factory_ma_route: ex.: BETIM / MA BOARD / TAURUS

    :return: 'true' if the file in COM+ was able to be
    created. That means there were no empty parameters.
    'false' if any parameter was empty, and the file is not created
    in MES COM+ Wip directory.
    """


def panel_birth_batch(customer,
                    serials,
                    mask,
                    panel_type,
                    assembly,
                    equipment,
                    factory_ma_route,
                    batch_id):

    """Serializes, birth and associate a panel to a batch in MES

    :param customer: CUSTOMER / DIVISION. ex.: "INGENICO / INGENICO"
    :param serials: list with all serial numbers to the panel
    :param mask: MES serial number mask for the assembly (serials
    are going to be checked against it
    :param panel_type: MES panel type field. ex.: "4*4 (16 UN)"
    :param assembly: ASSEMBLY / REVISION / VERSION
    :param equipment: equipment associated to the birth step
    of the route
    :param factory_ma_route: ex.: BETIM / MA BOARD / TAURUS
    :param batch_id: string with the name of the batch (new or
    existing one)

    :return: 'true' if the file in COM+ was able to be
    created. That means there were no empty parameters.
    'false' if any parameter was empty, and the file is not created
    in MES COM+ Wip directory.
    """
