import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable


def sbox_nct():
    # 数据准备
    data = {
        "林达": {"T": 68, "M": 22, "T*M": 1496},
        "罗庆斌": {"T": 46, "M": 21, "T*M": 966},
        "Lin": {"T": 24, "M": 21, "T*M": 504},
        "Luo": {"T": 40, "M": 20, "T*M": 800},
        "刘嘉宏": {"T": 36, "M": 20, "T*M": 720},
        "本文S1": {"T": 32, "M": 20, "T*M": 640},
        "本文S2": {"T": 30, "M": 21, "T*M": 630},
        "本文S3": {"T": 12, "M": 50, "T*M": 600},
    }

    # 按来源分配颜色
    categories = list(data.keys())
    colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))  # 10种预设颜色[6](@ref)

    # 绘制散点图（实心小点）
    plt.figure(figsize=(10, 6))
    for i, (name, d) in enumerate(data.items()):
        plt.scatter(d["M"], d["T"], s=15, color=colors[i], edgecolor='black',
                    linewidth=0.5, label=name)

    # 绘制双曲线（冷色表示低T*M）
    C_values = [600, 800, 1000, 1500]
    colors_curve = plt.cm.cool(np.linspace(0.2, 1, len(C_values)))  # 冷色映射[3](@ref)
    x = np.linspace(0, 100, 100)
    for C, color in zip(C_values, colors_curve):
        y = C / x
        plt.plot(x, y, color=color, linestyle='-', linewidth=1,
                 label=f'T*M={C}')

    # 坐标轴与图例
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.xlabel('M(量子比特数量)', fontsize=12)
    plt.ylabel('T(Toffoli深度)', fontsize=12)
    plt.title('T-M Scatter Plot with Hyperbolic Contours', fontsize=14)
    plt.legend(loc='upper right', frameon=False, fontsize=8)  # 合并图例[8,10](@ref)

    # 显示颜色条（仅针对双曲线）
    sm = plt.cm.ScalarMappable(cmap=plt.cm.cool,
                               norm=plt.Normalize(vmin=600, vmax=1500))
    plt.colorbar(sm, label='T*M (越小越好)')

    plt.grid(alpha=0.3)
    plt.savefig('figs/sbox_nct.png')
    plt.show()


def sbox_clifford():
    data = {
        "Zou": {"T": 86, "M": 23, "T*M": 1978},
        "Lin(1)": {"T": 72, "M": 21, "T*M": 1512},
        "Lin(2)": {"T": 22, "M": 28, "T*M": 616},
        "刘嘉宏": {"T": 108, "M": 20, "T*M": 2160},
        "本文S4": {"T": 96, "M": 20, "T*M": 1920},
        "本文S5": {"T": 9, "M": 53, "T*M": 477},
        "本文S6": {"T": 6, "M": 63, "T*M": 378},
        "本文S7": {"T": 7, "M": 118, "T*M": 826},
    }

    # 颜色配置
    categories = list(data.keys())
    colors = plt.cm.tab20(np.linspace(0, 1, len(categories)))

    # 画布设置
    plt.figure(figsize=(14, 7))

    for i, (name, d) in enumerate(data.items()):
        plt.scatter(d["M"], d["T"], s=20, color=colors[i], edgecolor='black',
                    linewidth=0.5, label=name)

    # 绘制双曲线（冷色表示低T*M）
    C_values = [600, 800, 1000, 1500, 2000]
    colors_curve = plt.cm.cool(np.linspace(0.2, 1, len(C_values)))  # 冷色映射[3](@ref)
    x = np.linspace(0, 150, 150)
    for C, color in zip(C_values, colors_curve):
        y = C / x
        plt.plot(x, y, color=color, linestyle='-', linewidth=1,
                 label=f'T*M={C}')

    # 坐标轴与图例
    plt.xlim(0, 150)
    plt.ylim(0, 150)
    plt.xlabel('M(量子比特数量)', fontsize=12)
    plt.ylabel('T(T深度)', fontsize=12)
    plt.title('T-M Scatter Plot with Hyperbolic Contours', fontsize=14)
    plt.legend(loc='upper right', frameon=False, fontsize=8)  # 合并图例[8,10](@ref)

    # 显示颜色条（仅针对双曲线）
    sm = plt.cm.ScalarMappable(cmap=plt.cm.cool,
                               norm=plt.Normalize(vmin=600, vmax=1500))
    plt.colorbar(sm, label='T*M (越小越好)')

    plt.grid(alpha=0.3)
    plt.savefig('figs/sbox_clifford.png')
    plt.show()


def sm4_nct():
    data = {
        # "Lin(i=1)": {"T": 6144, "M": 261, "T*M": 1603584},
        "Lin(i=8)": {"T": 788, "M": 296, "T*M": 233248},
        # "Luo(i=1)": {"T": 20480, "M": 260, "T*M": 5324800},
        "Luo(i=8)": {"T": 1716, "M": 288, "T*M": 494208},
        # "本文S1(i=1)": {"T": 8192, "M": 260, "T*M": 2129920},
        "本文S1(i=8)": {"T": 1056, "M": 288, "T*M": 304128},
        # "本文S3(i=1)": {"T": 3072, "M": 290, "T*M": 890880},
        "本文S3(i=8)": {"T": 396, "M": 528, "T*M": 209088},
    }

    # 颜色配置
    categories = list(data.keys())
    colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))

    # 画布设置
    plt.figure(figsize=(14, 7), dpi=300)

    for i, (name, d) in enumerate(data.items()):
        plt.scatter(d["M"], d["T"], s=20, color=colors[i], edgecolor='black',
                    linewidth=0.5, label=name)

    # 绘制双曲线（冷色表示低T*M）
    C_values = [220000, 300000, 500000]
    colors_curve = plt.cm.cool(np.linspace(0.2, 1, len(C_values)))  # 冷色映射[3](@ref)
    x = np.linspace(0, 600, 150)
    for C, color in zip(C_values, colors_curve):
        y = C / x
        plt.plot(x, y, color=color, linestyle='-', linewidth=1,
                 label=f'T*M={C}')

    # 坐标轴与图例
    plt.xlim(0, 600)
    plt.ylim(0, 1800)
    plt.xlabel('M(量子比特数量)', fontsize=12)
    plt.ylabel('T(Toffoli深度)', fontsize=12)
    # plt.title('T*M等值曲线的散点图', fontsize=14)
    plt.legend(loc='upper right', frameon=False, fontsize=8)  # 合并图例[8,10](@ref)

    # 显示颜色条（仅针对双曲线）
    sm = plt.cm.ScalarMappable(cmap=plt.cm.cool,
                               norm=plt.Normalize(vmin=600, vmax=1500))
    plt.colorbar(sm, label='T*M (越小越好)')

    # plt.grid(alpha=0.3)
    plt.savefig('figs/sm4_nct.png')
    plt.show()


def sm4_clifford():
    data = {
        "Zou(i=8)": {"T": 231, "M": 1336, "T*M": 308616},
        "Lin(i=8)": {"T": 726, "M": 352, "T*M": 255552},
        # "本文S4(i=1)": {"T": 24576, "M": 260, "T*M": 6389760},
        "本文S7(i=8)": {"T": 231, "M": 1072, "T*M": 247632},
        "本文S6(i=8)": {"T": 198, "M": 632, "T*M": 125136},
    }

    # 颜色配置
    categories = list(data.keys())
    colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))

    # 画布设置
    plt.figure(figsize=(14, 7), dpi=300)

    for i, (name, d) in enumerate(data.items()):
        plt.scatter(d["M"], d["T"], s=20, color=colors[i], edgecolor='black',
                    linewidth=0.5, label=name)

    # 绘制双曲线（冷色表示低T*M）
    C_values = [140000, 250000, 300000]
    colors_curve = plt.cm.cool(np.linspace(0.2, 1, len(C_values)))  # 冷色映射[3](@ref)
    x = np.linspace(0, 1400, 150)
    for C, color in zip(C_values, colors_curve):
        y = C / x
        plt.plot(x, y, color=color, linestyle='-', linewidth=1,
                 label=f'T*M={C}')

    # 坐标轴与图例
    plt.xlim(0, 1400)
    plt.ylim(0, 800)
    plt.xlabel('M(量子比特数量)', fontsize=12)
    plt.ylabel('T(T深度)', fontsize=12)
    # plt.title('T*M等值曲线的散点图', fontsize=14)
    plt.legend(loc='upper right', frameon=False, fontsize=8)  # 合并图例[8,10](@ref)

    # 显示颜色条（仅针对双曲线）
    sm = plt.cm.ScalarMappable(cmap=plt.cm.cool,
                               norm=plt.Normalize(vmin=600, vmax=1500))
    plt.colorbar(sm, label='T*M (越小越好)')

    # plt.grid(alpha=0.3)
    plt.savefig('figs/sm4_clifford.png')
    plt.show()


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    sm4_nct()
    sm4_clifford()