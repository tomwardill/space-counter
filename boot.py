def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ACCESSPOINTNAME', 'ACCESSPOINTPASSWORD')
        while not sta_if.isconnected():
            pass
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    print('network config:', sta_if.ifconfig())


def enable_webrepl():
    import webrepl
    webrepl.start()


do_connect()
enable_webrepl()
