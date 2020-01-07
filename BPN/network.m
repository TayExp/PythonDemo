load('matlab.mat')
[pn, inputStr] = mapminmax(input');
[tn, outputStr] = mapminmax(output');
net = newff(pn,tn,30);
%每10轮回显示一次结果
net.trainParam.show = 10;

%最大训练次数
net.trainParam.epochs = 1000;

%网络的学习速率
net.trainParam.lr = 0.05;

%训练网络所要达到的目标误差
net.trainParam.goal = 1e-4;

%进行训练
[net,tr]=train(net,pn,tn);
outputs  = sim(net, mapminmax(input_test'));
