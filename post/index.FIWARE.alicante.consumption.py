from post_FIWARE import SendData

config_ali = {
    'type':{
        'name': 'consumption',
        'time_name': 'stampm',
        'data_name': ['value']
    },
    'kafka':{
        'topics': [
            "predictions_alicante_alipark_flow",
            "predictions_alicante_benalua_flow",
            "predictions_alicante_autobuses_flow",
            "predictions_alicante_diputacion_flow",
            "predictions_alicante_mercado_flow",
            "predictions_alicante_montaneta_flow",
            "predictions_alicante_rambla_flow"
        ],
        'bootstrap_servers': "localhost:9092",
        'offset':'earliest'  #'earliest', 'latest'
    },
    'fiware':{
        'headers': {
            'Fiware-Service': 'alicante',
            'Content-Type': 'application/json',
        },
        'update': True,
        'url': 'http://5.53.108.182:1026/v2/entities/',
        'id': 'Consumption:Spain-Alicante-',
        'sensor_name_re': 'predictions_alicante_(.+)_flow'
    }
}

influx_config = {
        "token" : "----INFLOX_TOKEN-------",
        "org" : "naiades",
        "url" : "http://localhost:8086/"
    }

alicante_consumption = SendData(config_ali, config_influx=influx_config)

alicante_consumption.send()
