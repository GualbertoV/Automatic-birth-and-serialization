"""Developed by Alan Oliveira & Victor Gualberto - 2017
This module instanciates the EPS Controls Web Service functions.

Each function is documentated below
"""

import requests
import xml.etree.ElementTree as Et


def mov_in(equipment_id, routestep_id, customer_id, serial_number):

    """Makes MES 'mouviment in' in a serial number
    Inputs:

    equipmentID - Equipment's ID in MES
    routeStepID - Route Step's ID in MES
    customerID - Customer's ID in MES
    serial_number - Serial number to make movement

    Outputs:

    String with WS's result

    """

    request = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" +
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <BoardMovementIn_PV xmlns="http://tempuri.org/">
          <SerialNumber>""" + serial_number + """</SerialNumber>
          <RouteStep_ID>""" + routestep_id + """</RouteStep_ID>
          <Equipment_ID>""" + equipment_id + """</Equipment_ID>
          <Customer_ID>""" + customer_id + """</Customer_ID>
        </BoardMovementIn_PV>
      </soap:Body>
    </soap:Envelope>"""

    encoded_request = request.encode('utf-8')

    headers = {"Host": "brbelm0apps02",
               "Content-Type": "text/xml; charset=utf-8",
               "Content-Length": str(len(encoded_request)),
               "SOAPAction": "http://tempuri.org/BoardMovementIn_PV"}

    response = requests.post(url="http://brbelm0apps02/JabilTest_EPSControls/JabilTest_EPSControls.asmx",
                             headers=headers,
                             data=encoded_request,
                             verify=False)

    root = Et.fromstring(response.text)
    return root[0][0][0].text


def mov_out(equipment_id, routestep_id, customer_id, serial_number):

    """Makes MES 'mouviment out' in a serial number

    Inputs:

    equipmentID - Equipment's ID in MES
    routeStepID - Route Step's ID in MES
    customerID - Customer's ID in MES
    serial_number - Serial number to make movement

    Outputs:

    String with WS's result

    """

    request = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" +
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <BoardMovementOut_PV xmlns="http://tempuri.org/">
          <SerialNumber>""" + serial_number + """</SerialNumber>
          <RouteStep_ID>""" + routestep_id + """</RouteStep_ID>
          <Equipment_ID>""" + equipment_id + """</Equipment_ID>
          <Customer_ID>""" + customer_id + """</Customer_ID>
        </BoardMovementOut_PV>
      </soap:Body>
    </soap:Envelope>"""

    encoded_request = request.encode('utf-8')

    headers = {"Host": "brbelm0apps02",
               "Content-Type": "text/xml; charset=utf-8",
               "Content-Length": str(len(encoded_request)),
               "SOAPAction": "http://tempuri.org/BoardMovementOut_PV"}

    response = requests.post(url="http://brbelm0apps02/JabilTest_EPSControls/JabilTest_EPSControls.asmx",
                             headers=headers,
                             data=encoded_request,
                             verify=False)

    root = Et.fromstring(response.text)
    return root[0][0][0].text


def change_batch(batch_id, customer_id, serial_number):

    """Modifies the batch of a given serial number, using EPS Controls

    Inputs:

    batchID - The new batch (must exist in MES)
    customerID - The customer ID of the serial number in MES
    serial_number - The serial number's batch to move

    Outputs:

    String with WS's result

    Obs.: if the serial number does not belong to a batch, then
    it will be associated to one.
    """

    request = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" +
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <ChangeBatch xmlns="http://tempuri.org/">
          <SerialNumber>""" + serial_number + """</SerialNumber>
          <Customer_ID>""" + customer_id + """</Customer_ID>
          <Batch>""" + batch_id + """</Batch>
        </ChangeBatch>
      </soap:Body>
    </soap:Envelope>"""

    encoded_request = request.encode('utf-8')

    headers = {"Host": "brbelm0apps02",
               "Content-Type": "text/xml; charset=utf-8",
               "Content-Length": str(len(encoded_request)),
               "SOAPAction": "http://tempuri.org/ChangeBatch"}

    response = requests.post(url="http://brbelm0apps02/JabilTest_EPSControls/JabilTest_EPSControls.asmx",
                             headers=headers,
                             data=encoded_request,
                             verify=False)

    root = Et.fromstring(response.text)
    return root[0][0][0].text
