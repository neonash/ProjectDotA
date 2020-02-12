from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dota_analytics.config import dbConfig
import lightgbm as lgb

import pandas as pd
import traceback
from dota_analytics.models import TrainData,TestData,TrainTargets
import json
from django.core.serializers.json import DjangoJSONEncoder
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def getData(request):
    print("Fetching sample training data..")
    req = TrainTargets.objects.all().values()[:5]
    req1 = TrainData.objects.all().values()[:1]
    print("Train Targets data:", json.dumps(list(req1), cls=DjangoJSONEncoder))
    sample_object = json.dumps(list(req1), cls=DjangoJSONEncoder)
    return HttpResponse(json.dumps(list(req), cls=DjangoJSONEncoder), status=200)

def deparseTrainData(request):
    req = TrainData.objects.all().values()[:1]
    data = list(req)
    sample_object = data[0]
    #########DEPARSING CODE###############
    keys_list1 = [f'r{i}' for i in range(1, 6)]
    keys_list2 = [f'd{i}' for i in range(1, 6)]
    keys_list = keys_list1 + keys_list2
    final_values = []
    new_object = dict()
    for i in range(1, 6):
        new_object['player'] = f'r{i}'
        for c in ['gold', 'xp', 'health', 'level', 'hero_id']:
            new_object[c] = str(int(sample_object[f'r{i}_{c}']))
        final_values.append(new_object)
        new_object = {}
    for i in range(1, 6):
        new_object['player'] = f'd{i}'
        for c in ['gold', 'xp', 'health', 'level', 'hero_id']:
            new_object[c] = str(int(sample_object[f'd{i}_{c}']))
        final_values.append(new_object)
        new_object = {}

    return HttpResponse(json.dumps(final_values), status=200)

    ###########DEPARSING ENDS###############

@csrf_exempt
def parseData(request):
    records = request.POST['records']
    match_id = request.POST['match_id_hash']
    # print("Match details")
    # print(type(json.loads(records)))
    new_data = formatNewdata(json.loads(records),match_id)
    predictionvalue = predict(new_data)
    return HttpResponse(predictionvalue, status=200)

def predict(new_data):
    gbmModel = lgb.Booster(model_file=dbConfig.dict['modelPath'])
    y_pred = gbmModel.predict(new_data, num_iteration=gbmModel.best_iteration)

    return y_pred

def formatNewdata(records,match_id):
    new_obj = {}
    print(records)
    for i in records:
        new_obj[i['player'] + '_gold'] = int(i['gold'])
        new_obj[i['player'] + '_xp'] = int(i['xp'])
        new_obj[i['player'] + '_health'] = int(i['health'])
        new_obj[i['player'] + '_level'] = int(i['level'])
        new_obj[i['player'] + '_hero_id'] = int(i['hero_id'])

    new_obj['match_id_hash'] = match_id
    df = pd.DataFrame(new_obj, index=[0])
    df.set_index('match_id_hash', inplace=True)
    #Feature engineering for additional features like total ratio, mean ,std
    for c in ['gold', 'xp', 'health', 'level']:
        r_columns = [f'r{i}_{c}' for i in range(1, 6)]
        d_columns = [f'd{i}_{c}' for i in range(1, 6)]

        df['r_total_' + c] = df[r_columns].sum(1)
        df['d_total_' + c] = df[d_columns].sum(1)
        df['total_' + c + '_ratio'] = df['r_total_' + c] / df['d_total_' + c]

        df['r_std_' + c] = df[r_columns].std(1)
        df['d_std_' + c] = df[d_columns].std(1)
        df['std_' + c + '_ratio'] = df['r_std_' + c] / df['d_std_' + c]

        df['r_mean_' + c] = df[r_columns].mean(1)
        df['d_mean_' + c] = df[d_columns].mean(1)
        df['mean_' + c + '_ratio'] = df['r_mean_' + c] / df['d_mean_' + c]
    return df

