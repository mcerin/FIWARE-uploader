from post_FIWARE import SendData

config_ad = {
    'type':{
        'name': 'cosumption',
        'time_name': 'timestamp',
        'data_name': ['value']
    },
    'kafka':{
        'topics': [
            "anomalies_braila_flow_211106H360",
            "anomalies_braila_flow_211206H360",
            "anomalies_braila_flow_211306H360",
            "anomalies_braila_flow_318505H498",
            "anomalies_braila_pressure_5770",
            "anomalies_braila_pressure_5771",
            "anomalies_braila_pressure_5772",
            "anomalies_braila_pressure_5773"

        ],
        'bootstrap_servers': "localhost:9092",
        'offset':'earlist'
    },
    'fiware':{
        'headers': {
            'Fiware-Service': 'braila',
            'Content-Type': 'application/json',
        },
        'update': True,
        'url': 'http://5.53.108.182:1026/v2/entities/',
        'id': 'Consumption:Romania-Braila-',
        'sensor_name_re': 'anomalies_braila_(.+)'
    }
}

braila_anomaly = SendData(config_ad)

braila_anomaly.send()
