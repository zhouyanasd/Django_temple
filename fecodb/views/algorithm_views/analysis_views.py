from rest_framework.views import APIView
from django.http import JsonResponse

from sklearn.preprocessing import MinMaxScaler
import json
from numpy import *
import numpy as np

class AnalysisRWNN(APIView):
    # def normalization_min_max(self,arr):
    #     arr_n = arr
    #     for i in range(arr.size):
    #         x = float(arr[i] - np.min(arr)) / (np.max(arr) - np.min(arr))
    #         arr_n[i] = x
    #     return arr_n

    def post(self, request):
        conf_s = json.loads(request.data.get('conf_s')) # test_in  [0,2,...,699]  list
        conf_p =json.loads(request.data.get('conf_p'))
        data = json.loads(request.data.get('data'))

        nodes = int(conf_s['node'])
        in_w = float(conf_p['in_w'])
        train_in = data['train_in']
        train_out =data['train_out']
        test_in = data['test_in']

        train_in = train_in.replace('[','').replace(']','').split(',')
        train_in = [float(x) for x in train_in]
        train_in = np.asarray(train_in)
        train_in = train_in.reshape(int(len(train_in) / 700), 700)

        train_out = train_out.replace('[','').replace(']','').split(',')
        train_out = [float(x) for x in train_out]
        train_out = np.asarray(train_out)

        test_in = test_in.replace('[','').replace(']','').split(',')
        test_in = [float(x) for x in test_in]
        test_in = np.asarray(test_in)
        test_in = test_in.reshape(int(len(test_in) / 700), 700)

        min_max_scaler_in = MinMaxScaler()
        train_in = (min_max_scaler_in.fit_transform(train_in.T)).T
        test_in = (min_max_scaler_in.fit_transform(test_in.T)).T

        rows, columns = train_in.shape
        iw = random.random(size=(nodes, columns)) * in_w - in_w / 2
        iw = iw.T
        bias = random.random(nodes)
        biasmatrix = np.tile(bias, [rows, 1])
        temph = train_in.dot(iw) + biasmatrix
        H = 1 / (1 + exp(-temph))
        HH = np.linalg.pinv(H)
        lw = HH.dot(train_out)
        #### testing
        test_rows, test_columns = test_in.shape
        test_biasmatrix = np.tile(bias, [test_rows, 1])
        test_temph = test_in.dot(iw) + test_biasmatrix
        test_H = 1 / (1 + exp(-test_temph))
        prediction = test_H.dot(lw)[0]
        data={
            'prediction':prediction
        }
        return JsonResponse(data)