# open-chat-video-editor
## 简介
Open Chat Video Editor是开源的短视频生成和编辑工具，整体技术框架如下：

![sys](https://user-images.githubusercontent.com/21036347/236424150-ff67dd18-5c6e-41ff-a865-340e63e8ff98.png)

目前具有以下特点：
- 1、**一键生成可用的短视频**，包括：配音、背景音乐、字幕等。

- 2、算法和数据均基于开源项目，方便技术交流和学习
- 3、支持多种输入数据，方便对各种各样的数据，一键转短视频，目前支持：
- [x] **短句转短视频**(Text2Video): 根据输入的简短文字，文本模型自动生成生成文案，并自动生成短视频
- [x] **网页链接转短视频**(URL2Video): 自动对网页的内容进行提取，生成视频文案，并自动生成短视频
- [ ] **长视频转短视频**(Long Video to Short Video): 对输入的长视频进行自动分析和自动摘要，并生成短视频
- 4、涵盖**生成模型**和**多模态检索模型**等多种主流算法和模型

文本生成上，支持：
- [x] ChatGPT 
- [ ] BELLE
- [ ] Alpaca
- [ ] Dolly 
等多种模型

视觉信息生成上，支持图像和视频两种模态，生成方式上，支持检索和生成两种模型，目前共有6种模式：
- [x] 图像检索
- [x] 图像生成（stable diffusion）
- [x] 先图像检索，再基于stable diffusion 进行图像生成
- [x] 视频检索
- [ ] 视频生成（stable diffusion）
- [ ] 视频检索后，再基于stable diffusion 进行视频生成

## 结果展示 
### 1 短句转短视频(Text2Video)
界面如下:
![text2video](https://user-images.githubusercontent.com/21036347/236427963-7e9a166b-c085-4af8-b691-5a67f3e865e5.png)
以输入文案：【小孩子养宠物】为例，利用文本模型（如：chatgpt 等），可以自动生成一个较长的短视频文案：
```
['小孩子养宠物', '可以更好地提升小孩子的责任感和独立感', '但也要慎重的选择合适的宠物', '因为只有经过一定的训练养成', '它们才能够成长起来', '一起玩耍和度过一段欢快的时光', '宠物不仅能够陪伴小孩子渡过寂寞时光', '还能培养小孩子处事冷静、自信以及情感交流和沟通能力', '在养宠物的过程中', '小孩子们可以唤醒和发掘他们被磨练出来的坚毅和耐力', '能够亲身体验到勤勉 和坚持的重要性'] 
```

根据不同的视频生成模式，可以生成不同的视频，各个模式对比如下: 

 **(1)图像检索** 

https://user-images.githubusercontent.com/21036347/236428839-9c3c3a2d-6163-4577-82f5-5815772f294f.mp4

**(2)图像生成(stable diffusion)** 

https://user-images.githubusercontent.com/21036347/236429111-b151f3b5-64d0-4572-8daa-29a78a3d1f3d.mp4

**(3)先图像检索，再基于stable diffusion 进行图像生成** 

https://user-images.githubusercontent.com/21036347/236429690-93ea7377-e233-4629-868f-ef953a4dfa4c.mp4

**(4)视频检索** 

https://user-images.githubusercontent.com/21036347/236430102-6054b28c-ebeb-42a2-880e-b2656fc32138.mp4

### 2网页转短视频(url2Video)
界面如下：

![url2video](https://user-images.githubusercontent.com/21036347/236430693-fe9b3d15-8da8-4a50-b7a9-b4dc93614076.png)

(1) 输入一个url, 例如：https://zh.wikipedia.org/wiki/%E7%BE%8E%E5%9B%BD%E7%9F%AD%E6%AF%9B%E7%8C%AB
其内容是：美国短毛猫的维基百科

![wiki](https://user-images.githubusercontent.com/21036347/236431138-5fbb6cf2-07c8-41a3-989d-64731a6891d4.png)

(2) 解析网页并自动摘要成短视频文案，结果如下：
```
['\n\n美国短毛猫', '是一种神奇又魔幻的宠物猫品种', '它们优雅可爱', '活力无比', '能拥有多达80多种头毛色彩', '最出名的是银虎斑', '其银色毛发中透着浓厚的黑色斑 
纹', '除此之外', '它们还非常温柔', '是非常适合家庭和人类相处的宠物', '并且平均寿命达15-20年', '这种可爱的猫 
品种', '正在受到越来越多人的喜爱', '不妨试试你也来养一只吧']

```
(3) 自动合成短视频
例如图像生成模式下生成的结果如下，其他模式不再一一对比

https://user-images.githubusercontent.com/21036347/236431745-9f61ebcc-91b5-4157-adf9-abf9c371e461.mp4 

### 3 长视频转短视频(Long Video to Short Video)
  **即将发布，敬请期待**


## 安装与使用 
### 环境安装
1.安装依赖环境
pip install -r http://requirements.txt

2  安装clip 
 pip install git+https://github.com/openai/CLIP.git
 
3 安装faiss 
 conda install -c pytorch faiss-cpu

### 代码执行




## 交流与学习 


## 声明 






