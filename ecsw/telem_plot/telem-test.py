import telemtools

s = telemtools.stream(port='COM3', baudrate=115200)

s.load_template(file='telemetry_master.template')

