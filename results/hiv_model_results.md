# HIV 病毒载量模型研究结果

## 病毒载量变化图

![4hiv1](https://github.com/user-attachments/assets/70aa71a1-3d3f-4581-8791-1d761dd88ca4)


## 模型预测图

![Figure_1](https://github.com/user-attachments/assets/cb06898b-b5b7-4214-9f0a-ad1443e25b87)
![Figure_2](https://github.com/user-attachments/assets/021e6a33-d0eb-42cc-8905-12b035bd9bd9)
![Figure_3](https://github.com/user-attachments/assets/5887ed8b-3a6e-4a8e-95cf-d3f3d22605cb)
![hiv](https://github.com/user-attachments/assets/73be6c24-d3cc-49a2-8607-e106d3ed5f44)


## 分析与结论

模型参数对病毒载量的影响
A 和 B：代表病毒载量中不同成分的初始 “贡献量”。
A：对应指数项 \(\text{A} \cdot e^{-\alpha t}\) 的初始值，A 越大，该部分在初始时刻的病毒载量越高；
B：对应指数项 \(\text{B} \cdot e^{-\beta t}\) 的初始值，B 越大，该部分在初始时刻的病毒载量越高。
alpha 和 beta：反映病毒载量的衰减速率。
alpha：决定 \(e^{-\alpha t}\) 的衰减速度，alpha 越大，对应部分的病毒载量随时间下降越快；
beta：决定 \(e^{-\beta t}\) 的衰减速度，beta 越大，对应部分的病毒载量随时间下降越快。

不同治疗方案下的预测结果
通过调整模型参数模拟不同治疗方案：
强抑制治疗：若治疗增强对病毒的抑制（如药物提升病毒清除效率），可增大 alpha 或 beta。此时，病毒载量公式中对应指数项衰减更快，预测结果为病毒载量随时间快速下降。
弱抑制治疗：若治疗效果有限，alpha 或 beta 较小，病毒载量下降缓慢，预测曲线会在较长时间内维持较高水平。
联合治疗模拟：同时调整多个参数（如增大 alpha 并减小 B），可综合预测联合治疗对病毒载量的抑制效果，通过对比不同参数组合下 viral_load 函数的计算结果与曲线，分析治疗方案的优劣。
