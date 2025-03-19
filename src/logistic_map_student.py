"""
Logistic映射与混沌系统研究
"""
import numpy as np
import matplotlib.pyplot as plt

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义 Logistic 模型迭代函数
# r 是 Logistic 模型中的参数，x0 是初始值，n 是迭代次数
def logistic_iteration(r, x0, n):
    # 创建一个长度为 n 的零数组，用于存储每次迭代的结果
    x = np.zeros(n)
    # 初始化第一次迭代的结果为初始值 x0
    x[0] = x0
    # 从第二次迭代开始，根据 Logistic 模型公式进行迭代计算
    for i in range(1, n):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x

# 任务 1：Logistic 模型的迭代
# 定义不同的 r 值，用于观察不同参数下系统的行为
r_values = [2, 3.2, 3.45, 3.6]
# 设定初始值
x0 = 0.5
# 设定迭代次数
n_iterations = 60

# 创建一个 2x2 的子图布局，用于分别展示不同 r 值下的迭代结果
fig1, axes = plt.subplots(2, 2, figsize=(10, 8))
# 将二维的 axes 数组展平为一维数组，方便后续操作
axes = axes.flatten()

# 遍历不同的 r 值
for i, r in enumerate(r_values):
    # 调用 logistic_iteration 函数进行迭代计算
    x = logistic_iteration(r, x0, n_iterations)
    # 在对应的子图中绘制迭代次数和 x 值的关系图
    axes[i].plot(range(n_iterations), x)
    # 设置子图的标题，显示当前的 r 值
    axes[i].set_title(f'r = {r}')
    # 设置子图的 x 轴标签
    axes[i].set_xlabel('迭代次数')
    # 设置子图的 y 轴标签
    axes[i].set_ylabel('x')

# 自动调整子图的布局，避免重叠
plt.tight_layout()

# 设置 figure1 的窗口标题
manager = plt.get_current_fig_manager()
manager.window.title('figure1')

# 任务 2：费根鲍姆图的绘制
# 定义 r 的取值范围，从 2.6 到 4，步长为 0.001
r_range = np.arange(2.6, 4, 0.001)
# 设定初始值
x0 = 0.5
# 设定总的迭代次数
n_total = 250
# 设定前 100 次迭代用于稳定系统，不记录结果
n_discard = 100
# 计算需要记录的迭代次数
n_record = n_total - n_discard

# 用于存储每个 r 值对应的记录的 x 值
x_values = []
# 遍历不同的 r 值
for r in r_range:
    # 调用 logistic_iteration 函数进行迭代计算
    x = logistic_iteration(r, x0, n_total)
    # 只记录后 150 次迭代的结果
    x_values.append(x[n_discard:])

# 创建一个新的图形窗口
fig2 = plt.figure(figsize=(10, 6))
# 遍历每个 r 值和对应的记录的 x 值
for r, x in zip(r_range, x_values):
    # 绘制散点图，横坐标为 r，纵坐标为 x
    plt.scatter([r] * len(x), x, s=0.1, color='k')

# 设置图形的标题
plt.title('费根鲍姆图')
# 设置 x 轴标签
plt.xlabel('r')
# 设置 y 轴标签
plt.ylabel('x')

# 设置 figure2 的窗口标题
manager = plt.get_current_fig_manager()
manager.window.title('figure2')

# 显示所有图形
plt.show()
