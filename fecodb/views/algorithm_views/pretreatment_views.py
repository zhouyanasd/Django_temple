from rest_framework.views import APIView
import numpy as np
import numpy
from django.http import JsonResponse
import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class PretreatmentSNV(APIView):
    def snv(self, input):
        # input = [0,2,...,699] np.array
        r, c = input.shape
        m = np.mean(input, 1)
        xt = np.tile(m, [c, 1])
        xt = xt.T
        dr = input - xt
        dr2 = numpy.square(dr)
        sumdr2 = dr2.sum(axis=1) / (c - 1)
        sqrtsumdr2 = numpy.sqrt(sumdr2)
        drr = np.tile(sqrtsumdr2, [c, 1])
        drr = drr.T
        xsnv = dr / drr
        # output  =  [0,2,...,699] np.array
        return xsnv

    def post(self, request):
        test_in = request.data.get('data')
        path = request.data.get('property_train_data_path')
        self.data = np.loadtxt(BASE_DIR+path, delimiter=",", skiprows=0)
        # string to float to nparray
        test_in = test_in.split(',')
        test_in = [float(x) for x in test_in]
        test_in = np.asarray(test_in)
        test_in = test_in.reshape(int(len(test_in) / 700), 700)
        # training data
        inputdata = self.data[:, 1:701]
        outputdata = self.data[:, 0]
        train_in = inputdata[0:770, :]
        train_in = self.snv(train_in)
        train_out = outputdata[0:770]
        # testing data
        test_in = self.snv(test_in)

        data = {}
        data['train_in'] = json.dumps(train_in.tolist())
        data['train_out'] = json.dumps(train_out.tolist())
        data['test_in'] = json.dumps(test_in.tolist())
        return JsonResponse(data)


class PretreatmentPCA(APIView):
    pass



class PretreatmentDIFF1(APIView):
    def diff1(self,input):
        differentiation1 = np.diff(input)
        return differentiation1

    def post(self, request):
        test_in = request.data.get('data')
        path = request.data.get('property_train_data_path')
        self.data = np.loadtxt(BASE_DIR + path, delimiter=",", skiprows=0)
        # string to float to nparray
        test_in = test_in.split(',')
        test_in = [float(x) for x in test_in]
        test_in = np.asarray(test_in)
        test_in = test_in.reshape(int(len(test_in) / 700), 700)

        inputdata = self.data[:, 1:701]
        outputdata = self.data[:, 0]
        train_in = inputdata[0:770, :]
        train_in = self.diff1(train_in)
        train_out = outputdata[0:770]
        # testing data
        test_in = self.diff1(test_in)
        test_in = np.hstack((test_in,np.array([[0]])))
        train_in = np.hstack((train_in,np.array([[0]]*770)))

        data = {}
        data['train_in'] = json.dumps(train_in.tolist())
        data['train_out'] = json.dumps(train_out.tolist())
        data['test_in'] = json.dumps(test_in.tolist())
        return JsonResponse(data)


class PretreatmentDIFF2(APIView):
    def diff2(self,input):
        differentiation2 = np.diff(input, 2)
        return differentiation2

    def post(self, request):
        test_in = request.data.get('data')
        path = request.data.get('property_train_data_path')
        self.data = np.loadtxt(BASE_DIR + path, delimiter=",", skiprows=0)
        # string to float to nparray
        test_in = test_in.split(',')
        test_in = [float(x) for x in test_in]
        test_in = np.asarray(test_in)
        test_in = test_in.reshape(int(len(test_in) / 700), 700)

        inputdata = self.data[:, 1:701]
        outputdata = self.data[:, 0]
        train_in = inputdata[0:770, :]
        train_in = self.diff2(train_in)
        train_out = outputdata[0:770]
        # testing data
        test_in = self.diff2(test_in)
        test_in = np.hstack((test_in, np.array([[0,0]])))
        train_in = np.hstack((train_in, np.array([[0,0]] * 770)))

        data = {}
        data['train_in'] = json.dumps(train_in.tolist())
        data['train_out'] = json.dumps(train_out.tolist())
        data['test_in'] = json.dumps(test_in.tolist())
        return JsonResponse(data)


class PretreatmentFAKE(APIView):
    def post(self, request):
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        test_in = request.data.get('data')
        path = request.data.get('property_train_data_path')
        self.data = np.loadtxt(BASE_DIR + path, delimiter=",", skiprows=0)
        # string to float to nparray
        test_in = test_in.split(',')
        test_in = [float(x) for x in test_in]
        test_in = np.asarray(test_in)
        test_in = test_in.reshape(int(len(test_in) / 700), 700)

        inputdata = self.data[:, 1:701]
        outputdata = self.data[:, 0]
        train_in = inputdata[0:770, :]
        train_out = outputdata[0:770]

        data = {}
        data['train_in'] = json.dumps(train_in.tolist())
        data['train_out'] = json.dumps(train_out.tolist())
        data['test_in'] = json.dumps(test_in.tolist())
        return JsonResponse(data)