def connect(force=False):
    import network

    ssid = "SSID"
    password = "secret"

    station = network.WLAN(network.STA_IF)

    if not force and station.isconnected() == True:
        print("Device connected. Nothing to do.")
        return

    station.active(True)
    station.connect(ssid, password)

    # Waiting for connection
    while station.isconnected() == False:
        pass

    print("Connection successful.")
    print(station.ifconfig())