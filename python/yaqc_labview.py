import yaqc
import numpy as np
import json

def yaqc_labview_client(host,port):
    c=yaqc.Client(host=host, port=port)
    return c

#misc
def yaqc_labview_traits(client):
    return client.traits


#has-limits
def yaqc_labview_get_limits(client):
    limits=client.get_limits()
    return limits

def yaqc_labview_in_limits(client,position):
    inlimits=client.in_limits(position)
    return bool(inlimits)


#has-mapping
def yaqc_labview_get_channel_map(client,channel_name):
    mapid=client.get_channel_mappings()[channel_name][0]
    return client.get_mappings()[mapid]

def yaqc_labview_get_channel_map_units(client,channel_name):
    mapid=client.get_channel_mappings()[channel_name][0]
    return client.get_mapping_units()[mapid]

def yaqc_labview_get_mapping_id(client):
    mappingid=client.get_mapping_id()
    return int(mappingid)


#has-measure-trigger
def yaqc_labview_measure(client,loop):
    client.measure(loop)
    return

def yaqc_labview_stop_looping(client):
    client.stop_looping()
    return


#has-position
def yaqc_labview_get_destination(client):
    dest=client.get_destination()
    return dest

def yaqc_labview_get_units(client):
    units=client.get_units()
    return units 

def yaqc_labview_get_position(client):
    pos=client.get_position()
    return pos

def yaqc_labview_set_position(client,position):
    client.set_position(position)
    return

def yaqc_labview_set_relative(client,position):
    client.set_relative(position)
    return  


#has-transformed-position
def yaqc_labview_set_native_reference(client,coord):
    client.set_native_reference(coord)
    return

def yaqc_labview_get_native_reference(client):
    coord=client.get_native_reference()
    return coord

def yaqc_labview_set_native_position(client,coord):
    client.set_native_position(coord)
    return

def yaqc_labview_get_native_position(client):
    coord=client.get_native_position()
    return coord

def yaqc_labview_get_native_limits(client):
    lims=client.get_native_limits()
    return lims

def yaqc_labview_get_native_units(client):
    units=client.get_native_units()
    return str(units)

def yaqc_labview_get_native_destination(client):
    dest=client.get_native_destination()
    return dest


#has-turret
def yaqc_labview_get_turret(client):
    tur=client.get_turret()
    return tur

def yaqc_labview_get_turret_options(client):
    opt=client.get_turret_options()
    return opt

def yaqc_labview_set_turret(client,pos):
    client.set_turret(pos)
    return


#is-daemon
def yaqc_labview_busy(client):
    busy=client.busy()
    return bool(busy)

def yaqc_labview_id(client):
    id=client.id()
    return json.dumps(id)

def yaqc_labview_get_config_filepath(client):
    filepath=client.get_config_filepath()
    return filepath

def yaqc_labview_get_config(client):
    cfg=client.get_config()
    return cfg

def yaqc_labview_shutdown(client, restart):
    client.shutdown(restart)
    return

def yaqc_labview_get_state(client):
    state=client.get_state()
    return state


#is-discrete
def yaqc_labview_get_position_of_identifier(client, identifier):
    pos=client.get_position_identifiers()[identifier]
    return pos

def yaqc_labview_get_position_identifier_options(client):
    names=client.get_position_identifier_options()
    return names

def yaqc_labview_set_identifier(client,identifier):
    dest=client.set_identifier(identifier)
    return dest

def yaqc_labview_get_identifier(client):
    currentid=client.get_identifier()
    return str(currentid)


#is-homeable
def yaqc_labview_home(client):
    client.home()
    return 


#is-sensor
def yaqc_labview_get_measured_channel(client,channel_name):
    data=client.get_measured()
    return data[channel_name]

def yaqc_labview_get_measurement_id(client):
    id=client.get_measurement_id()
    return float(id)

def yaqc_labview_get_channel_names(client):
    return client.get_channel_names()

def yaqc_labview_get_channel_shapes(client, channel_name):
    shape=client.get_channel_shapes()[channel_name]
    return shape

def yaqc_labview_get_channel_units(client, channel_name):
    units=client.get_channel_units()[channel_name]
    return str(units)
