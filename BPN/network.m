load('matlab.mat')
[pn, inputStr] = mapminmax(input');
[tn, outputStr] = mapminmax(output');
net = newff(pn,tn,30);
%ÿ10�ֻ���ʾһ�ν��
net.trainParam.show = 10;

%���ѵ������
net.trainParam.epochs = 1000;

%�����ѧϰ����
net.trainParam.lr = 0.05;

%ѵ��������Ҫ�ﵽ��Ŀ�����
net.trainParam.goal = 1e-4;

%����ѵ��
[net,tr]=train(net,pn,tn);
outputs  = sim(net, mapminmax(input_test'));
